"""Analise semantica da linguagem Cifra.

Percorre a arvore sintatica produzida pelo parser e verifica regras que a
gramatica sozinha nao consegue garantir. Sao acumulados dois tipos de
diagnostico:

  * erros  -> impedem a geracao de codigo (a melodia esta "incorreta");
  * avisos -> nao impedem a geracao, apenas alertam o usuario.

Verificacoes implementadas:
  1. Compasso estourado: a soma das duracoes entre duas barras "|" nao pode
     ultrapassar a capacidade definida pela formula de compasso.
  2. Frase nao declarada: "toca X" exige que exista uma "frase X".
  3. Frase redeclarada: duas frases nao podem ter o mesmo nome.
  4. Duracao invalida: o denominador da figura deve ser uma figura conhecida.
  5. Nota fora da tonalidade: se um "tom" foi declarado, toda nota deve
     pertencer a escala correspondente.
  6. Instrumento desconhecido: o instrumento (global ou de trilha) deve estar
     na lista suportada.
  7. Valores fora de faixa: tempo, formula de compasso, contador de "repita" e
     volume de trilha.
  8. Marcas de tempo: "espere X" exige uma "marca X" definida (resolvida
     globalmente, ver linha_tempo.resolver_marcas), que nao aponte para um
     instante ja passado; "marca X" nao pode ser duplicada nem aparecer dentro
     de "repita".

Alem disso, emite avisos para frases declaradas e nunca usadas e para
compassos incompletos.
"""

from cifra.gerado.CifraParser import CifraParser
from cifra import musica
from cifra import linha_tempo


class Diagnostico:
    """Representa uma mensagem de erro ou aviso associada a uma linha."""

    def __init__(self, linha, mensagem, nivel):
        self.linha = linha
        self.mensagem = mensagem
        self.nivel = nivel  # "erro" ou "aviso"

    def __str__(self):
        return "Linha {}: {}".format(self.linha, self.mensagem)


