#!/usr/bin/env python3
"""Lancador do compilador Cifra.

Ajusta o caminho de importacao para a pasta 'src' e delega para cifra.main.
Assim o compilador pode ser executado diretamente da raiz do projeto:

    python3 cifra.py exemplos/escala.cifra saida.py --executar
"""

import os
import sys

RAIZ = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(RAIZ, "src"))

from cifra.main import main

if __name__ == "__main__":
    sys.exit(main())
