def fibonacci_sequence():
    fib_seq = [0, 1]
    yield 0
    yield 1
    while True:
        next_term = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_term)
        yield next_term


def find_index_of_n_digit_sequence(n):
    fib_gen = fibonacci_sequence()
    index = -1
    while True:
        term = next(fib_gen)
        index += 1
        if len(str(term)) == n:
            return index


nth_index = 1000
result = find_index_of_n_digit_sequence(nth_index)
print(f"The index of the first term containing {nth_index} digits is : {result}")