class AnalisadorSemantico:
    """Reúne as configuracoes globais e valida toda a arvore do programa."""

    def __init__(self):
        self.erros = []
        self.avisos = []

        # Configuracoes com seus valores padrao.
        self.tempo = 120
        self.instrumento = "piano"
        self.compasso = (4, 4)
        self.tom = None  # tupla (classe, modo) ou None quando nao ha checagem de tom

        # Frases declaradas: nome -> contexto; e o conjunto de frases efetivamente usadas.
        self.frases = {}
        self.frases_usadas = set()

        # Marcas de tempo: nome -> instante (em fracao de semibreve). Resolvidas
        # globalmente (ver linha_tempo.resolver_marcas), entao a ordem das trilhas
        # nao importa. self._marcas_definidas detecta nomes repetidos.
        self.marcas = {}
        self._marcas_definidas = set()

    # ------------------------------------------------------------------ #
    # API principal
    # ------------------------------------------------------------------ #
    def analisar(self, programa):
        """Executa todas as fases da analise sobre o contexto 'programa'."""
        self._coletar_configuracoes(programa)
        self._coletar_frases(programa)

        # Resolve os instantes de todas as marcas de uma vez (ordem-independente).
        self.marcas = linha_tempo.resolver_marcas(programa.musica(), self.frases)

        # Valida o conteudo de cada frase (duracoes, tonalidade e compassos).
        for declaracao in programa.declaracao():
            eventos = declaracao.evento()
            self._validar_eventos(eventos)
            self._validar_compassos(eventos)

        # Valida o bloco principal.
        self._validar_musica(programa.musica())

        # Avisa sobre frases declaradas e nunca tocadas.
        for nome, contexto in self.frases.items():
            if nome not in self.frases_usadas:
                self._aviso(contexto.start.line, "frase '{}' declarada mas nunca usada".format(nome))

        return self.erros, self.avisos

    # ------------------------------------------------------------------ #
    # Coleta de configuracoes e frases
    # ------------------------------------------------------------------ #
    def _coletar_configuracoes(self, programa):
        for cfg in programa.configuracao():
            if isinstance(cfg, CifraParser.ConfigTempoContext):
                valor = int(cfg.INT().getText())
                if valor < musica.TEMPO_MINIMO or valor > musica.TEMPO_MAXIMO:
                    self._erro(cfg.start.line,
                               "tempo {} fora da faixa permitida ({}-{} BPM)".format(
                                   valor, musica.TEMPO_MINIMO, musica.TEMPO_MAXIMO))
                else:
                    self.tempo = valor

            elif isinstance(cfg, CifraParser.ConfigInstrumentoContext):
                nome = cfg.IDENT().getText()
                if nome not in musica.INSTRUMENTOS_VALIDOS:
                    self._erro(cfg.start.line,
                               "instrumento '{}' desconhecido (use um de: {})".format(
                                   nome, ", ".join(sorted(musica.INSTRUMENTOS_VALIDOS))))
                else:
                    self.instrumento = nome

            elif isinstance(cfg, CifraParser.ConfigTomContext):
                self.tom = (cfg.NOTA_CLASSE().getText(), cfg.MODO().getText())

            elif isinstance(cfg, CifraParser.ConfigCompassoContext):
                numerador = int(cfg.INT(0).getText())
                denominador = int(cfg.INT(1).getText())
                if numerador <= 0 or denominador not in musica.DURACOES_VALIDAS:
                    self._erro(cfg.start.line,
                               "formula de compasso {}/{} invalida".format(numerador, denominador))
                else:
                    self.compasso = (numerador, denominador)

    def _coletar_frases(self, programa):
        for declaracao in programa.declaracao():
            nome = declaracao.IDENT().getText()
            if nome in self.frases:
                self._erro(declaracao.start.line, "frase '{}' ja declarada anteriormente".format(nome))
            else:
                self.frases[nome] = declaracao

    # ------------------------------------------------------------------ #
    # Validacao do bloco principal
    # ------------------------------------------------------------------ #
    def _validar_musica(self, musica_ctx):
        trilhas = musica_ctx.trilha()
        if trilhas:
            for trilha in trilhas:
                instrumento = trilha.IDENT().getText()
                if instrumento not in musica.INSTRUMENTOS_VALIDOS:
                    self._erro(trilha.start.line,
                               "instrumento '{}' desconhecido (use um de: {})".format(
                                   instrumento, ", ".join(sorted(musica.INSTRUMENTOS_VALIDOS))))
                if trilha.INT() is not None:
                    volume = int(trilha.INT().getText())
                    if volume < musica.VOLUME_MINIMO or volume > musica.VOLUME_MAXIMO:
                        self._erro(trilha.start.line,
                                   "volume {} fora da faixa permitida ({}-{})".format(
                                       volume, musica.VOLUME_MINIMO, musica.VOLUME_MAXIMO))
                self._validar_comandos(trilha.comando())
                self._validar_marcas(trilha.comando())
        else:
            self._validar_comandos(musica_ctx.comando())
            self._validar_marcas(musica_ctx.comando())

    def _validar_comandos(self, comandos, topo=True):
        """Valida uma lista de comandos e os compassos dos trechos literais.

        'toca', 'repita', 'marca' e 'espere' interrompem a contagem de compassos:
        cada trecho contiguo de eventos escritos diretamente e conferido
        isoladamente. 'marca'/'espere' so podem aparecer no nivel da trilha.
        """
        trecho_atual = []
        for comando in comandos:
            if isinstance(comando, CifraParser.ComandoEventoContext):
                evento = comando.evento()
                trecho_atual.append(evento)
                self._validar_evento(evento)
            elif isinstance(comando, CifraParser.ComandoTocaContext):
                self._validar_compassos(trecho_atual)
                trecho_atual = []
                self._validar_toca(comando)
            elif isinstance(comando, CifraParser.ComandoRepitaContext):
                self._validar_compassos(trecho_atual)
                trecho_atual = []
                self._validar_repita(comando)
            elif isinstance(comando, (CifraParser.ComandoMarcaContext, CifraParser.ComandoEspereContext)):
                self._validar_compassos(trecho_atual)
                trecho_atual = []
                if not topo:
                    self._erro(comando.start.line,
                               "marca/espere nao pode aparecer dentro de repita")
        self._validar_compassos(trecho_atual)

    def _validar_toca(self, comando):
        nome = comando.IDENT().getText()
        if nome not in self.frases:
            self._erro(comando.start.line, "frase '{}' nao declarada".format(nome))
        else:
            self.frases_usadas.add(nome)

    def _validar_repita(self, comando):
        vezes = int(comando.INT().getText())
        if vezes <= 0:
            self._erro(comando.start.line, "repita deve ter um numero positivo de repeticoes")
        self._validar_comandos(comando.comando(), topo=False)

    def _validar_marcas(self, comandos):
        """Valida as marcas e esperas de uma trilha usando os instantes ja resolvidos.

        Detecta marca com nome repetido, 'espere' de marca inexistente e 'espere'
        que apontaria para um instante ja passado nesta trilha.
        """
        cursor = 0.0
        epsilon = 1e-9
        for comando in comandos:
            if isinstance(comando, CifraParser.ComandoMarcaContext):
                nome = comando.IDENT().getText()
                if nome in self._marcas_definidas:
                    self._erro(comando.start.line, "marca '{}' ja definida anteriormente".format(nome))
                else:
                    self._marcas_definidas.add(nome)
            elif isinstance(comando, CifraParser.ComandoEspereContext):
                nome = comando.IDENT().getText()
                if nome not in self.marcas:
                    self._erro(comando.start.line, "marca '{}' nao definida".format(nome))
                elif self.marcas[nome] < cursor - epsilon:
                    self._erro(comando.start.line,
                               "espere '{}' aponta para um instante ja passado".format(nome))
                else:
                    cursor = self.marcas[nome]
            else:
                cursor += linha_tempo.duracao_comando(comando, self.frases)

    # ------------------------------------------------------------------ #
    # Validacao de eventos (notas, acordes, pausas)
    # ------------------------------------------------------------------ #
    def _validar_eventos(self, eventos):
        for evento in eventos:
            self._validar_evento(evento)

    def _validar_evento(self, evento):
        if isinstance(evento, CifraParser.EventoNotaContext):
            self._validar_nota(evento.nota())
        elif isinstance(evento, CifraParser.EventoAcordeContext):
            self._validar_acorde(evento.acorde())
        elif isinstance(evento, CifraParser.EventoPausaContext):
            self._validar_duracao(evento.pausa().duracao())
        elif isinstance(evento, CifraParser.EventoPercussaoContext):
            self._validar_duracao(evento.percussao().duracao())

    def _validar_nota(self, nota):
        self._validar_duracao(nota.duracao())
        self._validar_tonalidade(nota.ALTURA())

    def _validar_acorde(self, acorde):
        self._validar_duracao(acorde.duracao())
        for altura in acorde.ALTURA():
            self._validar_tonalidade(altura)

    def _validar_duracao(self, duracao):
        # Cada figura ligada por '~' deve usar um denominador de figura conhecido.
        for figura in duracao.figura():
            denominador = int(figura.INT().getText())
            if denominador not in musica.DURACOES_VALIDAS:
                self._erro(figura.start.line, "duracao 1/{} invalida (use {})".format(
                    denominador, ", ".join(str(d) for d in sorted(musica.DURACOES_VALIDAS))))

    def _validar_tonalidade(self, terminal_altura):
        if self.tom is None:
            return
        texto = terminal_altura.getText()
        tonica, modo = self.tom
        if not musica.altura_esta_na_tonalidade(texto, tonica, modo):
            self._erro(terminal_altura.symbol.line,
                       "nota '{}' nao pertence a tonalidade {} {}".format(texto, tonica, modo))

    # ------------------------------------------------------------------ #
    # Validacao de compassos
    # ------------------------------------------------------------------ #
    def _validar_compassos(self, eventos):
        """Confere que cada compasso (trecho entre barras) respeita a formula."""
        numerador, denominador = self.compasso
        capacidade = numerador / denominador
        acumulado = 0.0
        linha_inicio = None

        for evento in eventos:
            if isinstance(evento, CifraParser.EventoBarraContext):
                self._conferir_compasso(acumulado, capacidade, evento.start.line, fechado=True)
                acumulado = 0.0
                linha_inicio = None
            else:
                acumulado += linha_tempo.duracao_evento(evento)
                if linha_inicio is None:
                    linha_inicio = evento.start.line

        # Trecho final que nao foi fechado por uma barra.
        if acumulado > 0 and linha_inicio is not None:
            self._conferir_compasso(acumulado, capacidade, linha_inicio, fechado=False)

    def _conferir_compasso(self, acumulado, capacidade, linha, fechado):
        epsilon = 1e-9
        if acumulado > capacidade + epsilon:
            self._erro(linha, "compasso excede a capacidade da formula {}/{} ({:.3f} > {:.3f})".format(
                self.compasso[0], self.compasso[1], acumulado, capacidade))
        elif fechado and acumulado < capacidade - epsilon:
            self._aviso(linha, "compasso incompleto ({:.3f} de {:.3f})".format(acumulado, capacidade))

    # ------------------------------------------------------------------ #
    # Registro de diagnosticos
    # ------------------------------------------------------------------ #
    def _erro(self, linha, mensagem):
        self.erros.append(Diagnostico(linha, mensagem, "erro"))

    def _aviso(self, linha, mensagem):
        self.avisos.append(Diagnostico(linha, mensagem, "aviso"))
