# Generated from /home/lucas/Desktop/faculdade/compiladores/projetos/trabalho/cifra/gramatica/Cifra.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CifraParser import CifraParser
else:
    from CifraParser import CifraParser

# This class defines a complete generic visitor for a parse tree produced by CifraParser.

class CifraVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CifraParser#programa.
    def visitPrograma(self, ctx:CifraParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CifraParser#configTempo.
    def visitConfigTempo(self, ctx:CifraParser.ConfigTempoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CifraParser#configInstrumento.
    def visitConfigInstrumento(self, ctx:CifraParser.ConfigInstrumentoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CifraParser#configTom.
    def visitConfigTom(self, ctx:CifraParser.ConfigTomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CifraParser#configCompasso.
    def visitConfigCompasso(self, ctx:CifraParser.ConfigCompassoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CifraParser#declaracao.
    def visitDeclaracao(self, ctx:CifraParser.DeclaracaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CifraParser#musica.
    def visitMusica(self, ctx:CifraParser.MusicaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CifraParser#trilha.
    def visitTrilha(self, ctx:CifraParser.TrilhaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CifraParser#comandoEvento.
    def visitComandoEvento(self, ctx:CifraParser.ComandoEventoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CifraParser#comandoToca.
    def visitComandoToca(self, ctx:CifraParser.ComandoTocaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CifraParser#comandoRepita.
    def visitComandoRepita(self, ctx:CifraParser.ComandoRepitaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CifraParser#comandoMarca.
    def visitComandoMarca(self, ctx:CifraParser.ComandoMarcaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CifraParser#comandoEspere.
    def visitComandoEspere(self, ctx:CifraParser.ComandoEspereContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CifraParser#eventoNota.
    def visitEventoNota(self, ctx:CifraParser.EventoNotaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CifraParser#eventoAcorde.
    def visitEventoAcorde(self, ctx:CifraParser.EventoAcordeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CifraParser#eventoPausa.
    def visitEventoPausa(self, ctx:CifraParser.EventoPausaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CifraParser#eventoPercussao.
    def visitEventoPercussao(self, ctx:CifraParser.EventoPercussaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CifraParser#eventoBarra.
    def visitEventoBarra(self, ctx:CifraParser.EventoBarraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CifraParser#nota.
    def visitNota(self, ctx:CifraParser.NotaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CifraParser#acorde.
    def visitAcorde(self, ctx:CifraParser.AcordeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CifraParser#pausa.
    def visitPausa(self, ctx:CifraParser.PausaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CifraParser#percussao.
    def visitPercussao(self, ctx:CifraParser.PercussaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CifraParser#duracao.
    def visitDuracao(self, ctx:CifraParser.DuracaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CifraParser#figura.
    def visitFigura(self, ctx:CifraParser.FiguraContext):
        return self.visitChildren(ctx)



del CifraParser