
# Implement unary and binary predicates as Python functions in this file.

# For the binary predicates, i and j are as in Huang et al. 2025:
# i is the position at which we're evaluating #[predicate], and j is the position to the left
# at which we're evaluating the nested expression.

# You can define predicates as you wish. Huang et al. 2025 are focused
# on binary predicates that are translation-invariant and local and on unary predicates
# that are periodic. Such C-RASP programs can be compiled into length-generalizing
# limit transformers.

# All input positions are zero-based.


def pred(i: int, j: int) -> bool:
    return j == i-1


def pos_even(i: int) -> bool:
    return i%2 == 0

