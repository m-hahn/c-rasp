
import sys
from program import *
from parser import parse_file

program : Program = parse_file(sys.argv[1])
for assignment in program.statements:
        print(assignment.variable)
        print(assignment.expression)
        print()
