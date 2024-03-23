# digit-sum of 100!

# let's define the factorial function without using math module

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
# now we need a sum function
    
def digit_sum():
    factorial_funct = str(factorial(100))
    total = 0
    for i in factorial_funct:
        total += int(i)
    return total

sum_digit = digit_sum()

print(f"the result is : {sum_digit}")
    
