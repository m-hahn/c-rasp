# Generated from crasp.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .craspParser import craspParser
else:
    from craspParser import craspParser

# This class defines a complete listener for a parse tree produced by craspParser.
class craspListener(ParseTreeListener):

    # Enter a parse tree produced by craspParser#program.
    def enterProgram(self, ctx:craspParser.ProgramContext):
        pass

    # Exit a parse tree produced by craspParser#program.
    def exitProgram(self, ctx:craspParser.ProgramContext):
        pass


    # Enter a parse tree produced by craspParser#statement.
    def enterStatement(self, ctx:craspParser.StatementContext):
        pass

    # Exit a parse tree produced by craspParser#statement.
    def exitStatement(self, ctx:craspParser.StatementContext):
        pass


    # Enter a parse tree produced by craspParser#bool_expr.
    def enterBool_expr(self, ctx:craspParser.Bool_exprContext):
        pass

    # Exit a parse tree produced by craspParser#bool_expr.
    def exitBool_expr(self, ctx:craspParser.Bool_exprContext):
        pass


    # Enter a parse tree produced by craspParser#count_expr.
    def enterCount_expr(self, ctx:craspParser.Count_exprContext):
        pass

    # Exit a parse tree produced by craspParser#count_expr.
    def exitCount_expr(self, ctx:craspParser.Count_exprContext):
        pass



del craspParser