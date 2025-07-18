

C_open = # "("
C_close = # ")"
V = C_open < C_close
CV = # V
M = (CV == 0)
B = (C_open == C_close)
D = M && B

