"""Geracao de codigo da linguagem Cifra.

Percorre a arvore sintatica e produz um programa Python autossuficiente que,
ao ser executado, sintetiza a melodia e grava um arquivo de audio WAV usando
numpy. A traducao acontece em duas etapas:

  1. A melodia e "achatada" numa lista linear de eventos concretos
     (nota / acorde / pausa) ja com frequencia em Hz e duracao em segundos.
     Nesse momento os comandos "toca" (frases) e "repita" sao expandidos.
  2. Essa lista e escrita dentro de um script Python que contem tambem o
     motor de sintese (formas de onda por instrumento, envelope e escrita WAV).

Assim, o "codigo gerado" e um .py legivel e independente do compilador.
"""

from cifra.gerado.CifraParser import CifraParser
from cifra import musica
from cifra import linha_tempo
from cifra import linha_tempo


# Motor de sintese embutido no script gerado. Fica separado do restante para
# facilitar a leitura; os marcadores {instrumento} e {eventos} sao preenchidos
# na hora da geracao.
MOTOR = '''import sys
import wave
import numpy as np

# Taxa de amostragem do audio (amostras por segundo).
TAXA = 44100

# Descricao de cada instrumento: lista de harmonicos (multiplo da frequencia
# fundamental, amplitude relativa), tipo de envelope e taxa de decaimento.
# "percussivo" decai sozinho (piano, violao...); "sustentado" se mantem (orgao...).
TIMBRES = {
    "piano":  ([(1, 1.0), (2, 0.6), (3, 0.3), (4, 0.15)], "percussivo", 3.0),
    "orgao":  ([(1, 1.0), (2, 0.5), (4, 0.5), (8, 0.2)], "sustentado", 0.0),
    "flauta": ([(1, 1.0), (2, 0.2)], "sustentado", 0.0),
    "violao": ([(1, 1.0), (2, 0.5), (3, 0.35), (5, 0.2)], "percussivo", 4.5),
    "baixo":  ([(1, 1.0), (2, 0.3)], "percussivo", 2.0),
    "sino":   ([(1, 1.0), (2.76, 0.6), (5.40, 0.3), (8.93, 0.15)], "percussivo", 2.5),
    "corda":  ([(1, 1.0), (2, 0.6), (3, 0.4), (4, 0.3)], "sustentado", 0.0),
    "bateria": ([(1, 1.0)], "percussivo", 6.0),
}


def envelope(n, tipo, taxa_decaimento):
    """Constroi a curva de amplitude ao longo das n amostras da nota."""
    t = np.linspace(0, n / TAXA, n, endpoint=False)
    env = np.ones(n)
    ataque = min(int(0.01 * TAXA), n)
    if ataque > 0:
        env[:ataque] = np.linspace(0, 1, ataque)
    if tipo == "percussivo":
        env = env * np.exp(-taxa_decaimento * t)
    else:
        relaxamento = min(int(0.03 * TAXA), n)
        if relaxamento > 0:
            env[-relaxamento:] = env[-relaxamento:] * np.linspace(1, 0, relaxamento)
    return env


def sintetizar(freq, dur, instrumento):
    """Gera a forma de onda de uma nota (frequencia freq, duracao dur em s)."""
    n = max(1, int(TAXA * dur))
    t = np.linspace(0, dur, n, endpoint=False)
    harmonicos, tipo, decaimento = TIMBRES.get(instrumento, TIMBRES["piano"])
    onda = np.zeros(n)
    for multiplo, amplitude in harmonicos:
        onda += amplitude * np.sin(2 * np.pi * freq * multiplo * t)
    total = sum(amplitude for _, amplitude in harmonicos)
    onda = onda / total
    return onda * envelope(n, tipo, decaimento)


def silencio(dur):
    """Gera um trecho de silencio com a duracao pedida (em segundos)."""
    return np.zeros(max(1, int(TAXA * dur)))


def percussao(peca, dur):
    """Sintetiza uma batida de percussao a partir de ruido e envelopes curtos."""
    n = max(1, int(TAXA * dur))
    t = np.linspace(0, dur, n, endpoint=False)
    ruido = np.random.uniform(-1.0, 1.0, n)
    if peca == "bumbo":
        # Grave com queda rapida de altura (o "soco" do bumbo).
        freq = 110.0 * np.exp(-28.0 * t) + 45.0
        onda = np.sin(np.cumsum(2 * np.pi * freq / TAXA))
        return onda * np.exp(-11.0 * t)
    if peca == "caixa":
        # Ruido com um pouco de tom, decaimento medio.
        onda = 0.7 * ruido + 0.3 * np.sin(2 * np.pi * 180.0 * t)
        return onda * np.exp(-28.0 * t)
    if peca == "chimbal":
        # Ruido agudo bem curto.
        return 0.5 * ruido * np.exp(-75.0 * t)
    if peca == "prato":
        # Ruido com cauda longa.
        return 0.5 * ruido * np.exp(-7.0 * t)
    return np.zeros(n)


def render_trilha(eventos, instrumento):
    """Concatena os eventos de uma trilha (sequencial) numa unica onda."""
    partes = []
    for evento in eventos:
        if evento[0] == "nota":
            partes.append(sintetizar(evento[1], evento[2], instrumento))
        elif evento[0] == "acorde":
            comprimento = max(1, int(TAXA * evento[2]))
            soma = np.zeros(comprimento)
            for freq in evento[1]:
                soma += sintetizar(freq, evento[2], instrumento)
            if evento[1]:
                soma /= len(evento[1])
            partes.append(soma)
        elif evento[0] == "pausa":
            partes.append(silencio(evento[1]))
        elif evento[0] == "perc":
            partes.append(percussao(evento[1], evento[2]))
    if not partes:
        return np.zeros(0)
    return np.concatenate(partes)


def mixar(trilhas):
    """Sobrepoe (soma) as trilhas, alinhadas no inicio, aplicando o volume de cada uma."""
    sinais = []
    for instrumento, volume, eventos in trilhas:
        sinal = render_trilha(eventos, instrumento) * volume
        if sinal.size > 0:
            sinais.append(sinal)
    if not sinais:
        return np.zeros(0)
    comprimento = max(s.size for s in sinais)
    total = np.zeros(comprimento)
    for sinal in sinais:
        total[:sinal.size] += sinal
    return total


def salvar_wav(sinal, caminho):
    """Normaliza o sinal e grava um WAV mono de 16 bits."""
    if sinal.size > 0:
        pico = np.max(np.abs(sinal))
        if pico > 0:
            sinal = sinal / pico * 0.9
    amostras = (sinal * 32767).astype(np.int16)
    with wave.open(caminho, "w") as arquivo:
        arquivo.setnchannels(1)
        arquivo.setsampwidth(2)
        arquivo.setframerate(TAXA)
        arquivo.writeframes(amostras.tobytes())


# Trilhas definidas pelo programa Cifra de origem: cada uma tem um instrumento
# e uma lista de eventos. Trilhas diferentes tocam simultaneamente (mixadas).
TRILHAS = [
{trilhas}
]

if __name__ == "__main__":
    saida = sys.argv[1] if len(sys.argv) > 1 else "saida.wav"
    salvar_wav(mixar(TRILHAS), saida)
    print("Arquivo de audio gerado:", saida)
'''


