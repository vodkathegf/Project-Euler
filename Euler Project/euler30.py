# find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

def sum_of_digit_powers(number, power):
    return sum(int(digit) ** power for digit in str(number))

def find_digit_powers():
    result = 0
    number = 2
    while True:
        if number == sum_of_digit_powers(number,5):
            result += number
        number +=1
        if number > 999999:
            break
    return result

result = find_digit_powers()

print(f"the result is : {result}")