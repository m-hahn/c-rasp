# Generated from crasp.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .craspParser import craspParser
else:
    from craspParser import craspParser

# This class defines a complete generic visitor for a parse tree produced by craspParser.

class craspVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by craspParser#program.
    def visitProgram(self, ctx:craspParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by craspParser#statement.
    def visitStatement(self, ctx:craspParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by craspParser#bool_expr.
    def visitBool_expr(self, ctx:craspParser.Bool_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by craspParser#count_expr.
    def visitCount_expr(self, ctx:craspParser.Count_exprContext):
        return self.visitChildren(ctx)



del craspParser