class GeradorCodigo:
    """Traduz a arvore de um programa Cifra num script Python de sintese."""

    def __init__(self, tempo, instrumento, frases):
        self.tempo = tempo
        self.instrumento = instrumento
        self.frases = frases  # nome -> contexto de declaracao (para expandir "toca")
        self.eventos = []     # lista achatada de eventos da trilha corrente
        self.trilhas = []     # lista de (instrumento, eventos) prontas para o script
        self.cursor = 0.0     # instante atual da trilha corrente, em segundos
        self.marcas = {}      # nome da marca -> instante em segundos (global)

    def gerar(self, programa):
        """Produz o texto completo do script Python gerado."""
        musica = programa.musica()
        trilhas_ctx = musica.trilha()

        # Instantes das marcas (resolvidos globalmente) convertidos para segundos.
        # Uma semibreve dura 4 batidas; cada batida dura 60/tempo segundos.
        segundos_por_semibreve = 4.0 * 60.0 / self.tempo
        self.marcas = {
            nome: fracao * segundos_por_semibreve
            for nome, fracao in linha_tempo.resolver_marcas(musica, self.frases).items()
        }
        if trilhas_ctx:
            # Uma trilha por instrumento; todas tocam simultaneamente.
            for trilha in trilhas_ctx:
                self.eventos = []
                self.cursor = 0.0
                self._processar_comandos(trilha.comando())
                volume = int(trilha.INT().getText()) / 100.0 if trilha.INT() is not None else 1.0
                self.trilhas.append((trilha.IDENT().getText(), volume, self.eventos))
        else:
            # Sem trilhas: uma unica trilha com o instrumento global.
            self.eventos = []
            self.cursor = 0.0
            self._processar_comandos(musica.comando())
            self.trilhas.append((self.instrumento, 1.0, self.eventos))
        return self._montar_script()

    # ------------------------------------------------------------------ #
    # Achatamento da melodia
    # ------------------------------------------------------------------ #
    def _processar_comandos(self, comandos):
        for comando in comandos:
            if isinstance(comando, CifraParser.ComandoEventoContext):
                self._processar_evento(comando.evento())
            elif isinstance(comando, CifraParser.ComandoTocaContext):
                nome = comando.IDENT().getText()
                declaracao = self.frases.get(nome)
                if declaracao is not None:
                    for evento in declaracao.evento():
                        self._processar_evento(evento)
            elif isinstance(comando, CifraParser.ComandoRepitaContext):
                vezes = int(comando.INT().getText())
                for _ in range(vezes):
                    self._processar_comandos(comando.comando())
            elif isinstance(comando, CifraParser.ComandoMarcaContext):
                # As marcas ja foram resolvidas em self.marcas; nada a fazer aqui.
                pass
            elif isinstance(comando, CifraParser.ComandoEspereContext):
                # Insere silencio ate alcancar o instante (global) da marca.
                alvo = self.marcas.get(comando.IDENT().getText(), self.cursor)
                espera = alvo - self.cursor
                if espera > 1e-6:
                    self.eventos.append(("pausa", round(espera, 4)))
                    self.cursor = alvo

    def _segundos(self, duracao):
        """Converte uma duracao (fracao de semibreve) em segundos, dado o tempo.

        Uma semibreve dura 4 batidas; cada batida dura 60/tempo segundos.
        """
        return linha_tempo.fracao_de_duracao(duracao) * (4.0 * 60.0 / self.tempo)

    def _processar_evento(self, evento):
        if isinstance(evento, CifraParser.EventoNotaContext):
            nota = evento.nota()
            freq = musica.altura_para_frequencia(nota.ALTURA().getText())
            self._emitir_sonoro(("nota", round(freq, 3)), self._segundos(nota.duracao()),
                                nota.STAC() is not None)
        elif isinstance(evento, CifraParser.EventoAcordeContext):
            acorde = evento.acorde()
            freqs = [round(musica.altura_para_frequencia(a.getText()), 3) for a in acorde.ALTURA()]
            self._emitir_sonoro(("acorde", freqs), self._segundos(acorde.duracao()),
                                acorde.STAC() is not None)
        elif isinstance(evento, CifraParser.EventoPausaContext):
            dur = self._segundos(evento.pausa().duracao())
            self.eventos.append(("pausa", round(dur, 4)))
            self.cursor += dur
        elif isinstance(evento, CifraParser.EventoPercussaoContext):
            percussao = evento.percussao()
            self._emitir_sonoro(("perc", percussao.PECA().getText()), self._segundos(percussao.duracao()),
                                percussao.STAC() is not None)
        # EventoBarra nao produz som: e apenas um separador de compasso.

    def _emitir_sonoro(self, prefixo, dur, staccato):
        """Emite um evento sonoro (nota/acorde/percussao) de duracao 'dur'.

        Com staccato, a parte soada e encurtada (FATOR_STACCATO) e o restante do
        tempo vira silencio, de modo que o compasso e as marcas nao se alteram.
        """
        soada = dur * musica.FATOR_STACCATO if staccato else dur
        self.eventos.append(prefixo + (round(soada, 4),))
        if staccato and dur - soada > 1e-6:
            self.eventos.append(("pausa", round(dur - soada, 4)))
        self.cursor += dur

    # ------------------------------------------------------------------ #
    # Montagem do script final
    # ------------------------------------------------------------------ #
    def _montar_script(self):
        blocos = []
        for instrumento, volume, eventos in self.trilhas:
            blocos.append(self._formatar_trilha(instrumento, volume, eventos))

        cabecalho = (
            "# -*- coding: utf-8 -*-\n"
            "# Arquivo gerado automaticamente pelo compilador da linguagem Cifra.\n"
            "# Execute com: python3 este_arquivo.py saida.wav\n\n"
        )
        return cabecalho + MOTOR.replace("{trilhas}", "\n".join(blocos))

    def _formatar_trilha(self, instrumento, volume, eventos):
        """Formata uma trilha como ("instrumento", volume, [ eventos... ])."""
        linhas = ['    ("{}", {}, ['.format(instrumento, round(volume, 3))]
        for evento in eventos:
            if evento[0] == "nota":
                linhas.append('        ("nota", {}, {}),'.format(evento[1], evento[2]))
            elif evento[0] == "acorde":
                freqs = ", ".join(str(f) for f in evento[1])
                linhas.append('        ("acorde", [{}], {}),'.format(freqs, evento[2]))
            elif evento[0] == "pausa":
                linhas.append('        ("pausa", {}),'.format(evento[1]))
            elif evento[0] == "perc":
                linhas.append('        ("perc", "{}", {}),'.format(evento[1], evento[2]))
        linhas.append('    ]),')
        return "\n".join(linhas)
