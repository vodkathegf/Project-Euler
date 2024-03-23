def longest_recurring_cycle(limit):
    max_cycle_length = 0
    number_with_max_cycle = 0

    for d in range(2, limit):
        remainders = {}
        remainder = 1 / d
        recurring_cycle_length = 0

        while remainder != 0 and remainder not in remainders:
            remainders[remainder] = len(remainders)
            remainder *= 10
            remainder %= d

        if remainder != 0:
            recurring_cycle_length = len(remainders) - remainders[remainder]

        if recurring_cycle_length > max_cycle_length:
            max_cycle_length = recurring_cycle_length
            number_with_max_cycle = d

    return number_with_max_cycle


limit = 1000
result = longest_recurring_cycle(limit)
print(
    f"the number with the longest recurring cycle within the limit of {limit} is : {result}")
