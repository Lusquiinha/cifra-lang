"""Conhecimento de dominio musical usado pela analise semantica e pela geracao de codigo.

Concentra aqui tudo que traduz os conceitos da linguagem Cifra para numeros:
conversao de notas em altura MIDI e frequencia, calculo de duracoes em segundos,
escalas das tonalidades e a lista de instrumentos suportados. Manter essa logica
isolada evita duplicacao entre o analisador semantico e o gerador de codigo.
"""

# Semitom (dentro de uma oitava) de cada nome de nota, tomando 'do' como 0.
SEMITONS = {
    "do": 0,
    "re": 2,
    "mi": 4,
    "fa": 5,
    "sol": 7,
    "la": 9,
    "si": 11,
}

# Denominadores de figura aceitos: 1=semibreve, 2=minima, 4=seminima, 8=colcheia...
DURACOES_VALIDAS = {1, 2, 4, 8, 16, 32}

# Intervalos (em semitons) das escalas a partir da tonica.
ESCALA_MAIOR = [0, 2, 4, 5, 7, 9, 11]
ESCALA_MENOR = [0, 2, 3, 5, 7, 8, 10]

# Instrumentos reconhecidos. O nome escolhido determina o timbre na sintese WAV.
# "bateria" e uma trilha de percussao (usa as pecas bumbo/caixa/chimbal/prato).
INSTRUMENTOS_VALIDOS = {
    "piano",
    "orgao",
    "flauta",
    "violao",
    "baixo",
    "sino",
    "corda",
    "bateria",
}

# Volume de uma trilha (percentual): 0 = mudo, 100 = cheio.
VOLUME_MINIMO = 0
VOLUME_MAXIMO = 100

# Fracao da duracao que uma nota staccato realmente soa (o resto vira silencio).
FATOR_STACCATO = 0.5

# Faixa aceita para o andamento (BPM).
TEMPO_MINIMO = 1
TEMPO_MAXIMO = 400


def separar_altura(texto):
    """Divide o texto de uma altura (ex.: 'do#4') em (nome, acidente, oitava).

    'acidente' e '' (sem acidente), '#' (sustenido) ou 'b' (bemol).
    """
    oitava = int(texto[-1])
    corpo = texto[:-1]
    acidente = ""
    if corpo and corpo[-1] in ("#", "b"):
        acidente = corpo[-1]
        corpo = corpo[:-1]
    return corpo, acidente, oitava


def deslocamento_acidente(acidente):
    """Converte o acidente em deslocamento de semitons."""
    if acidente == "#":
        return 1
    if acidente == "b":
        return -1
    return 0


def altura_para_midi(texto):
    """Converte o texto de uma altura na sua nota MIDI (do4 -> 60)."""
    nome, acidente, oitava = separar_altura(texto)
    return 12 * (oitava + 1) + SEMITONS[nome] + deslocamento_acidente(acidente)


def midi_para_frequencia(nota_midi):
    """Converte uma nota MIDI na frequencia em Hz (temperamento igual, la4 = 440 Hz)."""
    return 440.0 * (2.0 ** ((nota_midi - 69) / 12.0))


def altura_para_frequencia(texto):
    """Atalho: texto de altura -> frequencia em Hz."""
    return midi_para_frequencia(altura_para_midi(texto))


def fracao_da_duracao(denominador):
    """Fracao de uma semibreve que a figura ocupa (denominador 4 -> 1/4)."""
    return 1.0 / denominador


def duracao_em_segundos(denominador, tempo_bpm):
    """Duracao real de uma figura, em segundos, para um dado andamento.

    A seminima (denominador 4) equivale a uma batida; portanto ela dura
    60/tempo segundos. As demais figuras sao proporcionais.
    """
    batidas = 4.0 / denominador
    return batidas * (60.0 / tempo_bpm)


def classe_para_semitom(texto_classe):
    """Converte uma classe de nota (ex.: 'fa#') no seu semitom 0-11."""
    acidente = ""
    corpo = texto_classe
    if corpo[-1] in ("#", "b"):
        acidente = corpo[-1]
        corpo = corpo[:-1]
    return (SEMITONS[corpo] + deslocamento_acidente(acidente)) % 12


def notas_da_tonalidade(tonica_classe, modo):
    """Retorna o conjunto de semitons (0-11) que pertencem a uma tonalidade."""
    escala = ESCALA_MAIOR if modo == "maior" else ESCALA_MENOR
    base = classe_para_semitom(tonica_classe)
    return {(base + intervalo) % 12 for intervalo in escala}


def altura_esta_na_tonalidade(texto_altura, tonica_classe, modo):
    """Indica se uma altura pertence a escala da tonalidade informada."""
    return (altura_para_midi(texto_altura) % 12) in notas_da_tonalidade(tonica_classe, modo)
