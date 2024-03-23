# find the largest palindrome made from the product of two 3-digit numbers

def is_palindrome(number):

    return str(number) == str(number)[::-1]


def largest_product():
    max_palindrome = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j

            if is_palindrome(product) and product > max_palindrome:
                max_palindrome = product
    return max_palindrome


largest_palindrome = largest_product()

print(
    f"the largest palindrome made from the product of two 3-digit numbers is : {largest_palindrome}")
