# Generated from crasp.g4 by ANTLR 4.13.1
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
        4,1,33,140,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,5,0,10,8,0,10,0,12,
        0,13,9,0,1,0,1,0,4,0,17,8,0,11,0,12,0,18,1,0,5,0,22,8,0,10,0,12,
        0,25,9,0,1,0,5,0,28,8,0,10,0,12,0,31,9,0,1,0,1,0,1,1,1,1,1,1,1,1,
        3,1,39,8,1,1,1,1,1,3,1,43,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,80,8,2,1,2,1,2,1,2,
        1,2,1,2,1,2,5,2,88,8,2,10,2,12,2,91,9,2,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,3,3,121,8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,5,3,135,8,3,10,3,12,3,138,9,3,1,3,0,2,4,6,4,
        0,2,4,6,0,0,163,0,11,1,0,0,0,2,42,1,0,0,0,4,79,1,0,0,0,6,120,1,0,
        0,0,8,10,5,32,0,0,9,8,1,0,0,0,10,13,1,0,0,0,11,9,1,0,0,0,11,12,1,
        0,0,0,12,14,1,0,0,0,13,11,1,0,0,0,14,23,3,2,1,0,15,17,5,32,0,0,16,
        15,1,0,0,0,17,18,1,0,0,0,18,16,1,0,0,0,18,19,1,0,0,0,19,20,1,0,0,
        0,20,22,3,2,1,0,21,16,1,0,0,0,22,25,1,0,0,0,23,21,1,0,0,0,23,24,
        1,0,0,0,24,29,1,0,0,0,25,23,1,0,0,0,26,28,5,32,0,0,27,26,1,0,0,0,
        28,31,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,32,1,0,0,0,31,29,1,
        0,0,0,32,33,5,0,0,1,33,1,1,0,0,0,34,35,5,5,0,0,35,38,5,21,0,0,36,
        39,3,4,2,0,37,39,3,6,3,0,38,36,1,0,0,0,38,37,1,0,0,0,39,43,1,0,0,
        0,40,41,5,4,0,0,41,43,5,5,0,0,42,34,1,0,0,0,42,40,1,0,0,0,43,3,1,
        0,0,0,44,45,6,2,-1,0,45,80,5,6,0,0,46,47,3,6,3,0,47,48,5,17,0,0,
        48,49,3,6,3,0,49,80,1,0,0,0,50,51,3,6,3,0,51,52,5,18,0,0,52,53,3,
        6,3,0,53,80,1,0,0,0,54,55,3,6,3,0,55,56,5,15,0,0,56,57,3,6,3,0,57,
        80,1,0,0,0,58,59,3,6,3,0,59,60,5,16,0,0,60,61,3,6,3,0,61,80,1,0,
        0,0,62,63,3,6,3,0,63,64,5,19,0,0,64,65,3,6,3,0,65,80,1,0,0,0,66,
        67,3,6,3,0,67,68,5,20,0,0,68,69,3,6,3,0,69,80,1,0,0,0,70,71,5,14,
        0,0,71,80,3,4,2,5,72,80,5,5,0,0,73,74,5,29,0,0,74,75,3,4,2,0,75,
        76,5,30,0,0,76,80,1,0,0,0,77,80,5,8,0,0,78,80,5,9,0,0,79,44,1,0,
        0,0,79,46,1,0,0,0,79,50,1,0,0,0,79,54,1,0,0,0,79,58,1,0,0,0,79,62,
        1,0,0,0,79,66,1,0,0,0,79,70,1,0,0,0,79,72,1,0,0,0,79,73,1,0,0,0,
        79,77,1,0,0,0,79,78,1,0,0,0,80,89,1,0,0,0,81,82,10,7,0,0,82,83,5,
        12,0,0,83,88,3,4,2,8,84,85,10,6,0,0,85,86,5,13,0,0,86,88,3,4,2,7,
        87,81,1,0,0,0,87,84,1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,89,90,1,
        0,0,0,90,5,1,0,0,0,91,89,1,0,0,0,92,93,6,3,-1,0,93,94,5,28,0,0,94,
        121,3,4,2,0,95,96,5,28,0,0,96,97,5,1,0,0,97,98,5,5,0,0,98,99,5,2,
        0,0,99,121,3,4,2,0,100,121,5,5,0,0,101,121,5,7,0,0,102,103,5,27,
        0,0,103,104,5,29,0,0,104,105,3,6,3,0,105,106,5,31,0,0,106,107,3,
        6,3,0,107,108,5,30,0,0,108,121,1,0,0,0,109,110,5,26,0,0,110,111,
        5,29,0,0,111,112,3,6,3,0,112,113,5,31,0,0,113,114,3,6,3,0,114,115,
        5,30,0,0,115,121,1,0,0,0,116,117,5,29,0,0,117,118,3,6,3,0,118,119,
        5,30,0,0,119,121,1,0,0,0,120,92,1,0,0,0,120,95,1,0,0,0,120,100,1,
        0,0,0,120,101,1,0,0,0,120,102,1,0,0,0,120,109,1,0,0,0,120,116,1,
        0,0,0,121,136,1,0,0,0,122,123,10,6,0,0,123,124,5,24,0,0,124,135,
        3,6,3,7,125,126,10,5,0,0,126,127,5,25,0,0,127,135,3,6,3,6,128,129,
        10,2,0,0,129,130,5,10,0,0,130,131,3,4,2,0,131,132,5,11,0,0,132,133,
        3,6,3,3,133,135,1,0,0,0,134,122,1,0,0,0,134,125,1,0,0,0,134,128,
        1,0,0,0,135,138,1,0,0,0,136,134,1,0,0,0,136,137,1,0,0,0,137,7,1,
        0,0,0,138,136,1,0,0,0,12,11,18,23,29,38,42,79,87,89,120,134,136
    ]

