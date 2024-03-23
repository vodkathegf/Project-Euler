# counting sundays from 1 jan 1901 to 31 dec 2000
# "A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400"
# 1 jan 1901 tuesday

# let's just approach it with more basic way (datetime)

# import datetime


# def count_sundays():
#     sunday_count = 0
#     for year in range(1901, 2001):  # years from 1901 to 2001
#         for month in range(1, 13):
#             if datetime.date(year, month, 1).weekday() == 6:
#                 sunday_count += 1
#     return sunday_count


# but let's just go with the hard way

weekdays = {
    1: "monday",
    2: "tuesday",
    3: "wednesday",
    4: "thursday",
    5: "friday",
    6: "saturday",
    7: "sunday"
}


def count_sundays():
    sunday_count = 0
    for year in range(1901,2001):
        for month in range(1,13):
            #let's implement Zeller's Congruence formula here
            if month < 3:
                month +=12
                year -= 1
            day_of_week = (1 + (13 * (month + 1)) // 5 + year + year // 4 - year // 100 + year // 400) % 7
            day_of_week = (day_of_week + 5) % 7
            # although sunday seems to correspond to 7th element, it is actually 0th index in our weekdays dictionary
            if day_of_week == 0:
                sunday_count += 1
    return sunday_count


result = count_sundays()
print(f"number of sundays between the given dates is {result}")
