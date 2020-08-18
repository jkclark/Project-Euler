#!/usr/bin/env python3
'''
The number, 197, is called a circular prime because all rotations of the digits:
197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

from helpers import print_memory_usage_report, print_time_elapsed
from time import time
import tracemalloc

from math import floor, sqrt


def main():
    # Keep track of time elapsed and memory used
    start_time = time()
    tracemalloc.start()

    # ********** Solution begins here ********** #

    LIMIT = 1_000_000
    prime_or_not = [True for _ in range(LIMIT)]
    prime_or_not[0] = False
    prime_or_not[1] = False

    # Sieve of Eratosthenes -- same solution as problem 10
    for num in range(2, floor(sqrt(LIMIT)) + 1):
        if prime_or_not[num]:
            for multiple in range(num * num, LIMIT, num):
                prime_or_not[multiple] = False

    # Check all rotations of every number, stopping for a number if a rotation isn't prime
    count_circular_primes = 0
    for num in range(LIMIT):
        num_string = str(num)
        for pivot in range(len(num_string)):
            if not prime_or_not[int(num_string[pivot:] + num_string[:pivot])]:
                break
        else:
            count_circular_primes += 1

    print(f'Number of circular primes below one million:\n\n\t{count_circular_primes}\n')

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
