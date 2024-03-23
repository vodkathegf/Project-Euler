def get_sum_of_divisors(limit):
    memo = {}
    for n in range(1, limit):
        sumDivisors = 0
        for i in range(1, n):
            if n % i == 0:
                sumDivisors += i
        memo[n] = sumDivisors
    return memo


def is_abundant(n, sum_of_divisors):
    return sum_of_divisors[n] > n


def get_abundant_numbers(limit, sum_of_divisors):
    return [i for i in range(1, limit) if is_abundant(i, sum_of_divisors)]


def get_abundant_sums(abundant_numbers, limit):
    abundant_sums = set()
    for i in range(len(abundant_numbers)):
        for j in range(i, len(abundant_numbers)):
            x = abundant_numbers[i] + abundant_numbers[j]
            if x <= limit:
                abundant_sums.add(x)
            else:
                break
    return abundant_sums


def main(limit):
    sum_of_divisors = get_sum_of_divisors(limit)
    abundant_numbers = get_abundant_numbers(limit, sum_of_divisors)
    abundant_sums = get_abundant_sums(abundant_numbers, limit)
    total_sum = sum(range(1, limit + 1))
    non_abundant_sum = total_sum - sum(abundant_sums)
    return non_abundant_sum


limit = 28123
result = main(limit)

print(f"the result is : {result}")
