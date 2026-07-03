# Generated from /home/lucas/Desktop/faculdade/compiladores/projetos/trabalho/cifra/gramatica/Cifra.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,32,167,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,5,0,
        28,8,0,10,0,12,0,31,9,0,1,0,5,0,34,8,0,10,0,12,0,37,9,0,1,0,1,0,
        1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,53,8,1,1,2,1,
        2,1,2,1,2,5,2,59,8,2,10,2,12,2,62,9,2,1,2,1,2,1,3,1,3,1,3,4,3,69,
        8,3,11,3,12,3,70,1,3,5,3,74,8,3,10,3,12,3,77,9,3,3,3,79,8,3,1,3,
        1,3,1,4,1,4,1,4,1,4,3,4,87,8,4,1,4,1,4,5,4,91,8,4,10,4,12,4,94,9,
        4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,105,8,5,10,5,12,5,108,
        9,5,1,5,1,5,1,5,1,5,1,5,3,5,115,8,5,1,6,1,6,1,6,1,6,1,6,3,6,122,
        8,6,1,7,1,7,1,7,1,7,3,7,128,8,7,1,8,1,8,4,8,132,8,8,11,8,12,8,133,
        1,8,1,8,1,8,1,8,3,8,140,8,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,
        3,10,150,8,10,1,11,1,11,1,11,5,11,155,8,11,10,11,12,11,158,9,11,
        1,12,1,12,5,12,162,8,12,10,12,12,12,165,9,12,1,12,0,0,13,0,2,4,6,
        8,10,12,14,16,18,20,22,24,0,0,179,0,29,1,0,0,0,2,52,1,0,0,0,4,54,
        1,0,0,0,6,65,1,0,0,0,8,82,1,0,0,0,10,114,1,0,0,0,12,121,1,0,0,0,
        14,123,1,0,0,0,16,129,1,0,0,0,18,141,1,0,0,0,20,145,1,0,0,0,22,151,
        1,0,0,0,24,159,1,0,0,0,26,28,3,2,1,0,27,26,1,0,0,0,28,31,1,0,0,0,
        29,27,1,0,0,0,29,30,1,0,0,0,30,35,1,0,0,0,31,29,1,0,0,0,32,34,3,
        4,2,0,33,32,1,0,0,0,34,37,1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,
        38,1,0,0,0,37,35,1,0,0,0,38,39,3,6,3,0,39,40,5,0,0,1,40,1,1,0,0,
        0,41,42,5,1,0,0,42,53,5,24,0,0,43,44,5,2,0,0,44,53,5,25,0,0,45,46,
        5,3,0,0,46,47,5,22,0,0,47,53,5,20,0,0,48,49,5,4,0,0,49,50,5,24,0,
        0,50,51,5,5,0,0,51,53,5,24,0,0,52,41,1,0,0,0,52,43,1,0,0,0,52,45,
        1,0,0,0,52,48,1,0,0,0,53,3,1,0,0,0,54,55,5,6,0,0,55,56,5,25,0,0,
        56,60,5,7,0,0,57,59,3,12,6,0,58,57,1,0,0,0,59,62,1,0,0,0,60,58,1,
        0,0,0,60,61,1,0,0,0,61,63,1,0,0,0,62,60,1,0,0,0,63,64,5,8,0,0,64,
        5,1,0,0,0,65,66,5,9,0,0,66,78,5,7,0,0,67,69,3,8,4,0,68,67,1,0,0,
        0,69,70,1,0,0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,79,1,0,0,0,72,74,
        3,10,5,0,73,72,1,0,0,0,74,77,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,
        76,79,1,0,0,0,77,75,1,0,0,0,78,68,1,0,0,0,78,75,1,0,0,0,79,80,1,
        0,0,0,80,81,5,8,0,0,81,7,1,0,0,0,82,83,5,10,0,0,83,86,5,25,0,0,84,
        85,5,11,0,0,85,87,5,24,0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,88,1,0,
        0,0,88,92,5,7,0,0,89,91,3,10,5,0,90,89,1,0,0,0,91,94,1,0,0,0,92,
        90,1,0,0,0,92,93,1,0,0,0,93,95,1,0,0,0,94,92,1,0,0,0,95,96,5,8,0,
        0,96,9,1,0,0,0,97,115,3,12,6,0,98,99,5,12,0,0,99,115,5,25,0,0,100,
        101,5,13,0,0,101,102,5,24,0,0,102,106,5,7,0,0,103,105,3,10,5,0,104,
        103,1,0,0,0,105,108,1,0,0,0,106,104,1,0,0,0,106,107,1,0,0,0,107,
        109,1,0,0,0,108,106,1,0,0,0,109,115,5,8,0,0,110,111,5,14,0,0,111,
        115,5,25,0,0,112,113,5,15,0,0,113,115,5,25,0,0,114,97,1,0,0,0,114,
        98,1,0,0,0,114,100,1,0,0,0,114,110,1,0,0,0,114,112,1,0,0,0,115,11,
        1,0,0,0,116,122,3,14,7,0,117,122,3,16,8,0,118,122,3,18,9,0,119,122,
        3,20,10,0,120,122,5,26,0,0,121,116,1,0,0,0,121,117,1,0,0,0,121,118,
        1,0,0,0,121,119,1,0,0,0,121,120,1,0,0,0,122,13,1,0,0,0,123,124,5,
        21,0,0,124,125,5,16,0,0,125,127,3,22,11,0,126,128,5,29,0,0,127,126,
        1,0,0,0,127,128,1,0,0,0,128,15,1,0,0,0,129,131,5,17,0,0,130,132,
        5,21,0,0,131,130,1,0,0,0,132,133,1,0,0,0,133,131,1,0,0,0,133,134,
        1,0,0,0,134,135,1,0,0,0,135,136,5,18,0,0,136,137,5,16,0,0,137,139,
        3,22,11,0,138,140,5,29,0,0,139,138,1,0,0,0,139,140,1,0,0,0,140,17,
        1,0,0,0,141,142,5,19,0,0,142,143,5,16,0,0,143,144,3,22,11,0,144,
        19,1,0,0,0,145,146,5,23,0,0,146,147,5,16,0,0,147,149,3,22,11,0,148,
        150,5,29,0,0,149,148,1,0,0,0,149,150,1,0,0,0,150,21,1,0,0,0,151,
        156,3,24,12,0,152,153,5,28,0,0,153,155,3,24,12,0,154,152,1,0,0,0,
        155,158,1,0,0,0,156,154,1,0,0,0,156,157,1,0,0,0,157,23,1,0,0,0,158,
        156,1,0,0,0,159,163,5,24,0,0,160,162,5,27,0,0,161,160,1,0,0,0,162,
        165,1,0,0,0,163,161,1,0,0,0,163,164,1,0,0,0,164,25,1,0,0,0,165,163,
        1,0,0,0,18,29,35,52,60,70,75,78,86,92,106,114,121,127,133,139,149,
        156,163
    ]

