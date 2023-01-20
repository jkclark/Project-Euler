#!/usr/bin/env python3
"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right,
and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from helpers import print_memory_usage_report, print_time_elapsed
from time import time
import tracemalloc

from math import floor, sqrt


prime_or_not = []


def get_primes_up_to_limit(limit: int):
    global prime_or_not

    prime_or_not = [True for _ in range(limit)]
    prime_or_not[0] = False
    prime_or_not[1] = False

    # Sieve of Eratosthenes
    for num in range(2, floor(sqrt(limit)) + 1):
        if prime_or_not[num]:
            for multiple in range(num * num, limit, num):
                prime_or_not[multiple] = False

    return prime_or_not


def truncate_left_to_right(num: int):
    """Return a given number with its leading digit removed, or 0 if given a 1-digit number."""
    if num < 10:
        return 0

    return int(str(num)[1:])


def truncate_right_to_left(num: int):
    """Return a given number with its trailing digit removed, or 0 if given a 1-digit number."""
    return num // 10


def truncate_num_in_direction(num: int, direction: str):
    return truncate_left_to_right(num) if direction == "ltr" else truncate_right_to_left(num)


def is_truncatable_in_direction(prime: int, direction: str):
    """Determine if a given prime is truncatable either left-to-right or vice-versa.

    NOTE: This function will erroneously return True for 2, 3, 5, and 7.

    direction (str): "ltr" - left to right
                     "rtl" - right to left
    """
    prime = truncate_num_in_direction(prime, direction)
    while prime > 0:
        if not prime_or_not[prime]:
            return False

        prime = truncate_num_in_direction(prime, direction)

    return True


def main():
    # Keep track of time elapsed and memory used
    start_time = time()
    tracemalloc.start()

    # ********** Solution begins here ********** #

    # Get all primes up to some number
    LIMIT = 1_000_000
    get_primes_up_to_limit(LIMIT)

    sum_of_truncatable_primes = 0
    # Iterate over primes, determining if they are truncatable
    for num, is_prime in enumerate(prime_or_not):
        if num < 11:  # Primes < 11 are not considered truncatable
            continue

        if is_prime and is_truncatable_in_direction(num, "ltr") and is_truncatable_in_direction(num, "rtl"):
            sum_of_truncatable_primes += num

    print(f"Sum of the 11 truncatable primes:\n\n\t{sum_of_truncatable_primes}\n")

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
