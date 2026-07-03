/*
 * Cifra - Linguagem declarativa para descrever melodias.
 *
 * Esta gramatica combinada (lexer + parser) define a sintaxe da linguagem Cifra.
 * Um programa Cifra tem tres partes, nesta ordem:
 *   1. Configuracoes globais (tempo, instrumento, tom, compasso);
 *   2. Declaracoes de frases reutilizaveis (blocos de notas com nome);
 *   3. Um bloco "musica" com a sequencia principal de comandos.
 *
 * O compilador usa esta gramatica para gerar, via ANTLR, o lexer e o parser
 * em Python, alem de um visitor que e usado pela analise semantica e pela
 * geracao de codigo.
 */
grammar Cifra;

/* ============================ PARSER ============================ */

// Ponto de entrada: configuracoes, depois frases, depois o bloco principal.
programa
    : configuracao* declaracao* musica EOF
    ;

// Cada configuracao ajusta um parametro global da melodia.
// As alternativas sao rotuladas (#) para gerar um metodo de visita por caso.
configuracao
    : 'tempo' INT                        # configTempo         // andamento em BPM
    | 'instrumento' IDENT                # configInstrumento   // timbre usado na sintese
    | 'tom' NOTA_CLASSE MODO             # configTom           // tonalidade (ex.: do maior)
    | 'compasso' INT '/' INT             # configCompasso      // formula de compasso (ex.: 4/4)
    ;

// Uma frase e um trecho musical nomeado, reutilizavel via "toca".
declaracao
    : 'frase' IDENT '{' evento* '}'
    ;

// Bloco principal: e o que efetivamente sera tocado.
// Pode conter uma sequencia simples de comandos (um unico instrumento, o global)
// OU varias trilhas, cada uma com seu instrumento, que tocam simultaneamente.
musica
    : 'musica' '{' (trilha+ | comando*) '}'
    ;

// Trilha paralela: um instrumento proprio, volume opcional (0-100) e comandos.
// Ex.: trilha baixo volume 80 { do3:2 sol2:2 | }
trilha
    : 'trilha' IDENT ('volume' INT)? '{' comando* '}'
    ;

// Comandos que aparecem dentro do bloco "musica".
comando
    : evento                              # comandoEvento   // uma nota/acorde/pausa/barra literal
    | 'toca' IDENT                        # comandoToca     // reproduz uma frase declarada
    | 'repita' INT '{' comando* '}'       # comandoRepita   // repete um bloco N vezes
    | 'marca' IDENT                       # comandoMarca    // registra um instante na linha do tempo
    | 'espere' IDENT                      # comandoEspere   // silencia a trilha ate uma marca
    ;

// Eventos musicais elementares.
evento
    : nota                                # eventoNota
    | acorde                              # eventoAcorde
    | pausa                               # eventoPausa
    | percussao                           # eventoPercussao
    | BARRA                               # eventoBarra     // separador de compasso "|"
    ;

// Nota isolada: altura (nome+oitava), duracao e um "!" opcional (staccato).
// Ex.: do4:4 -> do na 4a oitava, semínima (1/4); do4:4! -> a mesma, tocada curta.
nota
    : ALTURA ':' duracao STAC?
    ;

// Acorde: varias alturas tocadas juntas com a mesma duracao (staccato opcional).
// Ex.: [do4 mi4 sol4]:2
acorde
    : '[' ALTURA+ ']' ':' duracao STAC?
    ;

// Pausa (silencio) com uma duracao.
pausa
    : 'pausa' ':' duracao
    ;

// Batida de percussao (bateria): uma peca com uma duracao. Ex.: bumbo:4
percussao
    : PECA ':' duracao STAC?
    ;

// Duracao: uma figura, opcionalmente ligada (~) a outras figuras, cujas
// duracoes se somam. Ex.: 4 (seminima), 8. (colcheia pontuada), 4~8 (seminima
// ligada a colcheia = 3/8).
duracao
    : figura (TIL figura)*
    ;

// Figura: o denominador (1,2,4,8,...) com zero ou mais pontos de aumento.
// Cada ponto acrescenta metade do valor anterior (8. = 1/8 + 1/16).
figura
    : INT PONTO*
    ;

/* ============================ LEXER ============================ */

// Modo da tonalidade. Definido antes de IDENT para ter prioridade no empate.
MODO
    : 'maior' | 'menor'
    ;

// Altura completa: nome da nota, acidente opcional e uma oitava (0-9).
// Precisa vir antes de NOTA_CLASSE e IDENT para "vencer" pelo casamento mais longo.
ALTURA
    : NOME_NOTA ('#' | 'b')? [0-9]
    ;

// Classe de nota (sem oitava), usada apenas na tonalidade. Ex.: do, fa#, sib.
NOTA_CLASSE
    : NOME_NOTA ('#' | 'b')?
    ;

// Nomes das sete notas em solfejo (portugues). Fragmento: nao gera token proprio.
fragment NOME_NOTA
    : 'do' | 're' | 'mi' | 'fa' | 'sol' | 'la' | 'si'
    ;

// Pecas de percussao. Definido antes de IDENT para ter prioridade no empate.
PECA
    : 'bumbo' | 'caixa' | 'chimbal' | 'prato'
    ;

// Numero inteiro nao negativo (tempo, oitava ja embutida em ALTURA, duracao, etc.).
INT
    : [0-9]+
    ;

// Identificador: nomes de frases e de instrumentos.
IDENT
    : [a-zA-Z_] [a-zA-Z0-9_]*
    ;

// Barra de compasso.
BARRA
    : '|'
    ;

// Ponto de aumento de figura e ligadura entre figuras.
PONTO
    : '.'
    ;

TIL
    : '~'
    ;

// Marcador de staccato: a nota soa curta sem alterar o tempo ate a proxima.
STAC
    : '!'
    ;

// Espacos em branco e comentarios sao descartados.
WS
    : [ \t\r\n]+ -> skip
    ;

COMENTARIO_LINHA
    : '//' ~[\r\n]* -> skip
    ;

COMENTARIO_BLOCO
    : '/*' .*? '*/' -> skip
    ;
