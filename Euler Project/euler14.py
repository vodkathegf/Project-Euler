# find starting number, under one million, produces the longest chain

def collatz_sequence(n, memo):
    if n in memo:
        return memo[n]
    
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
        if n in memo:
            sequence_length = len(sequence) + memo[n]
            memo[sequence[0]] = sequence_length
            return sequence_length
    memo[sequence[0]] = len(sequence)
    return len(sequence)

def find_starting_number(limit):
    max_length = 0
    starting_number = 0
    memo = {}

    for number in range(1, limit):
        sequence_length = collatz_sequence(number, memo)
        if sequence_length > max_length:
            max_length = sequence_length
            starting_number = number
    
    return starting_number

limit = 1000000
result = find_starting_number(limit)
print(f"The starting number under {limit} producing the longest chain is: {result}")
