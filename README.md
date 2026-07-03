# 🎵 Cifra — uma linguagem para compor melodias

**Cifra** é uma pequena linguagem *declarativa* para escrever melodias em solfejo
(dó, ré, mi…) e transformá-las em **áudio**. Em vez de mexer com um editor de
partitura ou com uma DAW, você escreve a música como texto — notas, frases
reutilizáveis, repetições, andamento e instrumento — e o compilador gera um
programa **Python** que sintetiza as ondas sonoras e grava um arquivo **`.wav`**
pronto para tocar.

É o **Trabalho 6** da disciplina de **Construção de Compiladores** (DC/UFSCar):
uma linguagem própria, com análise léxica/sintática (via **ANTLR 4**), análise
semântica e geração de código.

## Integrantes do grupo

- Lucas de Oliveira Rodrigues Alves — RA: 811943

## 🎬 Vídeo demonstrativo

> _(Adicione aqui o link do vídeo curto apresentando a linguagem.)_

---

## Por que Cifra?

- **Simples e legível**: a música é texto em solfejo, fácil de versionar e editar.
- **Reutilização**: agrupe trechos em `frase` e repita com `repita`.
- **Verificação musical**: o compilador avisa se um compasso "estourou", se uma
  nota está fora do tom, se um instrumento não existe, etc.
- **Saída audível**: gera um `.wav` — não precisa de player MIDI nem *soundfont*.

Exemplo completo (`exemplos/estrela.cifra`, "Brilha, Brilha, Estrelinha"):

```
tempo 120
instrumento piano
tom do maior
compasso 4/4

frase verso {
  do4:4 do4:4 sol4:4 sol4:4 |
  la4:4 la4:4 sol4:2 |
  fa4:4 fa4:4 mi4:4 mi4:4 |
  re4:4 re4:4 do4:2 |
}

frase ponte {
  sol4:4 sol4:4 fa4:4 fa4:4 |
  mi4:4 mi4:4 re4:2 |
}

musica {
  toca verso
  repita 2 {
    toca ponte
  }
  toca verso
}
```

---

## Requisitos

| Ferramenta | Versão | Para quê |
|------------|--------|----------|
| Python | 3.8+ | executar o compilador |
| `antlr4-python3-runtime` | 4.13.2 | runtime do parser (via `pip`) |
| `numpy` | 1.20+ | executar o **código gerado** (síntese do WAV) |
| ANTLR 4 (`.jar`) + Java | 4.13.2 | apenas para **regerar** o parser a partir da gramática |

Instale as dependências Python com:

```bash
pip install -r requirements.txt
```

> O parser já vem **gerado** em `src/cifra/gerado/`, então você **não precisa**
> do ANTLR/Java para usar o compilador — só para modificar a gramática.

---

## Como compilar o compilador (regerar o parser)

