# Guia da linguagem Cifra

Este é o guia completo da linguagem **Cifra**, explicado parte por parte. Se você
só quer uma visão geral rápida, o [README](../README.md) basta. Aqui detalhamos
cada construção, com exemplos pequenos e o que cada uma significa na música e no
áudio gerado.

## Sumário

1. [Visão geral e estrutura de um programa](#1-visão-geral-e-estrutura-de-um-programa)
2. [Configurações](#2-configurações)
3. [Notas](#3-notas)
4. [Durações: figuras, pontos, ligaduras e staccato](#4-durações-figuras-pontos-ligaduras-e-staccato)
5. [Acordes](#5-acordes)
6. [Pausas](#6-pausas)
7. [Percussão (bateria)](#7-percussão-bateria)
8. [Barras de compasso](#8-barras-de-compasso)
9. [Frases e reutilização (`toca`)](#9-frases-e-reutilização-toca)
10. [Repetição (`repita`)](#10-repetição-repita)
11. [Trilhas e volume](#11-trilhas-e-volume)
12. [Marcas de tempo (`marca` / `espere`)](#12-marcas-de-tempo-marca--espere)
13. [Comentários](#13-comentários)
14. [O que a análise semântica verifica](#14-o-que-a-análise-semântica-verifica)
15. [Como o áudio é gerado](#15-como-o-áudio-é-gerado)
16. [Referência rápida](#16-referência-rápida)
17. [Exemplo completo, comentado](#17-exemplo-completo-comentado)

---

## 1. Visão geral e estrutura de um programa

Um programa Cifra descreve uma melodia como texto e é compilado para um arquivo
de áudio `.wav`. O programa tem **três partes, sempre nesta ordem**:

```
1) configurações   (tempo, instrumento, tom, compasso)  — opcionais
2) frases          (blocos de notas reutilizáveis)       — opcionais
3) bloco musica     { ... }                              — obrigatório
```

Exemplo mínimo:

```
tempo 120
compasso 4/4

musica {
  do4:4 re4:4 mi4:4 fa4:4 |
}
```

O bloco `musica` é o que realmente toca. Tudo que vem antes dele apenas configura
ou define material para ser usado dentro dele.

Para compilar:

```bash
python3 cifra.py meu_programa.cifra          # gera meu_programa.wav
python3 cifra.py meu_programa.cifra --python # também salva o script Python gerado
python3 cifra.py meu_programa.cifra --verificar  # só analisa, não gera nada
```

---

## 2. Configurações

Vêm no topo do arquivo, cada uma em sua linha. Todas são **opcionais** — se
omitidas, valem os padrões.

| Configuração | Exemplo | Padrão | O que faz |
|--------------|---------|--------|-----------|
| `tempo` | `tempo 90` | `120` | Andamento em BPM (batidas por minuto). Faixa aceita: 1 a 400. Controla a velocidade da música. |
| `instrumento` | `instrumento flauta` | `piano` | Timbre usado quando a música **não** usa trilhas (ver seção 11). |
| `tom` | `tom re menor` | *(nenhum)* | Tonalidade. Se declarada, **ativa a checagem** de notas na escala (ver seção 14). |
| `compasso` | `compasso 3/4` | `4/4` | Fórmula de compasso. Define a capacidade de cada compasso delimitado por `\|`. |

Detalhes:

- **`tempo`**: quanto maior, mais rápido. Uma semínima (`:4`) dura `60/tempo`
  segundos; a 120 BPM isso é 0,5 s, a 60 BPM é 1 s.
- **`instrumento`**: valores aceitos — `piano`, `orgao`, `flauta`, `violao`,
  `baixo`, `sino`, `corda`, `bateria`. Cada um tem um timbre diferente.
- **`tom`**: a classe da tônica (ex.: `do`, `re`, `fa#`, `sib`) seguida do modo
  (`maior` ou `menor`). Ex.: `tom do maior`, `tom la menor`. Sem essa linha, você
  pode usar qualquer nota livremente (útil para músicas cromáticas).
- **`compasso`**: `numerador/denominador`. O denominador deve ser uma figura
  válida (1, 2, 4, 8, 16, 32) e o numerador deve ser positivo. Em `4/4`, cabe uma
  semibreve por compasso; em `3/4`, cabem três semínimas; e assim por diante.

---

## 3. Notas

A construção mais básica. O formato é:

```
<nome><oitava>:<duração>
```

Exemplo: `do4:4` é a nota dó, na 4ª oitava, com duração de semínima.

**Nome da nota** (solfejo, em português):

```
do  re  mi  fa  sol  la  si
```

**Acidente** (opcional), logo após o nome:

- `#` — sustenido (sobe meio tom): `do#4`, `fa#5`
- `b` — bemol (desce meio tom): `sib3`, `mib4`

**Oitava**: um dígito de `0` a `9`. O dó central é `do4` (equivale ao MIDI 60,
≈ 261,6 Hz). Cada oitava a mais dobra a frequência: `do5` é uma oitava acima de
`do4`. O lá de referência da afinação é `la4` = 440 Hz.

```
do4:4      // dó central, semínima
do#4:8     // dó sustenido, colcheia
sib3:2     // si bemol da 3ª oitava, mínima
la5:16     // lá agudo, semicolcheia
```

> Dica: se você declarar um `tom`, todas as notas precisam pertencer à escala
> daquela tonalidade (ver seção 14). Para usar acidentes fora da escala, não
> declare o `tom`.

---

## 4. Durações: figuras, pontos, ligaduras e staccato

A duração vem depois dos dois-pontos (`:`). A base é a **figura**, indicada pelo
seu denominador:

| Escrita | Figura | Fração da semibreve |
|---------|--------|---------------------|
| `:1`  | semibreve   | 1     |
| `:2`  | mínima      | 1/2   |
| `:4`  | semínima    | 1/4   |
| `:8`  | colcheia    | 1/8   |
| `:16` | semicolcheia| 1/16  |
| `:32` | fusa        | 1/32  |

### Ponto de aumento (`.`)

Um ponto aumenta a figura em **metade** do seu valor. Pode repetir para pontos
adicionais (cada um soma metade do anterior):

```
do4:4.     // semínima pontuada = 1/4 + 1/8 = 3/8
do4:8.     // colcheia pontuada = 1/8 + 1/16 = 3/16 (0,1875)
do4:2..    // mínima duplo-pontuada = 1/2 + 1/4 + 1/8 = 7/8
```

### Ligadura (`~`)

O til **soma figuras** dentro de uma mesma nota, inclusive durações que uma figura
sozinha não expressa:

```
do4:4~8    // semínima ligada a colcheia = 1/4 + 1/8 = 3/8
do4:2~4    // mínima ligada a semínima  = 1/2 + 1/4 = 3/4
do4:1~1    // duas semibreves = uma nota bem longa
```

### Staccato (`!`)

Um `!` no fim faz a nota **soar curta** (metade do valor), **sem** alterar o
tempo até a próxima nota. Ou seja, o compasso e as marcas de tempo continuam
idênticos; muda só a articulação (o som fica "picado").

```
do4:4!     // ocupa o tempo de uma semínima, mas soa por metade dele
```

Você pode combinar tudo: `do4:4.!` (semínima pontuada, staccato),
`do4:2~8` (mínima ligada a colcheia), etc.

---

## 5. Acordes

Várias alturas tocadas **ao mesmo tempo**, com uma única duração. Escreva as
notas entre colchetes:

```
[do4 mi4 sol4]:2       // acorde de dó maior, mínima
[la3 do4 mi4]:4        // acorde de lá menor, semínima
[fa4 la4 do5]:1!       // acorde de fá, semibreve, staccato
```

Aceita ponto, ligadura e staccato na duração, igual às notas.

---

## 6. Pausas

Silêncio com uma duração. Use a palavra `pausa`:

```
pausa:4    // silêncio de uma semínima
pausa:8    // silêncio de uma colcheia
```

Serve para dar respiros na melodia e também para atrasar a entrada de uma trilha
(embora, para sincronizar trilhas, as **marcas de tempo** sejam mais práticas —
ver seção 12).

---

## 7. Percussão (bateria)

A Cifra tem quatro peças de percussão, escritas como uma peça seguida da duração:

| Peça | Som |
|------|-----|
| `bumbo`   | bumbo (grave, o "soco") |
| `caixa`   | caixa (tarola) |
| `chimbal` | chimbal (hi-hat, agudo e curto) |
| `prato`   | prato (com cauda longa) |

```
bumbo:4 caixa:4 bumbo:4 caixa:4 |
chimbal:8 chimbal:8 chimbal:8 chimbal:8 chimbal:8 chimbal:8 chimbal:8 chimbal:8 |
```

As peças usam síntese por ruído (não têm altura), então a checagem de tonalidade
não se aplica a elas. Como cada trilha é uma linha sequencial, uma bateria
"completa" (chimbal tocando junto com bumbo/caixa) é feita com **duas trilhas**
`bateria` ao mesmo tempo (ver seção 11).

---

## 8. Barras de compasso

A barra vertical `|` separa compassos. Ela não produz som — serve para organizar
a música e para o compilador **verificar** se cada compasso tem a duração certa
(ver seção 14):

```
compasso 4/4
musica {
  do4:4 re4:4 mi4:4 fa4:4 |   // 4 semínimas = 4/4, ok
  sol4:2 la4:2 |              // 2 mínimas = 4/4, ok
}
```

Se a soma das durações entre duas barras passar da capacidade do compasso, o
compilador acusa erro; se ficar abaixo, emite um aviso.

---

## 9. Frases e reutilização (`toca`)

Uma **frase** é um trecho musical com nome, definido **antes** do bloco `musica`.
Serve para reaproveitar partes (refrões, riffs) sem reescrever:

```
frase intro {
  do4:4 re4:4 mi4:4 fa4:4 |
}

musica {
  toca intro       // reproduz a frase "intro" aqui
  sol4:1 |
}
```

- Uma frase contém apenas **eventos musicais** (notas, acordes, pausas,
  percussão e barras). Ela não contém `toca`, `repita` nem marcas.
- Use `toca <nome>` dentro do bloco `musica` (ou de uma trilha) para inserir a
  frase naquele ponto.
- Chamar `toca` de uma frase que não existe é um erro; declarar duas frases com o
  mesmo nome também.

---

## 10. Repetição (`repita`)

Repete um bloco de comandos N vezes:

```
musica {
  repita 3 {
    do4:8 do4:8
  }
}
```

- `N` deve ser um inteiro positivo.
- O bloco pode conter eventos, `toca` e até outro `repita` (aninhado).
- **Não** pode conter `marca` nem `espere` (essas só valem no nível da trilha —
  ver seção 12).

---

## 11. Trilhas e volume

Por padrão, o bloco `musica` é uma única linha tocada pelo `instrumento` global.
Para usar **vários instrumentos ao mesmo tempo**, divida em `trilha`s. Todas as
trilhas começam juntas (no instante 0) e são **mixadas** (somadas):

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

- `trilha <instrumento> { ... }` — cada trilha tem seu próprio timbre.
- `volume <0-100>` é **opcional** e ajusta o volume relativo da trilha (útil para
  equilibrar, por exemplo, um baixo forte sob uma melodia suave). Sem ele, o
  volume é 100.
- Dentro de uma trilha valem os mesmos comandos do bloco `musica`: eventos,
  `toca`, `repita`, `marca` e `espere`.
- Ou você usa **trilhas**, ou usa **comandos soltos** no `musica` — não misture os
  dois no mesmo bloco.

---

## 12. Marcas de tempo (`marca` / `espere`)

Servem para **sincronizar** quando cada trilha entra. Como todas as trilhas
partem do instante 0:

- `marca <nome>` registra o instante atual (naquele ponto da trilha).
- `espere <nome>` silencia a trilha até chegar naquele instante.

```
musica {
  trilha violao {
    do4:4 mi4:4 sol4:4 mi4:4 |
    do4:4 mi4:4 sol4:4 mi4:4 |
    marca entra_piano        // aqui, ao fim de 2 compassos
    do4:2 sol4:2 |
  }
  trilha piano {
    espere entra_piano       // fica em silêncio até a marca
    do5:4 re5:4 mi5:4 sol5:4 |
  }
}
```

Detalhes:

- A resolução é **global e independente de ordem**: uma trilha pode esperar por
  uma marca definida em qualquer outra trilha, mesmo que ela apareça depois no
  texto.
- `marca` e `espere` só podem aparecer **no nível da trilha** (não dentro de
  `repita`).
- Esperar por uma marca inexistente, ou por uma que já passou nesta trilha, é
  erro. Definir a mesma marca duas vezes também.

---

## 13. Comentários

```
// comentário de uma linha

/* comentário
   de várias linhas */
```

Comentários são ignorados pelo compilador.

---

## 14. O que a análise semântica verifica

Além do que a gramática garante, o compilador faz estas verificações. Erros
**impedem** a geração do áudio; avisos apenas alertam.

**Erros:**

1. **Compasso estourado** — a soma das durações entre duas barras `|` não pode
   passar da capacidade da fórmula de compasso.
2. **Frase não declarada** — `toca X` exige uma `frase X` definida.
3. **Frase redeclarada** — não pode haver duas frases com o mesmo nome.
4. **Duração inválida** — cada figura deve usar um denominador conhecido
   (1, 2, 4, 8, 16, 32).
5. **Nota fora da tonalidade** — se um `tom` foi declarado, toda nota deve
   pertencer à escala (maior ou menor) correspondente.
6. **Instrumento desconhecido** — o instrumento (global ou de trilha) deve ser um
   dos suportados.
7. **Valores fora de faixa** — `tempo` (1–400), fórmula de `compasso`, contador de
   `repita` (positivo) e `volume` de trilha (0–100).
8. **Marcas de tempo** — `espere X` exige uma `marca X` que exista e não aponte
   para um instante já passado; `marca X` não pode ser duplicada nem aparecer
   dentro de `repita`.

**Avisos:**

- Frase declarada e nunca usada.
- Compasso incompleto (soma menor que a capacidade).

Cada verificação tem um caso de teste correspondente em `testes/erros/`. Rode
`bash testes/rodar_testes.sh` para ver todas em ação.

---

## 15. Como o áudio é gerado

Entender isso ajuda a prever o resultado:

1. **Achatamento** — o compilador expande `toca` (insere as frases) e `repita`
   (repete os blocos), transformando cada trilha numa lista linear de eventos.
2. **Conversão** — cada nota vira uma **frequência** (em Hz) e cada duração vira
   **segundos**:
   - frequência: a partir da altura (ex.: `la4` = 440 Hz; cada semitom multiplica
     por `2^(1/12)`);
   - duração: `fração_da_figura × 4 × 60 / tempo` segundos (uma semínima a 120 BPM
     = 0,5 s).
3. **Síntese** — o compilador emite um script **Python** (com `numpy`) que gera as
   ondas: cada instrumento tem um conjunto de harmônicos e um envelope de
   amplitude; a percussão usa ruído; as trilhas são somadas (com seus volumes) e o
   resultado é normalizado e gravado como WAV.

Com `--python`, você fica com esse script gerado e pode inspecioná-lo ou rodá-lo à
mão: `python3 saida.py minha_musica.wav`.

---

## 16. Referência rápida

```
// Configurações (opcionais, no topo)
tempo 120
instrumento piano          // piano orgao flauta violao baixo sino corda bateria
tom do maior               // <classe> maior|menor  (ativa checagem de escala)
compasso 4/4

// Frases (opcionais, antes do bloco musica)
frase nome { <eventos> }

// Bloco principal (obrigatório)
musica {
  <comandos>               // ou várias trilhas (não misture)
  trilha piano volume 80 { <comandos> }
}

// Eventos
do4:4                      // nota:  nome[#|b]oitava : duração
[do4 mi4 sol4]:2           // acorde
pausa:4                    // pausa
bumbo:4                    // percussão: bumbo caixa chimbal prato
|                          // barra de compasso

// Durações
:1 :2 :4 :8 :16 :32        // figuras (semibreve ... fusa)
:4.                        // pontuada (+50%)
:4~8                       // ligadura (soma figuras)
:4!                        // staccato (soa curto, tempo mantido)

// Comandos (no musica / na trilha)
toca nome                  // insere uma frase
repita 4 { <comandos> }    // repete N vezes
marca ponto                // registra instante (nível da trilha)
espere ponto               // espera até a marca (nível da trilha)

// Comentários
// linha       /* bloco */
```

---

## 17. Exemplo completo, comentado

O trecho abaixo (baseado em `exemplos/banda.cifra`) mostra quase tudo junto:
configurações, frases, trilhas com volume, percussão e `repita`.

```
tempo 100                     // 100 BPM
tom la menor                  // ativa checagem: só notas de lá menor
compasso 4/4                  // cada compasso = uma semibreve

// --- material reutilizável ---
frase acordes_piano {
  [la3 do4 mi4]:1 |           // Lá menor, uma semibreve
  [fa3 la3 do4]:1 |           // Fá maior
}

frase batida {
  bumbo:4 caixa:4 bumbo:4 caixa:4 |   // 4 semínimas = 4/4
}

// --- o que toca ---
musica {
  trilha piano volume 70 {    // piano, volume 70%
    repita 2 { toca acordes_piano }
  }
  trilha bateria volume 100 { // bateria, volume cheio, tocando junto
    repita 4 { toca batida }
  }
}
```

O que acontece:

- As duas trilhas começam juntas e são mixadas.
- O piano toca a progressão de acordes duas vezes (4 compassos).
- A bateria toca a batida quatro vezes (4 compassos), no mesmo tempo.
- Como `tom la menor` está declarado, se você trocasse alguma nota por uma fora da
  escala (ex.: `sol#4`), o compilador acusaria erro antes de gerar o áudio.

Para ouvir:

```bash
python3 cifra.py exemplo.cifra
```

Pronto — com isso você tem todas as peças da linguagem. Para mais exemplos
completos, veja a pasta [`exemplos/`](../exemplos) e os casos de teste em
[`testes/`](../testes).
