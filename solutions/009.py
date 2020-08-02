#!/usr/bin/python3
'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

from helpers import print_memory_usage_report, print_time_elapsed
from time import time
import tracemalloc

from math import sqrt


def main():
    # Keep track of time elapsed and memory used
    start_time = time()
    tracemalloc.start()

    # ********** Solution begins here ********** #

    for a in range(1, 1001):
        for b in range(1, 1001):
            c = sqrt(a ** 2 + b ** 2)
            if c == int(c) and a + b + c == 1000:
                product = int(a * b * c)
                break

    print(f'Product of Pythagorean triplet which sums to 1000:\n\n\t{product}\n')

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
