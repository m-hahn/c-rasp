

// C-RASP program for COUNT(3) = a^n b^n c^n
// (from Yang & Chiang 2024)

b_before_c = #("b" && (#"c" == 0)) == #"b"
a_before_bc = #("a" && (#("b" || "c") == 0)) == #"a"
same_counts = (#"a" == #"b") && (#"b" == #"c") && (#"c" == #"a")

count3 = b_before_c && a_before_bc && same_counts

