

from antlr4 import *
from antlr.craspLexer import craspLexer as CRaspLexer
from antlr.craspParser import craspParser as CRaspParser
from antlr.craspVisitor import craspVisitor as CRaspVisitor
from program import *


class MyCraspVisitor(CRaspVisitor):
    def visitProgram(self, ctx):
        stmts = [self.visit(s) for s in ctx.statement()]
        return Program(stmts)

    def visitStatement(self, ctx):
        var = ctx.VARIABLE().getText()
        expr = self.visit(ctx.getChild(2))
        return Assignment(var, expr)

    def visitBool_expr(self, ctx):
        if ctx.STRING_LITERAL():
            return StringLiteral(ctx.STRING_LITERAL().getText().strip('"'))

        elif ctx.LT():
            return Comparison(
                left=self.visit(ctx.count_expr(0)),
                op="<",
                right=self.visit(ctx.count_expr(1))
            )

        elif ctx.EQ():
            return Comparison(
                left=self.visit(ctx.count_expr(0)),
                op="==",
                right=self.visit(ctx.count_expr(1))
            )

        elif ctx.AND():
            return AndExpr(
                left=self.visit(ctx.bool_expr(0)),
                right=self.visit(ctx.bool_expr(1))
            )

        elif ctx.NOT():
            return NotExpr(self.visit(ctx.bool_expr(0)))

        elif ctx.VARIABLE():
            return BoolVariable(ctx.VARIABLE().getText())

        elif ctx.TRUE():
            return BoolLiteral(True)

        elif ctx.FALSE():
            return BoolLiteral(False)

        elif ctx.LPAREN():
            return self.visit(ctx.bool_expr(0))
        

    def visitCount_expr(self, ctx):
        if ctx.COUNT():
            return Count(self.visit(ctx.bool_expr()))

        elif ctx.IF():
            return IfExpr(
                then_branch=self.visit(ctx.count_expr(0)),
                condition=self.visit(ctx.bool_expr()),
                else_branch=self.visit(ctx.count_expr(1))
            )

        elif ctx.PLUS():
            return BinaryOp(
                left=self.visit(ctx.count_expr(0)),
                op="+",
                right=self.visit(ctx.count_expr(1))
            )

        elif ctx.MINUS():
            return BinaryOp(
                left=self.visit(ctx.count_expr(0)),
                op="-",
                right=self.visit(ctx.count_expr(1))
            )

        elif ctx.MAX():
            return BinaryOp(
                op="max",
                left=self.visit(ctx.count_expr(0)),
                right=self.visit(ctx.count_expr(1))
            )

        elif ctx.MIN():
            return BinaryOp(
                op="min",
                left=self.visit(ctx.count_expr(0)),
                right=self.visit(ctx.count_expr(1))
            )

        elif ctx.INT_LITERAL():
            return CountLiteral(int(ctx.INT_LITERAL().getText()))

        elif ctx.VARIABLE():
            return CountVariable(ctx.VARIABLE().getText())

        elif ctx.LPAREN():
            return self.visit(ctx.count_expr(0))


def parse_file(filename) -> Program:
    input_stream = FileStream(filename)
    lexer = CRaspLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CRaspParser(stream)

    # Replace 'startRule' with your actual entry rule
    tree = parser.program()
    # print(tree.toStringTree(recog=parser))

    visitor = MyCraspVisitor()
    ast : Program = visitor.visit(tree)

    return ast
