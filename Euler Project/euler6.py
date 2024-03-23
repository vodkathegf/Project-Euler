# find the difference between the sum of the squares of
# the first one hundred natural numbers and the square of the sum

def sum_of_squares(limit):
    total = 0
    for i in range(1, limit+1):
        total += i ** 2

    return total


def squares_of_sum(limit):
    total = 0
    for i in range(1, limit + 1):
        total += i
    return total ** 2


def difference_calculator(x, y):
    return abs(x - y)


limit = 100

result_sumsquare = sum_of_squares(limit)
result_squaresum = squares_of_sum(limit)

result_difference = difference_calculator(result_squaresum, result_sumsquare)

print(
    f"the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is :",
    result_difference)
