import operator
import sys
import traceback
from dataclasses import dataclass, field
from typing import Union, Callable
import inspect

from tracing import Trace
import predefined

@dataclass
class Environment:
    tokens: list[str]
    vars: dict[str, Union[list[bool], list[int]]] = field(default_factory=dict)
    binary_functions: dict[str, Callable[[int, int], bool]] = field(default_factory=dict) # values have to evaluated at runtime


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
class BinaryBoolExpr(BoolExpr):
    left: BoolExpr
    op: str
    right: BoolExpr
    _op: Callable = field(init=False)

    def __post_init__(self):
        if self.op == 'and':
            self._op = lambda a, b: a and b
        else: # or
            self._op = lambda a, b: a or b

    def evaluate(self, env: Environment) -> list[bool]:
        return [self._op(a,b) for a, b in zip(self.left.evaluate(env), self.right.evaluate(env))]

_comparison_dict = {
    '==': operator.eq,
    '<': operator.lt,
    '>': operator.gt,
    '<=': operator.le,
    '>=': operator.ge
}

@dataclass
class Comparison(BoolExpr):
    left: CountExpr
    op: str  # '<' or '==' or '<=' or ...
    right: CountExpr
    _op: Callable  = field(init=False)

    def __post_init__(self):
        self._op = _comparison_dict[self.op]

    def evaluate(self, env: Environment) -> list[bool]:
        return [self._op(val1, val2) for val1, val2 in zip(self.left.evaluate(env), self.right.evaluate(env))]



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
class GuardedCount(CountExpr):
    guard: str
    expr: BoolExpr

    def evaluate(self, env: Environment) -> list[int]:
        bools: list[bool] = self.expr.evaluate(env) # value of expr at each position
        counts: list[int] = []

        guard_func = env.binary_functions[self.guard]

        for i, val in enumerate(bools):
            count_of_trues = 0

            for j in range(i+1):
                if bools[j] and guard_func(i, j):
                    count_of_trues += 1

            counts.append(count_of_trues)

        return counts


@dataclass
class BinaryOp(CountExpr):
    left: CountExpr
    op: str  # '+' or '-'  or 'min' or 'max'
    right: CountExpr
    _op: Callable  = field(init=False)

    def __post_init__(self):
        if self.op == '+':
            self._op = operator.add
        elif self.op == '-':
            self._op = operator.sub
        elif self.op == 'min':
            self._op = min
        else: # max
            self._op = max

    def combine(self, val1: int, val2: int) -> bool:
        return self._op(val1, val2)

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
    imports: list[str]

    def execute(self, tokens, verbose=False, tracing: Trace = None) -> bool:
        # initialize empty environment with the given tokens
        env = Environment(tokens)
        most_recent_value = None

        # import predefined functions
        for imp in self.imports:
            func = getattr(predefined, imp)
            params = list(inspect.signature(func).parameters.values())

            if len(params) == 1:
                # unary function - evaluate it on all input positions and store results as variables
                values = [func(i) for i in range(len(tokens))]
                env.vars[imp] = values
            elif len(params) == 2:
                # binary function - store function itself
                env.binary_functions[imp] = func

        # set up tracing
        if tracing is not None:
            tracing.accept_tokens(tokens)

        # execute program
        for i, assignment in enumerate(self.statements):
            try:

                val = assignment.expression.evaluate(env)
                env.vars[assignment.variable] = val
                most_recent_value = val

                if tracing is not None:
                    tracing.accept(assignment.variable, val)

                if verbose:
                    print(assignment.variable)
                    print(val)
                    print()

            except Exception as e:
                print(f"Exception in statement {i+1}:", file=sys.stderr)
                print(f"Statement: {assignment}", file=sys.stderr)
                traceback.print_exc()
                sys.exit(1)

        if tracing is not None:
            tracing.accept_result(most_recent_value[-1])

        return most_recent_value[-1]
