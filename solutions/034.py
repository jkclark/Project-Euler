#!/usr/bin/env python3
'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
'''

from helpers import print_memory_usage_report, print_time_elapsed
from time import time
import tracemalloc

from math import factorial


def main():
    # Keep track of time elapsed and memory used
    start_time = time()
    tracemalloc.start()

    # ********** Solution begins here ********** #

    '''
    If there exist two numbers with the same digits, it is impossible that they
    are both curious, since the sum of their digits cannot equal both of them.
    We could leverage this information to reduce the number of iterations, but
    this code solves the problem in 6 seconds on my Mac.
    '''
    sum_curious_numbers = 0
    for num in range(10, 1_000_000):
        sum_digits = 0
        for digit in str(num):
            sum_digits += factorial(int(digit))

        if sum_digits == num:
            sum_curious_numbers += num

    print(f'Sum of numbers which equal the sum of the factorial of their digits:\n\n\t{sum_curious_numbers}\n')

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
