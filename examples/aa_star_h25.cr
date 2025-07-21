
#import pos_even

C_not_a = # !"a"
A = (C_not_a == 0)
D = !pos_even && A

// It has to be !pos_even (rather than pos_even) because we count positions from zero,
// whereas Huang et al. count from one.



