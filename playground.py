def reverse_string(x):
    # Reversing a string
    output = ""
    for c in x:
        output = c + output
    return output

print(reverse_string("hello"))

def reverse_string_2(x):
    output = [None] * len(x)
    idx = len(x)-1
    for c in x:
        output[idx] = c
        idx -= 1
    return ''.join(output)

print(reverse_string_2("hello"))
print(reverse_string_2(""))