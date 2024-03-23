# power digit sum 2 ** 1000

def power_calculator(n):
    return 2 ** n


def digit_sum(number):
    power_result = power_calculator(number)
    digits_str = str(power_result)
    total = sum(int(digit) for digit in digits_str )
    return total


number = 1000

result = digit_sum(number)

print(f"2 ** 1000 sum of its digits : {result}")