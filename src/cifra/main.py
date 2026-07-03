"""Ponto de entrada do compilador da linguagem Cifra.

Fluxo: le o programa de entrada, executa a analise lexica/sintatica (via ANTLR),
depois a analise semantica e, se nao houver erros, gera o codigo. A saida padrao
e o arquivo de audio .wav. Uso:

    python3 cifra.py <entrada.cifra> [saida.wav] [--python] [--verificar]

Opcoes:
    --python     alem do .wav, salva tambem o script Python intermediario;
    --verificar  apenas analisa a entrada (nao gera .wav nem .py).

A geracao do .wav requer numpy instalado (usado pelo codigo gerado).
"""

import os
import subprocess
import sys
import tempfile

from antlr4 import CommonTokenStream, FileStream
from antlr4.error.ErrorListener import ErrorListener

from cifra.gerado.CifraLexer import CifraLexer
from cifra.gerado.CifraParser import CifraParser
from cifra.analisador_semantico import AnalisadorSemantico
from cifra.gerador_codigo import GeradorCodigo


class ColetorDeErros(ErrorListener):
    """Coleta os erros lexicos/sintaticos em vez de imprimi-los no console."""

    def __init__(self):
        super().__init__()
        self.erros = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.erros.append("Linha {}: erro sintatico: {}".format(line, msg))


def compilar(caminho_entrada):
    """Analisa e gera o codigo de um arquivo Cifra.

    Retorna o texto do script Python gerado, ou None se houver erros (que sao
    impressos junto com eventuais avisos).
    """
    entrada = FileStream(caminho_entrada, encoding="utf-8")

    coletor = ColetorDeErros()
    lexer = CifraLexer(entrada)
    lexer.removeErrorListeners()
    lexer.addErrorListener(coletor)

    tokens = CommonTokenStream(lexer)
    parser = CifraParser(tokens)
    parser.removeErrorListeners()
    parser.addErrorListener(coletor)

    arvore = parser.programa()

    # Analise lexica/sintatica: se houve qualquer erro, nao prossegue.
    if coletor.erros:
        print("Erros lexicos/sintaticos encontrados:")
        for erro in coletor.erros:
            print("  " + erro)
        return None

    # Analise semantica.
    analisador = AnalisadorSemantico()
    erros, avisos = analisador.analisar(arvore)

    for aviso in avisos:
        print("Aviso: {}".format(aviso))

    if erros:
        print("Erros semanticos encontrados:")
        for erro in erros:
            print("  {}".format(erro))
        return None

    # Geracao de codigo.
    gerador = GeradorCodigo(analisador.tempo, analisador.instrumento, analisador.frases)
    return gerador.gerar(arvore)


def gerar_wav(codigo, caminho_wav):
    """Executa o script gerado num arquivo temporario para produzir o .wav."""
    temporario = tempfile.NamedTemporaryFile("w", suffix=".py", delete=False, encoding="utf-8")
    try:
        temporario.write(codigo)
        temporario.close()
        subprocess.run([sys.executable, temporario.name, caminho_wav], check=True)
    finally:
        os.unlink(temporario.name)


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    gerar_python = "--python" in argv
    apenas_verificar = "--verificar" in argv
    argumentos = [a for a in argv if not a.startswith("--")]

    if len(argumentos) < 1:
        print("Uso: python3 cifra.py <entrada.cifra> [saida.wav] [--python] [--verificar]")
        return 1

    caminho_entrada = argumentos[0]

    codigo = compilar(caminho_entrada)
    if codigo is None:
        return 1

    # Modo verificacao: apenas confirma que a analise passou, sem gerar arquivos.
    if apenas_verificar:
        print("Analise concluida: nenhum erro encontrado.")
        return 0

    # A saida padrao e o .wav; se nao for informada, usa o nome da entrada.
    if len(argumentos) >= 2:
        caminho_wav = argumentos[1]
    else:
        caminho_wav = os.path.splitext(caminho_entrada)[0] + ".wav"

    # O script Python so e salvo quando a flag --python e usada.
    if gerar_python:
        caminho_py = os.path.splitext(caminho_wav)[0] + ".py"
        with open(caminho_py, "w", encoding="utf-8") as arquivo:
            arquivo.write(codigo)
        print("Script Python gerado em: {}".format(caminho_py))

    gerar_wav(codigo, caminho_wav)
    print("Arquivo de audio gerado em: {}".format(caminho_wav))
    return 0


if __name__ == "__main__":
    sys.exit(main())
