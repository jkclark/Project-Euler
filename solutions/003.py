#!/usr/bin/python3
'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
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

    largest_prime_factor = None
    GIVEN_NUMBER = 600851475143
    for potential_factor in range(floor(sqrt(GIVEN_NUMBER)) + 1, 1, -1):
        if GIVEN_NUMBER % potential_factor == 0 and _is_prime(potential_factor):
            largest_prime_factor = potential_factor
            break

    print(f'Largest prime factor of 600851475143:\n\n\t{largest_prime_factor}\n')

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
