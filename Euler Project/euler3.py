# what is the largest prime factor of 600851475143

def largest_prime_factor(number):
    largest_factor = 1

    while number % 2 == 0:
        largest_factor = 2
        number //= 2

    factor1 = 3
    while factor1 * factor1 <= number:
        while number % factor1 == 0:
            largest_factor = factor1
            number //= factor1
        factor1 += 2

    if number > largest_factor:
        largest_factor = number

    return largest_factor


number = 600851475143

restult = largest_prime_factor(number)


print(f"the largest prime factor of {number} is : {restult}")