Só é necessário se você **alterar a gramática** `gramatica/Cifra.g4`.
É preciso o `.jar` do ANTLR 4.13.2 (baixe em <https://www.antlr.org/download.html>):

```bash
# Ajuste o caminho do jar, se necessario:
export ANTLR_JAR=/usr/local/lib/antlr-4.13.2-complete.jar
bash gerar_parser.sh
```

Isso recria `CifraLexer.py`, `CifraParser.py` e `CifraVisitor.py` em
`src/cifra/gerado/`.

---

## Como usar

A **saída padrão é o áudio `.wav`**. O compilador recebe o arquivo de entrada
`.cifra` e, opcionalmente, o nome do `.wav` de saída (se omitido, usa o nome da
entrada com extensão `.wav`):

```bash
python3 cifra.py exemplos/estrela.cifra                 # gera exemplos/estrela.wav
python3 cifra.py exemplos/estrela.cifra minha_musica.wav
```

Opções:

| Opção | Efeito |
|-------|--------|
| `--python` | além do `.wav`, salva o **script Python** intermediário (mesmo nome, extensão `.py`) |
| `--verificar` | apenas roda as análises (léxica/sintática/semântica) e **não gera** nenhum arquivo |

```bash
python3 cifra.py exemplos/estrela.cifra --python      # gera estrela.wav e estrela.py
python3 cifra.py exemplos/estrela.cifra --verificar   # só valida, não gera nada
```

> A geração do `.wav` usa `numpy` (o compilador escreve o código Python de síntese
> e o executa internamente). Com `--python` você também fica com esse script para
> inspecionar ou rodar à mão: `python3 estrela.py saida.wav`.

Ou rode o script gerado manualmente, escolhendo o nome do `.wav`:

```bash
python3 estrela.py minha_musica.wav
```

Se a entrada tiver erros, o compilador **não gera** o código e imprime os
diagnósticos (com o número da linha):

```
Erros semanticos encontrados:
  Linha 5: compasso excede a capacidade da formula 4/4 (1.250 > 1.000)
```

---

## A linguagem

Um programa Cifra tem três partes, nesta ordem: **configurações**, **frases** e o
bloco **`musica`**.

### Configurações (opcionais)

| Configuração | Exemplo | Significado |
|--------------|---------|-------------|
| `tempo` | `tempo 120` | andamento em BPM (1–400) |
| `instrumento` | `instrumento piano` | timbre usado na síntese |
| `tom` | `tom do maior` | tonalidade; ativa a checagem de notas na escala |
| `compasso` | `compasso 4/4` | fórmula de compasso (capacidade de cada `\|`) |

Instrumentos suportados: `piano`, `orgao`, `flauta`, `violao`, `baixo`, `sino`, `corda` e `bateria` (percussão). O `instrumento` global vale quando a música não usa trilhas.

### Notas, acordes e pausas

- **Nota**: `nome` + `oitava` + `:` + `duração`. Ex.: `do4:4` (dó, 4ª oitava, semínima).
  - Nomes (solfejo): `do re mi fa sol la si`, com acidente opcional `#` (sustenido) ou `b` (bemol): `do#4`, `sib3`.
  - Oitava: `0`–`9` (o dó central é `do4` → 261,6 Hz).
  - Duração (denominador da figura): `1` semibreve, `2` mínima, `4` semínima, `8` colcheia, `16`, `32`.
  - **Ponto de aumento** `.`: aumenta a figura em metade do seu valor (`8.` = colcheia pontuada = 1/8 + 1/16). Vários pontos são aceitos (`4..`).
  - **Ligadura** `~`: soma figuras numa mesma nota, inclusive durações que uma figura só não expressa. `do4:4~8` = semínima ligada a colcheia (3/8); `do4:2~4` atravessa o valor de uma mínima + semínima.
  - **Staccato** `!`: a nota soa curta (metade do valor), **sem** alterar o tempo até a próxima nota (o compasso e as marcas continuam iguais). Ex.: `do4:4!`. Vale para notas, acordes e percussão.
- **Acorde**: várias alturas entre colchetes com uma duração: `[do4 mi4 sol4]:2`.
- **Pausa** (silêncio): `pausa:4`.
- **Percussão** (bateria): peça + duração. Peças: `bumbo`, `caixa`, `chimbal`, `prato`. Ex.: `bumbo:4`.
- **Barra de compasso** `|`: separa compassos (usada na verificação semântica).

### Frases e repetições

```
frase intro {
  do4:4 re4:4 mi4:4 fa4:4 |
}

musica {
  toca intro          // reproduz a frase
  repita 3 {          // repete o bloco 3 vezes
    sol4:8 sol4:8
  }
}
```

### Trilhas (vários instrumentos ao mesmo tempo)

Por padrão, a música toca com o instrumento global. Para usar **mais de um
instrumento simultaneamente**, o bloco `musica` pode conter várias `trilha`s —
cada uma com seu instrumento, um **volume opcional** (0–100) e sua sequência de
comandos. As trilhas tocam em paralelo (os sinais são mixados):

```
musica {
  trilha flauta {
    do5:4 re5:4 mi5:4 sol5:4 |
  }
  trilha baixo volume 80 {
    do3:2 sol3:2 |
  }
}
```

Instrumentos: `piano, orgao, flauta, violao, baixo, sino, corda` e `bateria`
(percussão). Dentro de uma trilha valem os mesmos comandos (notas, acordes,
pausas, percussão, `toca`, `repita`). Como cada trilha é uma linha sequencial,
para uma bateria completa use **duas trilhas** `bateria` (uma para o chimbal e
outra para bumbo/caixa, tocando juntas).

Veja `exemplos/duas_trilhas.cifra` (duas trilhas) e `exemplos/banda.cifra` (banda
completa: guitarra, baixo, piano e bateria com volumes).

### Marcas de tempo (sincronizar entradas)

Todas as trilhas começam no instante 0. Para coordenar quando cada trilha entra,
use **marcas**: `marca <nome>` registra o instante atual da trilha, e
`espere <nome>` silencia a trilha até chegar naquele instante. Como o instante é
absoluto, uma trilha pode esperar por uma marca deixada em outra trilha (definida
antes, no texto).

```
musica {
  trilha violao {
    do4:4 mi4:4 sol4:4 mi4:4 |
    do4:4 mi4:4 sol4:4 mi4:4 |
    marca entra_piano          // aqui, aos 4 segundos
    do4:2 sol4:2 |
  }
  trilha piano {
    espere entra_piano         // fica em silêncio até os 4 segundos
    do5:4 re5:4 mi5:4 sol5:4 |
  }
}
```

Veja `exemplos/marcas.cifra`. `marca`/`espere` só podem aparecer no nível da
trilha (não dentro de `repita`).

### Comentários

`// comentário de linha` e `/* comentário de bloco */`.

---

## Análise semântica

Além da gramática, o compilador aplica estas verificações (todas com o número da
linha do problema):

1. **Compasso estourado** — a soma das durações entre duas barras `|` não pode
   exceder a capacidade da fórmula de compasso (ex.: 4/4 = 1 semibreve).
2. **Frase não declarada** — `toca X` exige uma `frase X` definida antes.
3. **Frase redeclarada** — não pode haver duas frases com o mesmo nome.
4. **Duração inválida** — o denominador da figura deve ser `1, 2, 4, 8, 16` ou `32`.
5. **Nota fora da tonalidade** — se um `tom` foi declarado, toda nota deve
   pertencer à escala (maior ou menor) correspondente.
6. **Instrumento desconhecido** — o instrumento (global ou de uma `trilha`) deve
   ser um dos suportados.
7. **Valores fora de faixa** — `tempo`, fórmula de `compasso`, contador de
   `repita` e `volume` de trilha (0–100).
8. **Marcas de tempo** — `espere X` exige uma `marca X` definida antes (e que não
   aponte para um instante já passado); `marca X` não pode ser duplicada nem
   aparecer dentro de `repita`.

E ainda **avisos** (não impedem a geração): frases declaradas e nunca usadas, e
compassos incompletos.

---

## Geração de código

O compilador **achata** cada trilha numa lista linear de eventos concretos
(expandindo `toca` e `repita`, convertendo cada nota em frequência e cada figura
em segundos) e escreve um script Python autossuficiente. Esse script contém o
motor de síntese (formas de onda por instrumento, envelope de amplitude, mixagem
das trilhas e gravação do WAV com `numpy`) e as trilhas de eventos; ao ser
executado, sintetiza cada trilha, soma-as e grava o arquivo de áudio.

---

## Exemplos incluídos

| Arquivo | O que demonstra |
|---------|-----------------|
| `exemplos/escala.cifra` | escala de dó maior (flauta) |
| `exemplos/estrela.cifra` | "Brilha, Brilha, Estrelinha" com frases e `repita` |
| `exemplos/acordes.cifra` | progressão de acordes (órgão) |
| `exemplos/duas_trilhas.cifra` | duas trilhas simultâneas (flauta + baixo) |
| `exemplos/marcas.cifra` | marcas de tempo (piano entra depois do violão) |
| `exemplos/banda.cifra` | banda completa (guitarra, baixo, piano e bateria) com volume |
| `exemplos/inverno.cifra` | "Inverno" (Vivaldi, domínio público) — cordas entrando com marcas de tempo |

## Casos de teste

```bash
bash testes/rodar_testes.sh
```

Isso compila todos os `exemplos/` e `testes/validos/` (devem passar) e todos os
`testes/erros/` (devem ser rejeitados, um caso por verificação semântica, mais um
erro sintático).

---

## Estrutura do projeto

```
cifra/
├── README.md                 # esta documentação
├── requirements.txt          # dependências Python
├── gerar_parser.sh           # regera o parser a partir da gramática (precisa do ANTLR)
├── cifra.py                  # lançador do compilador
├── gramatica/
│   └── Cifra.g4              # gramática (léxico + sintaxe), documentada
├── src/cifra/
│   ├── main.py              # orquestra as fases e trata a linha de comando
│   ├── musica.py            # domínio musical: notas→frequência, escalas, durações
│   ├── linha_tempo.py       # cálculo de durações (usado pelas marcas de tempo)
│   ├── analisador_semantico.py  # verificações semânticas
│   ├── gerador_codigo.py    # geração do script Python de síntese
│   └── gerado/              # lexer/parser/visitor gerados pelo ANTLR
├── exemplos/                 # programas de exemplo prontos
└── testes/
    ├── validos/             # entradas que devem compilar
    ├── erros/               # entradas que devem ser rejeitadas
    └── rodar_testes.sh      # executa toda a bateria de testes
```

---

## Como funciona (resumo do pipeline)

1. **Léxico + sintaxe**: o ANTLR gera o lexer/parser a partir de `Cifra.g4`; o
   `main.py` constrói a árvore sintática e coleta eventuais erros sintáticos.
2. **Semântica**: o `AnalisadorSemantico` percorre a árvore, coletando as
   configurações e validando frases, durações, tonalidade, compassos e faixas.
3. **Geração**: se não houver erros, o `GeradorCodigo` expande a melodia e emite
   um `.py` que sintetiza e grava o `.wav`.
