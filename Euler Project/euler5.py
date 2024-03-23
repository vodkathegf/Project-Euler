# the smallest positive number evenly divisible every number from 1 to 20

def greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a


def least_common_multiple(a, b):
    return a * b // greatest_common_divisor(a, b)


def smallest_divisible_finder(limit):
    lcm_result = 1
    for i in range(1, limit+1):
        lcm_result = least_common_multiple(lcm_result, i)
    return lcm_result


result = smallest_divisible_finder(20)

print(f"the smallest positive number evenly divisible every number from 1 to 20: ", result)
