
import sys
from program import *
from parser import parse_file

program : Program = parse_file(sys.argv[1])

tokens = "(()())"

print(program.execute(tokens, verbose=True))

