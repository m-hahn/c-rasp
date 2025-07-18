from dataclasses import dataclass
from typing import Union



class BoolExpr:
    pass


class CountExpr:
    pass


# boolean expressions

@dataclass
class BooleanLiteral:
    value: bool

@dataclass
class BoolLiteral(BoolExpr):
    value: bool

@dataclass
class StringLiteral(BoolExpr):
    value: str

@dataclass
class BoolVariable(BoolExpr):
    name: str

@dataclass
class NotExpr(BoolExpr):
    expr: BoolExpr

@dataclass
class AndExpr(BoolExpr):
    left: BoolExpr
    right: BoolExpr

@dataclass
class Comparison(BoolExpr):
    left: CountExpr
    op: str  # '<' or '=='
    right: CountExpr


# count expressions


@dataclass
class CountLiteral(CountExpr):
    value: int

@dataclass
class CountVariable(CountExpr):
    name: str

@dataclass
class Count(CountExpr):
    expr: BoolExpr

@dataclass
class BinaryOp(CountExpr):
    left: CountExpr
    op: str  # '+' or '-'
    right: CountExpr

@dataclass
class IfExpr(CountExpr):
    then_branch: CountExpr
    condition: BoolExpr
    else_branch: CountExpr

@dataclass
class MinMaxCall(CountExpr):
    op: str  # 'min' or 'max'
    left: CountExpr
    right: CountExpr



## program

@dataclass
class Assignment:
    variable: str
    expression: Union[BoolExpr, CountExpr]

@dataclass
class Program:
    statements: list[Assignment]

