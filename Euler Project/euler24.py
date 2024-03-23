from itertools import permutations


# def lexicographic_permutation():
#     digits = '0123456789'
#     perms = sorted(''.join(p) for p in permutations(digits))
#     millionth_permutation = perms[999999]
#     return millionth_permutation


# the result is 2783915460
# but I do not want to use itertools module
# so let's use a different approach

def generate_permutations(digits):
    if len(digits) == 1:
        return [digits]
    else:
        perms = []
        for i in range(len(digits)):
            current_digit = digits[i]
            remaining_digits = digits[:i] + digits[i+1:]
            for perm in generate_permutations(remaining_digits):
                perms.append([current_digit] + perm)
        return perms


def lexicographic_permutation():
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    perms = generate_permutations(digits)
    perms.sort()
    millionth_permutation = "".join(map(str, perms[999999]))
    return millionth_permutation

# it is not efficient, but I am just trying to show a different approach

result = lexicographic_permutation()
print(f"the result is : {result}")
