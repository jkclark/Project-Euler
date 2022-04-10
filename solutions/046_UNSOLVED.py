#!/usr/bin/env python3
'''
It was proposed by Christian Goldbach that every odd composite number can be written
as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
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

    LIMIT = 10_000_000
    prime_or_not = [True for _ in range(LIMIT)]
    prime_or_not[0] = False
    prime_or_not[1] = False

    # Sieve of Eratosthenes
    for num in range(2, floor(sqrt(LIMIT)) + 1):
        if prime_or_not[num]:
            for multiple in range(num * num, LIMIT, num):
                prime_or_not[multiple] = False

    # Get a list of prime numbers < LIMIT
    primes = []
    odd_composites = []
    for number, is_prime in enumerate(prime_or_not[2:]):
        if is_prime:
            primes.append(number + 2)
        else:
            if number % 2 == 1:
                odd_composites.append(number + 2)

    smallest_qualifying = None
    for odd_composite in odd_composites[500_000:]:
        for prime in primes:
            if prime >= odd_composite:
                break
            if sqrt((odd_composite - prime) / 2).is_integer():
                break
        else:
            smallest_qualifying = odd_composite
            break

    print(f'Smallest odd composite that cannot be written as a prime + twice a square:\n\n\t{smallest_qualifying}\n')

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
