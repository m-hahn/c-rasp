from dataclasses import dataclass
from typing import Union



@dataclass
class Environment:
    tokens: list[str]
    vars: dict[str, Union[list[bool], list[int]]]

    def __init__(self, tokens):
        self.tokens = tokens
        self.vars = {}



class BoolExpr:
    def evaluate(self, env: Environment) -> list[bool]:
        pass


class CountExpr:
    def evaluate(self, env: Environment) -> list[int]:
        pass


# boolean expressions

@dataclass
class BoolLiteral(BoolExpr):
    value: bool

    def evaluate(self, env:Environment) -> list[bool]:
        return [self.value] * len(env.tokens)

@dataclass
class StringLiteral(BoolExpr):
    value: str

    def evaluate(self, env: Environment) -> list[bool]:
        return [tok == self.value for tok in env.tokens]

@dataclass
class BoolVariable(BoolExpr):
    name: str

    def evaluate(self, env: Environment) -> list[bool]:
        return env.vars[self.name]

@dataclass
class NotExpr(BoolExpr):
    expr: BoolExpr

    def evaluate(self, env: Environment) -> list[bool]:
        return [not x for x in self.expr.evaluate(env)]

@dataclass
class AndExpr(BoolExpr):
    left: BoolExpr
    right: BoolExpr

    def evaluate(self, env: Environment) -> list[bool]:
        return [a and b for a, b in zip(self.left.evaluate(env), self.right.evaluate(env))]

@dataclass
class Comparison(BoolExpr):
    left: CountExpr
    op: str  # '<' or '=='
    right: CountExpr

    def compare(self, val1: int, val2: int) -> bool:
        if self.op == "<":
            return val1 < val2
        else:
            return val1 == val2

    def evaluate(self, env: Environment) -> list[bool]:
        return [self.compare(val1, val2) for val1, val2 in zip(self.left.evaluate(env), self.right.evaluate(env))]



# count expressions

@dataclass
class CountLiteral(CountExpr):
    value: int

    def evaluate(self, env: Environment) -> list[int]:
        return [self.value] * len(env.tokens)


@dataclass
class CountVariable(CountExpr):
    name: str

    def evaluate(self, env: Environment) -> list[int]:
        return env.vars[self.name]

@dataclass
class Count(CountExpr):
    expr: BoolExpr

    def evaluate(self, env: Environment) -> list[int]:
        bools = self.expr.evaluate(env)
        count_of_trues = 0
        counts = []

        for i, val in enumerate(bools):
            if val:
                count_of_trues += 1
            counts.append(count_of_trues)

        return counts

@dataclass
class BinaryOp(CountExpr):
    left: CountExpr
    op: str  # '+' or '-'  or 'min' or 'max'

    right: CountExpr

    def combine(self, val1: int, val2: int) -> bool:
        if self.op == "+":
            return val1 + val2
        elif self.op == "-":
            return val1 - val2
        elif self.op == "min":
            return min(val1, val2)
        else:
            return max(val1, val2)

    def evaluate(self, env: Environment) -> list[int]:
        return [self.combine(val1, val2) for val1, val2 in zip(self.left.evaluate(env), self.right.evaluate(env))]

@dataclass
class IfExpr(CountExpr):
    then_branch: CountExpr
    condition: BoolExpr
    else_branch: CountExpr

    def evaluate(self, env: Environment) -> list[int]:
        condition_vals = self.condition.evaluate(env)
        then_vals = self.then_branch.evaluate(env)
        else_vals = self.else_branch.evaluate(env)

        ret = []
        for i in range(len(condition_vals)):
            if condition_vals[i]:
                ret.append(then_vals[i])
            else:
                ret.append(else_vals[i])

        return ret


## program

@dataclass
class Assignment:
    variable: str
    expression: Union[BoolExpr, CountExpr]

@dataclass
class Program:
    statements: list[Assignment]

    def execute(self, tokens, verbose=False) -> bool:
        env = Environment(tokens)
        most_recent_value = None

        for assignment in self.statements:
            val = assignment.expression.evaluate(env)
            env.vars[assignment.variable] = val
            most_recent_value = val

            if verbose:
                print(assignment.variable)
                print(val)
                print()

        return most_recent_value[-1]