class CifraParser ( Parser ):

    grammarFileName = "Cifra.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'tempo'", "'instrumento'", "'tom'", "'compasso'", 
                     "'/'", "'frase'", "'{'", "'}'", "'musica'", "'trilha'", 
                     "'volume'", "'toca'", "'repita'", "'marca'", "'espere'", 
                     "':'", "'['", "']'", "'pausa'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'|'", "'.'", "'~'", "'!'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "MODO", "ALTURA", "NOTA_CLASSE", "PECA", "INT", "IDENT", 
                      "BARRA", "PONTO", "TIL", "STAC", "WS", "COMENTARIO_LINHA", 
                      "COMENTARIO_BLOCO" ]

    RULE_programa = 0
    RULE_configuracao = 1
    RULE_declaracao = 2
    RULE_musica = 3
    RULE_trilha = 4
    RULE_comando = 5
    RULE_evento = 6
    RULE_nota = 7
    RULE_acorde = 8
    RULE_pausa = 9
    RULE_percussao = 10
    RULE_duracao = 11
    RULE_figura = 12

    ruleNames =  [ "programa", "configuracao", "declaracao", "musica", "trilha", 
                   "comando", "evento", "nota", "acorde", "pausa", "percussao", 
                   "duracao", "figura" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    MODO=20
    ALTURA=21
    NOTA_CLASSE=22
    PECA=23
    INT=24
    IDENT=25
    BARRA=26
    PONTO=27
    TIL=28
    STAC=29
    WS=30
    COMENTARIO_LINHA=31
    COMENTARIO_BLOCO=32

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def musica(self):
            return self.getTypedRuleContext(CifraParser.MusicaContext,0)


        def EOF(self):
            return self.getToken(CifraParser.EOF, 0)

        def configuracao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CifraParser.ConfiguracaoContext)
            else:
                return self.getTypedRuleContext(CifraParser.ConfiguracaoContext,i)


        def declaracao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CifraParser.DeclaracaoContext)
            else:
                return self.getTypedRuleContext(CifraParser.DeclaracaoContext,i)


        def getRuleIndex(self):
            return CifraParser.RULE_programa

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = CifraParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0):
                self.state = 26
                self.configuracao()
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 32
                self.declaracao()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 38
            self.musica()
            self.state = 39
            self.match(CifraParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConfiguracaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CifraParser.RULE_configuracao

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ConfigTempoContext(ConfiguracaoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CifraParser.ConfiguracaoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(CifraParser.INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConfigTempo" ):
                return visitor.visitConfigTempo(self)
            else:
                return visitor.visitChildren(self)


    class ConfigInstrumentoContext(ConfiguracaoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CifraParser.ConfiguracaoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENT(self):
            return self.getToken(CifraParser.IDENT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConfigInstrumento" ):
                return visitor.visitConfigInstrumento(self)
            else:
                return visitor.visitChildren(self)


    class ConfigCompassoContext(ConfiguracaoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CifraParser.ConfiguracaoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(CifraParser.INT)
            else:
                return self.getToken(CifraParser.INT, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConfigCompasso" ):
                return visitor.visitConfigCompasso(self)
            else:
                return visitor.visitChildren(self)


    class ConfigTomContext(ConfiguracaoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CifraParser.ConfiguracaoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOTA_CLASSE(self):
            return self.getToken(CifraParser.NOTA_CLASSE, 0)
        def MODO(self):
            return self.getToken(CifraParser.MODO, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConfigTom" ):
                return visitor.visitConfigTom(self)
            else:
                return visitor.visitChildren(self)



    def configuracao(self):

        localctx = CifraParser.ConfiguracaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_configuracao)
        try:
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = CifraParser.ConfigTempoContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.match(CifraParser.T__0)
                self.state = 42
                self.match(CifraParser.INT)
                pass
            elif token in [2]:
                localctx = CifraParser.ConfigInstrumentoContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.match(CifraParser.T__1)
                self.state = 44
                self.match(CifraParser.IDENT)
                pass
            elif token in [3]:
                localctx = CifraParser.ConfigTomContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 45
                self.match(CifraParser.T__2)
                self.state = 46
                self.match(CifraParser.NOTA_CLASSE)
                self.state = 47
                self.match(CifraParser.MODO)
                pass
            elif token in [4]:
                localctx = CifraParser.ConfigCompassoContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 48
                self.match(CifraParser.T__3)
                self.state = 49
                self.match(CifraParser.INT)
                self.state = 50
                self.match(CifraParser.T__4)
                self.state = 51
                self.match(CifraParser.INT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(CifraParser.IDENT, 0)

        def evento(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CifraParser.EventoContext)
            else:
                return self.getTypedRuleContext(CifraParser.EventoContext,i)


        def getRuleIndex(self):
            return CifraParser.RULE_declaracao

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracao" ):
                return visitor.visitDeclaracao(self)
            else:
                return visitor.visitChildren(self)




    def declaracao(self):

        localctx = CifraParser.DeclaracaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaracao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(CifraParser.T__5)
            self.state = 55
            self.match(CifraParser.IDENT)
            self.state = 56
            self.match(CifraParser.T__6)
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 78249984) != 0):
                self.state = 57
                self.evento()
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 63
            self.match(CifraParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MusicaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def trilha(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CifraParser.TrilhaContext)
            else:
                return self.getTypedRuleContext(CifraParser.TrilhaContext,i)


        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CifraParser.ComandoContext)
            else:
                return self.getTypedRuleContext(CifraParser.ComandoContext,i)


        def getRuleIndex(self):
            return CifraParser.RULE_musica

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMusica" ):
                return visitor.visitMusica(self)
            else:
                return visitor.visitChildren(self)




    def musica(self):

        localctx = CifraParser.MusicaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_musica)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(CifraParser.T__8)
            self.state = 66
            self.match(CifraParser.T__6)
            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.state = 68 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 67
                    self.trilha()
                    self.state = 70 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==10):
                        break

                pass
            elif token in [8, 12, 13, 14, 15, 17, 19, 21, 23, 26]:
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 78311424) != 0):
                    self.state = 72
                    self.comando()
                    self.state = 77
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

            self.state = 80
            self.match(CifraParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TrilhaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(CifraParser.IDENT, 0)

        def INT(self):
            return self.getToken(CifraParser.INT, 0)

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CifraParser.ComandoContext)
            else:
                return self.getTypedRuleContext(CifraParser.ComandoContext,i)


        def getRuleIndex(self):
            return CifraParser.RULE_trilha

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrilha" ):
                return visitor.visitTrilha(self)
            else:
                return visitor.visitChildren(self)




    def trilha(self):

        localctx = CifraParser.TrilhaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_trilha)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(CifraParser.T__9)
            self.state = 83
            self.match(CifraParser.IDENT)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 84
                self.match(CifraParser.T__10)
                self.state = 85
                self.match(CifraParser.INT)


            self.state = 88
            self.match(CifraParser.T__6)
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 78311424) != 0):
                self.state = 89
                self.comando()
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 95
            self.match(CifraParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CifraParser.RULE_comando

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ComandoEspereContext(ComandoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CifraParser.ComandoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENT(self):
            return self.getToken(CifraParser.IDENT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComandoEspere" ):
                return visitor.visitComandoEspere(self)
            else:
                return visitor.visitChildren(self)


    class ComandoTocaContext(ComandoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CifraParser.ComandoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENT(self):
            return self.getToken(CifraParser.IDENT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComandoToca" ):
                return visitor.visitComandoToca(self)
            else:
                return visitor.visitChildren(self)


    class ComandoMarcaContext(ComandoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CifraParser.ComandoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENT(self):
            return self.getToken(CifraParser.IDENT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComandoMarca" ):
                return visitor.visitComandoMarca(self)
            else:
                return visitor.visitChildren(self)


    class ComandoRepitaContext(ComandoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CifraParser.ComandoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(CifraParser.INT, 0)
        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CifraParser.ComandoContext)
            else:
                return self.getTypedRuleContext(CifraParser.ComandoContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComandoRepita" ):
                return visitor.visitComandoRepita(self)
            else:
                return visitor.visitChildren(self)


    class ComandoEventoContext(ComandoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CifraParser.ComandoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def evento(self):
            return self.getTypedRuleContext(CifraParser.EventoContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComandoEvento" ):
                return visitor.visitComandoEvento(self)
            else:
                return visitor.visitChildren(self)



    def comando(self):

        localctx = CifraParser.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_comando)
        self._la = 0 # Token type
        try:
            self.state = 114
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17, 19, 21, 23, 26]:
                localctx = CifraParser.ComandoEventoContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                self.evento()
                pass
            elif token in [12]:
                localctx = CifraParser.ComandoTocaContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 98
                self.match(CifraParser.T__11)
                self.state = 99
                self.match(CifraParser.IDENT)
                pass
            elif token in [13]:
                localctx = CifraParser.ComandoRepitaContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 100
                self.match(CifraParser.T__12)
                self.state = 101
                self.match(CifraParser.INT)
                self.state = 102
                self.match(CifraParser.T__6)
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 78311424) != 0):
                    self.state = 103
                    self.comando()
                    self.state = 108
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 109
                self.match(CifraParser.T__7)
                pass
            elif token in [14]:
                localctx = CifraParser.ComandoMarcaContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 110
                self.match(CifraParser.T__13)
                self.state = 111
                self.match(CifraParser.IDENT)
                pass
            elif token in [15]:
                localctx = CifraParser.ComandoEspereContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 112
                self.match(CifraParser.T__14)
                self.state = 113
                self.match(CifraParser.IDENT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EventoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CifraParser.RULE_evento

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class EventoPercussaoContext(EventoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CifraParser.EventoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def percussao(self):
            return self.getTypedRuleContext(CifraParser.PercussaoContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEventoPercussao" ):
                return visitor.visitEventoPercussao(self)
            else:
                return visitor.visitChildren(self)


    class EventoPausaContext(EventoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CifraParser.EventoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def pausa(self):
            return self.getTypedRuleContext(CifraParser.PausaContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEventoPausa" ):
                return visitor.visitEventoPausa(self)
            else:
                return visitor.visitChildren(self)


    class EventoAcordeContext(EventoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CifraParser.EventoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def acorde(self):
            return self.getTypedRuleContext(CifraParser.AcordeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEventoAcorde" ):
                return visitor.visitEventoAcorde(self)
            else:
                return visitor.visitChildren(self)


    class EventoNotaContext(EventoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CifraParser.EventoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def nota(self):
            return self.getTypedRuleContext(CifraParser.NotaContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEventoNota" ):
                return visitor.visitEventoNota(self)
            else:
                return visitor.visitChildren(self)


    class EventoBarraContext(EventoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CifraParser.EventoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BARRA(self):
            return self.getToken(CifraParser.BARRA, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEventoBarra" ):
                return visitor.visitEventoBarra(self)
            else:
                return visitor.visitChildren(self)



    def evento(self):

        localctx = CifraParser.EventoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_evento)
        try:
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                localctx = CifraParser.EventoNotaContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self.nota()
                pass
            elif token in [17]:
                localctx = CifraParser.EventoAcordeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.acorde()
                pass
            elif token in [19]:
                localctx = CifraParser.EventoPausaContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 118
                self.pausa()
                pass
            elif token in [23]:
                localctx = CifraParser.EventoPercussaoContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 119
                self.percussao()
                pass
            elif token in [26]:
                localctx = CifraParser.EventoBarraContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 120
                self.match(CifraParser.BARRA)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NotaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ALTURA(self):
            return self.getToken(CifraParser.ALTURA, 0)

        def duracao(self):
            return self.getTypedRuleContext(CifraParser.DuracaoContext,0)


        def STAC(self):
            return self.getToken(CifraParser.STAC, 0)

        def getRuleIndex(self):
            return CifraParser.RULE_nota

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNota" ):
                return visitor.visitNota(self)
            else:
                return visitor.visitChildren(self)




    def nota(self):

        localctx = CifraParser.NotaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_nota)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(CifraParser.ALTURA)
            self.state = 124
            self.match(CifraParser.T__15)
            self.state = 125
            self.duracao()
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 126
                self.match(CifraParser.STAC)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AcordeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def duracao(self):
            return self.getTypedRuleContext(CifraParser.DuracaoContext,0)


        def ALTURA(self, i:int=None):
            if i is None:
                return self.getTokens(CifraParser.ALTURA)
            else:
                return self.getToken(CifraParser.ALTURA, i)

        def STAC(self):
            return self.getToken(CifraParser.STAC, 0)

        def getRuleIndex(self):
            return CifraParser.RULE_acorde

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAcorde" ):
                return visitor.visitAcorde(self)
            else:
                return visitor.visitChildren(self)




    def acorde(self):

        localctx = CifraParser.AcordeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_acorde)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(CifraParser.T__16)
            self.state = 131 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 130
                self.match(CifraParser.ALTURA)
                self.state = 133 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==21):
                    break

            self.state = 135
            self.match(CifraParser.T__17)
            self.state = 136
            self.match(CifraParser.T__15)
            self.state = 137
            self.duracao()
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 138
                self.match(CifraParser.STAC)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PausaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def duracao(self):
            return self.getTypedRuleContext(CifraParser.DuracaoContext,0)


        def getRuleIndex(self):
            return CifraParser.RULE_pausa

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPausa" ):
                return visitor.visitPausa(self)
            else:
                return visitor.visitChildren(self)




    def pausa(self):

        localctx = CifraParser.PausaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_pausa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(CifraParser.T__18)
            self.state = 142
            self.match(CifraParser.T__15)
            self.state = 143
            self.duracao()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PercussaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PECA(self):
            return self.getToken(CifraParser.PECA, 0)

        def duracao(self):
            return self.getTypedRuleContext(CifraParser.DuracaoContext,0)


        def STAC(self):
            return self.getToken(CifraParser.STAC, 0)

        def getRuleIndex(self):
            return CifraParser.RULE_percussao

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPercussao" ):
                return visitor.visitPercussao(self)
            else:
                return visitor.visitChildren(self)




    def percussao(self):

        localctx = CifraParser.PercussaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_percussao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(CifraParser.PECA)
            self.state = 146
            self.match(CifraParser.T__15)
            self.state = 147
            self.duracao()
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 148
                self.match(CifraParser.STAC)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DuracaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def figura(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CifraParser.FiguraContext)
            else:
                return self.getTypedRuleContext(CifraParser.FiguraContext,i)


        def TIL(self, i:int=None):
            if i is None:
                return self.getTokens(CifraParser.TIL)
            else:
                return self.getToken(CifraParser.TIL, i)

        def getRuleIndex(self):
            return CifraParser.RULE_duracao

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDuracao" ):
                return visitor.visitDuracao(self)
            else:
                return visitor.visitChildren(self)




    def duracao(self):

        localctx = CifraParser.DuracaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_duracao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.figura()
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 152
                self.match(CifraParser.TIL)
                self.state = 153
                self.figura()
                self.state = 158
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FiguraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CifraParser.INT, 0)

        def PONTO(self, i:int=None):
            if i is None:
                return self.getTokens(CifraParser.PONTO)
            else:
                return self.getToken(CifraParser.PONTO, i)

        def getRuleIndex(self):
            return CifraParser.RULE_figura

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFigura" ):
                return visitor.visitFigura(self)
            else:
                return visitor.visitChildren(self)




    def figura(self):

        localctx = CifraParser.FiguraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_figura)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(CifraParser.INT)
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 160
                self.match(CifraParser.PONTO)
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





