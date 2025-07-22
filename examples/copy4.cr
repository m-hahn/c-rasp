
// COPY4 = COPY language for strings of length exactly 4 over alphabet {a, b, c}
// i.e. abcbabcb in COPY4, but abcabc not

#import pred4

is_a_copy = "a" && ((#[pred4] "a") == 1)
is_b_copy = "b" && ((#[pred4] "b") == 1)
is_c_copy = "c" && ((#[pred4] "c") == 1)

token_count = #true

num_copies = #is_a_copy + #is_b_copy + #is_c_copy
copies_complete = (2*num_copies == token_count)
