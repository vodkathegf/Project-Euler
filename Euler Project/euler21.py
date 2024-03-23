
def sum_divisors(n):
    divisor_sum = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisor_sum += i
            if i != n // i:
                divisor_sum += n//i
    return divisor_sum



def find_amicable_numbers(limit):
    amicable_pairs = []
    for i in range(2, limit):
        x = sum_divisors(i)
        if x != i and sum_divisors(x) == i:
            amicable_pairs.append((i, x))
    return amicable_pairs


def sum_amicable_numbers():
    total = 0
    amicable_pairs = find_amicable_numbers(limit)
    for pair in amicable_pairs:
        for number in pair:
            total += number
    return total // 2




limit = 10000

result = sum_amicable_numbers()

print(result)