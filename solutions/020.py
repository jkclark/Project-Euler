#!/usr/bin/python3
'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
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

    sum_digits = sum([int(digit) for digit in str(factorial(100))])

    print(f'Sum of the digits of 100!:\n\n\t{sum_digits}\n')

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
