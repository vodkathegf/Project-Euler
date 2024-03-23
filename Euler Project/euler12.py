# the value of the first triangle number to have over 500 divisors

import math


def triangle_number(n):
    return (n * (n + 1) // 2)


def count_divisors(number):
    count = 0
    sqrt_num = math.isqrt(number)
    for i in range(1, sqrt_num + 1):
        if number % i == 0:
            count += 2
    if sqrt_num * sqrt_num == number:
        count -= 1
    return count


def find_number(number):
    num = 1
    while True:
        triangleNumber = triangle_number(num)
        if count_divisors(triangleNumber) > number:
            return triangleNumber
        num += 1


divisor_limit = 500

result = find_number(divisor_limit)

print(f"the first triangle number to have over 500 divisors : {result}")
