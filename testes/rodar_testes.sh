#!/bin/bash
# Executa todos os casos de teste da linguagem Cifra e resume o resultado.
#   - exemplos/ e testes/validos/ devem compilar (codigo de saida 0);
#   - testes/erros/  devem ser rejeitados (codigo de saida != 0).
#
# Uso: bash testes/rodar_testes.sh

RAIZ="$(cd "$(dirname "$0")/.." && pwd)"
TMP="$(mktemp -d)"
PASSOU=0
FALHOU=0

echo "==== Casos que DEVEM compilar ===="
for f in "$RAIZ"/exemplos/*.cifra "$RAIZ"/testes/validos/*.cifra; do
    python3 "$RAIZ/cifra.py" "$f" --verificar > "$TMP/log" 2>&1
    if [ $? -eq 0 ]; then
        echo "  OK    $(basename "$f")"
        PASSOU=$((PASSOU + 1))
    else
        echo "  FALHA $(basename "$f") (esperava compilar)"
        FALHOU=$((FALHOU + 1))
    fi
done

echo "==== Casos que DEVEM ser rejeitados ===="
for f in "$RAIZ"/testes/erros/*.cifra; do
    python3 "$RAIZ/cifra.py" "$f" --verificar > "$TMP/log" 2>&1
    if [ $? -ne 0 ]; then
        echo "  OK    $(basename "$f")  ->  $(grep -m1 -E 'Linha|erro' "$TMP/log" | sed 's/^ *//')"
        PASSOU=$((PASSOU + 1))
    else
        echo "  FALHA $(basename "$f") (esperava erro)"
        FALHOU=$((FALHOU + 1))
    fi
done

rm -rf "$TMP"
echo "======================================"
echo "Passou: $PASSOU | Falhou: $FALHOU"
[ "$FALHOU" -eq 0 ]
