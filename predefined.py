

# All input positions are zero-based.
# For the binary predicates, i and j are as in Huang et al. 2025:
# i is the position at which we're evaluating #[predicate], and j is the position to the left
# at which we're evaluating the nested expression.

def pred(i: int, j: int) -> bool:
    return j == i-1

