# find_missing
# arg1 array of unique numbers
# arg2 same array of unique numbers but with on number missing
# return missing number

def find_missing(full_set, partial_set):
    set_full = set(full_set)
    set_partial = set(partial_set)
    missing = set_full - set_partial
    assert(len(missing) == 1)
    return list(missing)[0]

print(find_missing([1,2,3,4,5], [2,3,4,5]))

def find_missing_xor(full_step, partial_set):
    xor_sum = 0
    for num in full_step:
        xor_sum ^= num
    for num in partial_set:
        xor_sum ^= num
    return xor_sum

print(find_missing_xor([1,2,3,4,5], [2,3,4,5]))