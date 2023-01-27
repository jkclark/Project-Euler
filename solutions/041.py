#!/usr/bin/env python3
"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

from helpers import print_memory_usage_report, print_time_elapsed
from time import time
import tracemalloc

from itertools import permutations
from math import floor, sqrt


def create_num_from_iterable(iterable):
    num = 0
    for digit in iterable:
        num *= 10
        num += digit

    return num


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

    digits = [1, 2, 3, 4]
    biggest_pandigital_prime = 0

    for digit in range(5, 10):
        digits.append(digit)
        for perm in permutations(digits):
            num = create_num_from_iterable(perm)
            if _is_prime(num):
                biggest_pandigital_prime = num

    print(f"Largest n-digit pandigital prime that exists:\n\n\t{biggest_pandigital_prime}\n")

    # ********** Solution ends here ********** #

    # Stop tracking time and memory
    snapshot = tracemalloc.take_snapshot()
    end_time = time()
    tracemalloc.stop()

    # Print time elapsed and memory used
    print_time_elapsed(start_time, end_time)
    print_memory_usage_report(snapshot)


if __name__ == "__main__":
    main()
