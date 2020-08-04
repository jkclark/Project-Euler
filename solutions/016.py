#!/usr/bin/python3
'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''

from helpers import print_memory_usage_report, print_time_elapsed
from time import time
import tracemalloc


def _sum_digits(num: int) -> int:
    sum_of_digits = 0
    while num > 0:
        sum_of_digits += num % 10
        num = num // 10

    return sum_of_digits


def main():
    # Keep track of time elapsed and memory used
    start_time = time()
    tracemalloc.start()

    # ********** Solution begins here ********** #

    sum_of_digits = _sum_digits(2 ** 1000)

    print(f'Sum of digits of 2^1000:\n\n\t{sum_of_digits}\n')

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
