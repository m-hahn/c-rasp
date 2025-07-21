#import pred

C_follows_a = #[pred] "a"
P_follows_a = (C_follows_a >= 1)
P_ends_in_ab = "b" && P_follows_a
C_ab = #P_ends_in_ab
L = (C_ab >= 1)

