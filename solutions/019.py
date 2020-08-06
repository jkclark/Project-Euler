#!/usr/bin/python3
'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.

Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

from helpers import print_memory_usage_report, print_time_elapsed
from time import time
import tracemalloc


def main():
    # Keep track of time elapsed and memory used
    start_time = time()
    tracemalloc.start()

    # ********** Solution begins here ********** #

    DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    day = month = 1
    day_of_the_week = 2  # 0 = Sunday, 1 = Monday, 2 = Tuesday = 01/01/1901
    year = 1901

    sundays_on_day_1 = 0

    while year < 2001:
        # Check if day/month/year is a Sunday on the first of the month
        if day == 1 and day_of_the_week == 0:
            sundays_on_day_1 += 1

        # Increment the day by one
        day += 1
        day_of_the_week = (day_of_the_week + 1) % 7

        # Check if day/month/year is a leap day
        # NOTE: Since this problem only asks for the dates between 1901 and 2000,
        #       we don't actually need to check the century-year rule for leap years.
        #       Checking if the year is divisible by 4 would suffice.
        leap_day = (
            day == 29
            and month == 2
            and year % 4 == 0
            and (not year % 100 == 0 or year % 400 == 0)
        )

        # If this is a leap day, don't do the normal check for moving past the
        # end of the month/year
        if leap_day:
            continue

        # If we've gone past the last day of the month, set day to 1 and increment month
        if day > DAYS_IN_MONTH[month - 1]:
            day = 1
            month += 1

            # If we've gone past the last month of the year
            if month == 13:
                month = 1
                year += 1

    print(f'Sundays that fell on the first of the month in the twentieth century:\n\n\t{sundays_on_day_1}\n')

    # ********** Solution ends here ********** #

    # Stop tracking time and memory
    snapshot = tracemalloc.take_snapshot()
    end_time = time()
    tracemalloc.stop()

    # Print time elapsed and memory used
    print_time_elapsed(start_time, end_time)
    print_memory_usage_report(snapshot)


if __name__ == '__main__':
    main()
