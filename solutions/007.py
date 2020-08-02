#!/usr/bin/python3
'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10001st prime number?
'''

from helpers import print_memory_usage_report, print_time_elapsed
from time import time
import tracemalloc

from math import floor, sqrt


def _is_prime(num: int) -> bool:
    if num <= 1:
        return False

    for potential_factor in range(2, floor(sqrt(num)) + 1):
        if num % potential_factor == 0:
            return False

    return True


def main():
    # Keep track of time elapsed and memory used
    start_time = time()
    tracemalloc.start()

    # ********** Solution begins here ********** #

    prime_count = 0
    candidate = 2
    while prime_count < 10001:
        if _is_prime(candidate):
            prime_count += 1
        candidate += 1

    # When the above loop terminates, we've added 1 to the number which was the 10,001st prime
    print(f'10,001st prime number:\n\n\t{candidate - 1}\n')

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
