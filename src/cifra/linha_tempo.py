"""Calculo de duracoes na linha do tempo da linguagem Cifra.

Fornece funcoes que medem quanto tempo (em fracoes de semibreve) um evento, uma
frase ou um comando ocupam. E usado tanto pela analise semantica (para resolver
as marcas de tempo e detectar saltos invalidos) quanto pela geracao de codigo
(para converter "espere <marca>" em uma pausa com a duracao correta). Manter esse
calculo num unico lugar garante que as duas fases enxerguem o mesmo tempo.
"""

from cifra.gerado.CifraParser import CifraParser


def fracao_de_figura(figura):
    """Duracao de uma figura em fracao de semibreve, considerando os pontos.

    Cada ponto de aumento soma metade do valor anterior: 8 -> 1/8; 8. -> 3/16;
    8.. -> 7/32. O denominador zero (ex.: :0) e tratado como duracao nula.
    """
    denominador = int(figura.INT().getText())
    if denominador <= 0:
        return 0.0
    valor = 1.0 / denominador
    incremento = valor
    for _ in range(len(figura.PONTO())):
        incremento /= 2.0
        valor += incremento
    return valor


def fracao_de_duracao(duracao):
    """Soma das figuras ligadas por '~' que formam uma duracao."""
    return sum(fracao_de_figura(figura) for figura in duracao.figura())


def duracao_evento(evento):
    """Duracao de um evento em fracao de semibreve (barra = 0)."""
    if isinstance(evento, CifraParser.EventoNotaContext):
        return fracao_de_duracao(evento.nota().duracao())
    if isinstance(evento, CifraParser.EventoAcordeContext):
        return fracao_de_duracao(evento.acorde().duracao())
    if isinstance(evento, CifraParser.EventoPausaContext):
        return fracao_de_duracao(evento.pausa().duracao())
    if isinstance(evento, CifraParser.EventoPercussaoContext):
        return fracao_de_duracao(evento.percussao().duracao())
    return 0.0


def duracao_frase(declaracao):
    """Soma das duracoes dos eventos de uma frase."""
    return sum(duracao_evento(evento) for evento in declaracao.evento())


def duracao_comando(comando, frases):
    """Duracao de um comando, expandindo 'toca' (frases) e 'repita'.

    'marca' e 'espere' nao tem duracao propria (retornam 0); o efeito do
    'espere' na linha do tempo e tratado por quem percorre a trilha.
    """
    if isinstance(comando, CifraParser.ComandoEventoContext):
        return duracao_evento(comando.evento())
    if isinstance(comando, CifraParser.ComandoTocaContext):
        declaracao = frases.get(comando.IDENT().getText())
        return duracao_frase(declaracao) if declaracao is not None else 0.0
    if isinstance(comando, CifraParser.ComandoRepitaContext):
        vezes = int(comando.INT().getText())
        interno = sum(duracao_comando(c, frases) for c in comando.comando())
        return max(vezes, 0) * interno
    return 0.0


def listas_de_comandos(musica_ctx):
    """Retorna a lista de comandos de cada trilha (ou a unica do bloco musica)."""
    trilhas = musica_ctx.trilha()
    if trilhas:
        return [trilha.comando() for trilha in trilhas]
    return [musica_ctx.comando()]


def resolver_marcas(musica_ctx, frases):
    """Calcula o instante (em fracao de semibreve) de cada marca de tempo.

    Como as trilhas comecam todas no instante 0, uma marca guarda um instante
    absoluto. A resolucao e feita por ponto-fixo: repete-se a varredura das
    trilhas ate que nenhum instante novo apareca, de modo que uma trilha possa
    esperar por uma marca definida em qualquer outra trilha, independentemente
    da ordem em que aparecem no texto.
    """
    listas = listas_de_comandos(musica_ctx)
    tempos = {}
    for _ in range(len(listas) + 1):
        mudou = False
        for comandos in listas:
            cursor = 0.0
            for comando in comandos:
                if isinstance(comando, CifraParser.ComandoMarcaContext):
                    nome = comando.IDENT().getText()
                    if nome not in tempos:
                        tempos[nome] = cursor
                        mudou = True
                elif isinstance(comando, CifraParser.ComandoEspereContext):
                    nome = comando.IDENT().getText()
                    if nome in tempos and tempos[nome] > cursor:
                        cursor = tempos[nome]
                else:
                    cursor += duracao_comando(comando, frases)
        if not mudou:
            break
    return tempos
