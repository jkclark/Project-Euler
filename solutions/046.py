#!/usr/bin/env python3
"""
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
"""

from math import floor, sqrt
from typing import List

from helpers import measure_time_and_memory


@measure_time_and_memory
def main():
    LIMIT = 500_000
    primes = set(get_primes_less_than_limit(LIMIT))
    twice_squares = [2 * num**2 for num in range(1, floor(sqrt(LIMIT)))]

    smallest_qualifying = None
    for odd_num in range(3, LIMIT, 2):
        # Only consider composite numbers
        if odd_num in primes:
            continue

        # TODO: Stop once twice_squares is greater than odd_num
        for twice_square in twice_squares:
            # If we find a way to express this number as a prime + twice a square, we can stop
            if odd_num - twice_square in primes:
                break

        # If we don't find a way to express it, then we've found our answer
        else:
            smallest_qualifying = odd_num
            break

    print(
        f"Smallest odd composite that cannot be written as a prime + twice a square:\n\n\t{smallest_qualifying}\n"
    )


def get_primes_less_than_limit(limit: int) -> List[int]:
    """Return a list of primes less than a given limit."""
    prime_or_not = [True for _ in range(limit)]
    prime_or_not[0] = False
    prime_or_not[1] = False

    # Sieve of Eratosthenes
    for num in range(2, floor(sqrt(limit)) + 1):
        if prime_or_not[num]:
            for multiple in range(num * num, limit, num):
                prime_or_not[multiple] = False

    return [number for number, is_prime in enumerate(prime_or_not) if is_prime]


if __name__ == "__main__":
    main()
