#!/usr/bin/python3
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from helpers import print_memory_usage_report, print_time_elapsed
from time import time
import tracemalloc

from math import floor, sqrt


def main():
    # Keep track of time elapsed and memory used
    start_time = time()
    tracemalloc.start()

    # ********** Solution begins here ********** #

    LIMIT = 2_000_000
    prime_or_not = [True for _ in range(LIMIT)]
    prime_or_not[0] = False
    prime_or_not[1] = False

    # Sieve of Eratosthenes
    for num in range(2, floor(sqrt(LIMIT)) + 1):
        if prime_or_not[num]:
            for multiple in range(num * num, LIMIT, num):
                prime_or_not[multiple] = False

    # Add up the value of each prime
    sum_of_primes = sum(index for index, value in enumerate(prime_or_not) if value)

    print(f"Sum of primes below two million:\n\n\t{sum_of_primes}\n")

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
