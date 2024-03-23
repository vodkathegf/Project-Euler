# find the 10 001st prime number


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def prime_finder(limit):
    count = 0
    number = 1
    while count < limit:
        number += 1
        if is_prime(number):
            count += 1
        
    return number


limit = 10001

result = prime_finder(limit)

print(f"the 10001st prime number is : {result}")
