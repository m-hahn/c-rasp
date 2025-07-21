

from antlr4 import *
from antlr.craspLexer import craspLexer as CRaspLexer
from antlr.craspParser import craspParser as CRaspParser
from antlr.craspVisitor import craspVisitor as CRaspVisitor
from program import *


class MyCraspVisitor(CRaspVisitor):
    imports: list[str] = []

    def visitProgram(self, ctx):
        stmts = [self.visit(s) for s in ctx.statement()]
        stmts = [s for s in stmts if s is not None]
        return Program(stmts, self.imports)

    def visitStatement(self, ctx):
        if ctx.IMPORT():
            # Handle the import statement: 'IMPORT VARIABLE'
            var_name = ctx.VARIABLE().getText()
            self.imports.append(var_name)
            return None
        else:
            # Handle the assignment: 'VARIABLE ASSIGN (bool_expr | count_expr)'
            var_name = ctx.VARIABLE().getText()
            expr = self.visit(ctx.getChild(2))
            return Assignment(var_name, expr)

    def visitBool_expr(self, ctx):
        if ctx.STRING_LITERAL():
            return StringLiteral(ctx.STRING_LITERAL().getText().strip('"'))

        elif ctx.LT():
            return Comparison(
                left=self.visit(ctx.count_expr(0)),
                op="<",
                right=self.visit(ctx.count_expr(1))
            )

        elif ctx.GT():
            return Comparison(
                left=self.visit(ctx.count_expr(0)),
                op=">",
                right=self.visit(ctx.count_expr(1))
            )

        elif ctx.EQ():
            return Comparison(
                left=self.visit(ctx.count_expr(0)),
                op="==",
                right=self.visit(ctx.count_expr(1))
            )

        elif ctx.LEQ():
            return Comparison(
                left=self.visit(ctx.count_expr(0)),
                op="<=",
                right=self.visit(ctx.count_expr(1))
            )

        elif ctx.GEQ():
            return Comparison(
                left=self.visit(ctx.count_expr(0)),
                op=">=",
                right=self.visit(ctx.count_expr(1))
            )

        elif ctx.AND():
            return BinaryBoolExpr(
                left=self.visit(ctx.bool_expr(0)),
                op="and",
                right=self.visit(ctx.bool_expr(1))
            )

        elif ctx.OR():
            return BinaryBoolExpr(
                left=self.visit(ctx.bool_expr(0)),
                op="or",
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
            if ctx.VARIABLE():  # means it's: COUNT '[' VARIABLE ']' bool_expr
                var = ctx.VARIABLE().getText()
                expr = self.visit(ctx.bool_expr())
                return GuardedCount(var, expr)
            else:  # just: COUNT bool_expr
                expr = self.visit(ctx.bool_expr())
                return Count(expr)

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
    input_stream = FileStream(filename, encoding="utf-8")
    lexer = CRaspLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CRaspParser(stream)

    # Replace 'startRule' with your actual entry rule
    tree = parser.program()
    # print(tree.toStringTree(recog=parser))

    visitor = MyCraspVisitor()
    ast : Program = visitor.visit(tree)

    return ast
