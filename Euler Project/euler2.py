# By considering the terms in the Fibonacci sequence whose values
# do not exceed four million, find the sum of the even-valued terms.

def fibonacci_sequence(limit):
    fiboSeq = [0, 1]
    while fiboSeq[-1] + fiboSeq[-2] < limit:
        next_term = fiboSeq[-1] + fiboSeq[-2]
        fiboSeq.append(next_term)

    return fiboSeq


def sum_even_valued_terms(sequence):
    total = 0
    for number in sequence:
        if number % 2 == 0:
            total += number
    return total


limit = 4e6
result = fibonacci_sequence(limit=limit)

total_result = sum_even_valued_terms(result)

print(
    f"Sum of the even-valued terms that do not exceed {limit} is : {total_result}")
