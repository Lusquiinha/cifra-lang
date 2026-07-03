#!/bin/bash
# Gera o lexer, o parser e o visitor em Python a partir da gramatica Cifra.g4.
# Requer o ANTLR 4.13.2 (arquivo .jar) instalado. Ajuste ANTLR_JAR se necessario.
set -e

RAIZ="$(cd "$(dirname "$0")" && pwd)"
ANTLR_JAR="${ANTLR_JAR:-/usr/local/lib/antlr-4.13.2-complete.jar}"
DESTINO="$RAIZ/src/cifra/gerado"

if [ ! -f "$ANTLR_JAR" ]; then
    echo "ANTLR nao encontrado em: $ANTLR_JAR"
    echo "Baixe em https://www.antlr.org/download.html e/ou defina a variavel ANTLR_JAR."
    exit 1
fi

mkdir -p "$DESTINO"
java -jar "$ANTLR_JAR" -Dlanguage=Python3 -visitor -no-listener \
    -o "$DESTINO" "$RAIZ/gramatica/Cifra.g4"
touch "$DESTINO/__init__.py"

echo "Parser gerado em: $DESTINO"