class craspParser ( Parser ):

    grammarFileName = "crasp.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "<INVALID>", "'#import'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'true'", "'false'", 
                     "'if'", "'else'", "'&&'", "'||'", "'!'", "'=='", "'!='", 
                     "'<'", "'>'", "'<='", "'>='", "'='", "'?'", "':'", 
                     "'+'", "'-'", "'min'", "'max'", "'#'", "'('", "')'", 
                     "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "LINE_COMMENT", 
                      "IMPORT", "VARIABLE", "STRING_LITERAL", "INT_LITERAL", 
                      "TRUE", "FALSE", "IF", "ELSE", "AND", "OR", "NOT", 
                      "EQ", "NEQ", "LT", "GT", "LEQ", "GEQ", "ASSIGN", "QUESTION", 
                      "COLON", "PLUS", "MINUS", "MIN", "MAX", "COUNT", "LPAREN", 
                      "RPAREN", "COMMA", "NL", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_bool_expr = 2
    RULE_count_expr = 3

    ruleNames =  [ "program", "statement", "bool_expr", "count_expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    LINE_COMMENT=3
    IMPORT=4
    VARIABLE=5
    STRING_LITERAL=6
    INT_LITERAL=7
    TRUE=8
    FALSE=9
    IF=10
    ELSE=11
    AND=12
    OR=13
    NOT=14
    EQ=15
    NEQ=16
    LT=17
    GT=18
    LEQ=19
    GEQ=20
    ASSIGN=21
    QUESTION=22
    COLON=23
    PLUS=24
    MINUS=25
    MIN=26
    MAX=27
    COUNT=28
    LPAREN=29
    RPAREN=30
    COMMA=31
    NL=32
    WS=33

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(craspParser.StatementContext)
            else:
                return self.getTypedRuleContext(craspParser.StatementContext,i)


        def EOF(self):
            return self.getToken(craspParser.EOF, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(craspParser.NL)
            else:
                return self.getToken(craspParser.NL, i)

        def getRuleIndex(self):
            return craspParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = craspParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32:
                self.state = 8
                self.match(craspParser.NL)
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 14
            self.statement()
            self.state = 23
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 16 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 15
                        self.match(craspParser.NL)
                        self.state = 18 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==32):
                            break

                    self.state = 20
                    self.statement() 
                self.state = 25
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32:
                self.state = 26
                self.match(craspParser.NL)
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 32
            self.match(craspParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(craspParser.VARIABLE, 0)

        def ASSIGN(self):
            return self.getToken(craspParser.ASSIGN, 0)

        def bool_expr(self):
            return self.getTypedRuleContext(craspParser.Bool_exprContext,0)


        def count_expr(self):
            return self.getTypedRuleContext(craspParser.Count_exprContext,0)


        def IMPORT(self):
            return self.getToken(craspParser.IMPORT, 0)

        def getRuleIndex(self):
            return craspParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = craspParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.match(craspParser.VARIABLE)
                self.state = 35
                self.match(craspParser.ASSIGN)
                self.state = 38
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 36
                    self.bool_expr(0)
                    pass

                elif la_ == 2:
                    self.state = 37
                    self.count_expr(0)
                    pass


                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.match(craspParser.IMPORT)
                self.state = 41
                self.match(craspParser.VARIABLE)
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


    class Bool_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_LITERAL(self):
            return self.getToken(craspParser.STRING_LITERAL, 0)

        def count_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(craspParser.Count_exprContext)
            else:
                return self.getTypedRuleContext(craspParser.Count_exprContext,i)


        def LT(self):
            return self.getToken(craspParser.LT, 0)

        def GT(self):
            return self.getToken(craspParser.GT, 0)

        def EQ(self):
            return self.getToken(craspParser.EQ, 0)

        def NEQ(self):
            return self.getToken(craspParser.NEQ, 0)

        def LEQ(self):
            return self.getToken(craspParser.LEQ, 0)

        def GEQ(self):
            return self.getToken(craspParser.GEQ, 0)

        def NOT(self):
            return self.getToken(craspParser.NOT, 0)

        def bool_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(craspParser.Bool_exprContext)
            else:
                return self.getTypedRuleContext(craspParser.Bool_exprContext,i)


        def VARIABLE(self):
            return self.getToken(craspParser.VARIABLE, 0)

        def LPAREN(self):
            return self.getToken(craspParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(craspParser.RPAREN, 0)

        def TRUE(self):
            return self.getToken(craspParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(craspParser.FALSE, 0)

        def AND(self):
            return self.getToken(craspParser.AND, 0)

        def OR(self):
            return self.getToken(craspParser.OR, 0)

        def getRuleIndex(self):
            return craspParser.RULE_bool_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_expr" ):
                listener.enterBool_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_expr" ):
                listener.exitBool_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_expr" ):
                return visitor.visitBool_expr(self)
            else:
                return visitor.visitChildren(self)



    def bool_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = craspParser.Bool_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_bool_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 45
                self.match(craspParser.STRING_LITERAL)
                pass

            elif la_ == 2:
                self.state = 46
                self.count_expr(0)
                self.state = 47
                self.match(craspParser.LT)
                self.state = 48
                self.count_expr(0)
                pass

            elif la_ == 3:
                self.state = 50
                self.count_expr(0)
                self.state = 51
                self.match(craspParser.GT)
                self.state = 52
                self.count_expr(0)
                pass

            elif la_ == 4:
                self.state = 54
                self.count_expr(0)
                self.state = 55
                self.match(craspParser.EQ)
                self.state = 56
                self.count_expr(0)
                pass

            elif la_ == 5:
                self.state = 58
                self.count_expr(0)
                self.state = 59
                self.match(craspParser.NEQ)
                self.state = 60
                self.count_expr(0)
                pass

            elif la_ == 6:
                self.state = 62
                self.count_expr(0)
                self.state = 63
                self.match(craspParser.LEQ)
                self.state = 64
                self.count_expr(0)
                pass

            elif la_ == 7:
                self.state = 66
                self.count_expr(0)
                self.state = 67
                self.match(craspParser.GEQ)
                self.state = 68
                self.count_expr(0)
                pass

            elif la_ == 8:
                self.state = 70
                self.match(craspParser.NOT)
                self.state = 71
                self.bool_expr(5)
                pass

            elif la_ == 9:
                self.state = 72
                self.match(craspParser.VARIABLE)
                pass

            elif la_ == 10:
                self.state = 73
                self.match(craspParser.LPAREN)
                self.state = 74
                self.bool_expr(0)
                self.state = 75
                self.match(craspParser.RPAREN)
                pass

            elif la_ == 11:
                self.state = 77
                self.match(craspParser.TRUE)
                pass

            elif la_ == 12:
                self.state = 78
                self.match(craspParser.FALSE)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 89
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 87
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = craspParser.Bool_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_bool_expr)
                        self.state = 81
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 82
                        self.match(craspParser.AND)
                        self.state = 83
                        self.bool_expr(8)
                        pass

                    elif la_ == 2:
                        localctx = craspParser.Bool_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_bool_expr)
                        self.state = 84
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 85
                        self.match(craspParser.OR)
                        self.state = 86
                        self.bool_expr(7)
                        pass

             
                self.state = 91
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Count_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COUNT(self):
            return self.getToken(craspParser.COUNT, 0)

        def bool_expr(self):
            return self.getTypedRuleContext(craspParser.Bool_exprContext,0)


        def VARIABLE(self):
            return self.getToken(craspParser.VARIABLE, 0)

        def INT_LITERAL(self):
            return self.getToken(craspParser.INT_LITERAL, 0)

        def MAX(self):
            return self.getToken(craspParser.MAX, 0)

        def LPAREN(self):
            return self.getToken(craspParser.LPAREN, 0)

        def count_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(craspParser.Count_exprContext)
            else:
                return self.getTypedRuleContext(craspParser.Count_exprContext,i)


        def COMMA(self):
            return self.getToken(craspParser.COMMA, 0)

        def RPAREN(self):
            return self.getToken(craspParser.RPAREN, 0)

        def MIN(self):
            return self.getToken(craspParser.MIN, 0)

        def PLUS(self):
            return self.getToken(craspParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(craspParser.MINUS, 0)

        def IF(self):
            return self.getToken(craspParser.IF, 0)

        def ELSE(self):
            return self.getToken(craspParser.ELSE, 0)

        def getRuleIndex(self):
            return craspParser.RULE_count_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCount_expr" ):
                listener.enterCount_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCount_expr" ):
                listener.exitCount_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCount_expr" ):
                return visitor.visitCount_expr(self)
            else:
                return visitor.visitChildren(self)



    def count_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = craspParser.Count_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_count_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 93
                self.match(craspParser.COUNT)
                self.state = 94
                self.bool_expr(0)
                pass

            elif la_ == 2:
                self.state = 95
                self.match(craspParser.COUNT)
                self.state = 96
                self.match(craspParser.T__0)
                self.state = 97
                self.match(craspParser.VARIABLE)
                self.state = 98
                self.match(craspParser.T__1)
                self.state = 99
                self.bool_expr(0)
                pass

            elif la_ == 3:
                self.state = 100
                self.match(craspParser.VARIABLE)
                pass

            elif la_ == 4:
                self.state = 101
                self.match(craspParser.INT_LITERAL)
                pass

            elif la_ == 5:
                self.state = 102
                self.match(craspParser.MAX)
                self.state = 103
                self.match(craspParser.LPAREN)
                self.state = 104
                self.count_expr(0)
                self.state = 105
                self.match(craspParser.COMMA)
                self.state = 106
                self.count_expr(0)
                self.state = 107
                self.match(craspParser.RPAREN)
                pass

            elif la_ == 6:
                self.state = 109
                self.match(craspParser.MIN)
                self.state = 110
                self.match(craspParser.LPAREN)
                self.state = 111
                self.count_expr(0)
                self.state = 112
                self.match(craspParser.COMMA)
                self.state = 113
                self.count_expr(0)
                self.state = 114
                self.match(craspParser.RPAREN)
                pass

            elif la_ == 7:
                self.state = 116
                self.match(craspParser.LPAREN)
                self.state = 117
                self.count_expr(0)
                self.state = 118
                self.match(craspParser.RPAREN)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 136
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 134
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = craspParser.Count_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_count_expr)
                        self.state = 122
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 123
                        self.match(craspParser.PLUS)
                        self.state = 124
                        self.count_expr(7)
                        pass

                    elif la_ == 2:
                        localctx = craspParser.Count_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_count_expr)
                        self.state = 125
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 126
                        self.match(craspParser.MINUS)
                        self.state = 127
                        self.count_expr(6)
                        pass

                    elif la_ == 3:
                        localctx = craspParser.Count_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_count_expr)
                        self.state = 128
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 129
                        self.match(craspParser.IF)
                        self.state = 130
                        self.bool_expr(0)
                        self.state = 131
                        self.match(craspParser.ELSE)
                        self.state = 132
                        self.count_expr(3)
                        pass

             
                self.state = 138
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.bool_expr_sempred
        self._predicates[3] = self.count_expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def bool_expr_sempred(self, localctx:Bool_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

    def count_expr_sempred(self, localctx:Count_exprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




