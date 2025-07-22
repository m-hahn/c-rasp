
#import pred4

// count ones strictly to my left
num_ones_up_to_here = #"1"   // number of 1's to the left; relevant for input half
num_ones_here = (1 if "1" else 0)
num_ones_before_here = num_ones_up_to_here - num_ones_here // # ones strictly to my left

// make list [1, 0, ... 0]
token_count = #true
first_position = (token_count == 1)

// set carry if either first position, or all tokens to my left are ones
carry = (num_ones_before_here == token_count-1) || first_position

// determine incremented string
incremented_is_one = (carry || "1") && !(carry && "1") // XOR: False iff input and carry are both 1; relevant for input half
incremented_is_zero = !incremented_is_one
// NB (#[pred4] incremented_is_zero) > 0 is not the same as #[pred4] incremented_is_one == 0
// because #[pred4] is always false for first four positions

// check if output string matches incremented string
num_ones_match = #("1" && ((#[pred4] incremented_is_one) > 0))     // how many positions (in second half) are 1 and should be?
num_zeroes_match = #("0" && ((#[pred4] incremented_is_zero) > 0))  // same for zeroes
num_matches = num_ones_match + num_zeroes_match
copies_complete = (num_matches + num_matches == token_count)

