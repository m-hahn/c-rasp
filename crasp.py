
import sys
from program import *
from parser import parse_file
from tracing import TraceToFile, TraceToHTML

program : Program = parse_file(sys.argv[1])

tokens = "(()())"

with TraceToHTML("trace.html") as tr:
    print(program.execute(tokens, tracing=tr))

