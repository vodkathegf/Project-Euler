def sum_of_multiplies(limit):
    total = 0
    for number in range(limit):
        if number % 3 == 0 or number % 5 == 0:
            total += number
    return total

# I can also take limit as input, which would make it more dynamic
# but this is just project euler question


limit = 1000


result = sum_of_multiplies(limit)

print(f"the sum of all multiplies of 3 or 5 below {limit} is: {result}")
