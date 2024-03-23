# class QuadraticPrimesSolver:
#     def __init__(self):
#         pass

#     def is_prime(self, number):
#         if number < 2:
#             return False
#         for i in range(2, int(number ** 0.5) + 1):
#             if number % i == 0:
#                 return False
#         return True

#     def generate_primes(self, limit):
#         primes = []
#         for num in range(2, limit):
#             if self.is_prime(num):
#                 primes.append(num)
#         return primes

#     def count_consecutive_primes(self, a, b, primes):
#         n = 0
#         while True:
#             number = n ** 2 + a * n + b
#             if number not in primes:
#                 break
#             n += 1
#         return n

#     def max_cons_primes(self, prime_numbers, primes):
#         max_consecutive_primes = 0
#         best_coefficients = None

#         for b in prime_numbers:
#             for a in range(-999, 1000):
#                 consecutive_primes = self.count_consecutive_primes(
#                     a, b, primes)
#                 if consecutive_primes > max_consecutive_primes:
#                     max_consecutive_primes = consecutive_primes
#                     best_coefficients = (a, b)

#         return best_coefficients, max_consecutive_primes


# solver = QuadraticPrimesSolver()
# primes = solver.generate_primes(1000)
# prime_numbers = [num for num in primes if num <= 1000]
# best_coefficients, max_consecutive_primes = solver.max_cons_primes(
#     prime_numbers, primes)
# print("Best coefficients:", best_coefficients)
# print("Maximum consecutive primes:", max_consecutive_primes)



# THIS IS THE MOST DIFFICULT QUESTION UP TO NOW

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def generate_primes(limit):
    primes = []
    for number in range(2, limit):
        if is_prime(number):
            primes.append(number)
    return primes

def count_consecutive_primes(a, b, primes):
    n = 0
    while True:
        number = n ** 2 + a * n + b
        if number not in primes:
            break
        n += 1
    return n

def max_cons_primes(a_range, b_range):
    max_consecutive_primes = 0
    best_coefficients = None
    primes = generate_primes(b_range[-1])  
    
    for a in range(a_range[0], a_range[1] + 1):
        for b in range(b_range[0], b_range[1] + 1):
            consecutive_primes = count_consecutive_primes(a, b, primes)

            if consecutive_primes > max_consecutive_primes:
                max_consecutive_primes = consecutive_primes
                best_coefficients = (a, b)

    return best_coefficients

best_coefficients = max_cons_primes((-1000, 1000), (-1000, 1000))
product = best_coefficients[0] * best_coefficients[1]
print("Best coefficients:", best_coefficients)
print("Product of coefficients:", product)
