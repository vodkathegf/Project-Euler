words_of_numbers = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "onehundred",
    200: "twohundred",
    300: "threehundred",
    400: "fourhundred",
    500: "fivehundred",
    600: "sixhundred",
    700: "sevenhundred",
    800: "eighthundred",
    900: "ninehundred",
    1000: "onethoushand"
}


def number_to_words(number):
    if number in words_of_numbers:
        return words_of_numbers[number]

    elif number < 100:
        tens = (number // 10) * 10
        units = number % 10
        return words_of_numbers[tens] + words_of_numbers[units]

    elif number < 1000:
        hundreds = (number // 100) * 100
        remainder = number % 100
        if remainder == 0:
            return words_of_numbers[hundreds]
        else:
            return words_of_numbers[hundreds] + "and" + number_to_words(remainder)
    else:
        return words_of_numbers[1000]


result = sum(len(number_to_words(i)) for i in range(1, 1001))
print(f"the sum of the user letters : {result}")
