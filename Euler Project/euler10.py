# find the sum of all the primes below two million




def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def sum_primes(limit):
    total = 0
    for i in range(1, limit):
        if is_prime(i):
            total += i
    return total

limit = 2000000

result = sum_primes(limit)
print(f"the sum of all the primes below 2m is : {result}")
