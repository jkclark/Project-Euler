#!/usr/bin/env python3
"""
Starting with 1 and spiralling anticlockwise in the following way, a square
spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right
diagonal, but what is more interesting is that 8 out of the 13 numbers lying
along both diagonals are prime; that is, a ratio of 8/13 ~=~ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral
with side length 9 will be formed. If this process is continued, what is the
side length of the square spiral for which the ratio of primes along both
diagonals first falls below 10%?
"""
import math
from typing import Set

from helpers import measure_time_and_memory


@measure_time_and_memory
def main():
    """Find the first side length for which the ratio falls below 10%

    NOTE: This takes ~22 minutes and ~10 kilobytes when getting primes up to 1 billion.
    """
    current_num = 1
    side_length = 3
    all_primes = get_primes_less_than_limit(1_000_000_000)
    max_prime = max(all_primes)
    prime_diagonal_count = 0
    total_diagonal_count = 0
    ratio = math.inf
    while ratio > 0.10:
        if current_num % 100 == 0:
            print(f"Doing num {current_num}")

        if current_num > max_prime:
            raise ValueError

        # Check each diagonal (of which there are 4 per side length)
        for _ in range(4):
            current_num += side_length - 1
            total_diagonal_count += 1
            if current_num in all_primes:
                prime_diagonal_count += 1

        ratio = prime_diagonal_count / total_diagonal_count

        side_length += 2

    print(f"The first side length with a ratio < 10%:\n\n\t{side_length - 2}\n")


def get_primes_less_than_limit(limit: int) -> Set[int]:
    """Return a list of primes less than a given limit."""
    prime_or_not = [True for _ in range(limit)]
    prime_or_not[0] = False
    prime_or_not[1] = False

    # Sieve of Eratosthenes
    for num in range(2, math.floor(math.sqrt(limit)) + 1):
        if prime_or_not[num]:
            for multiple in range(num * num, limit, num):
                prime_or_not[multiple] = False

    return {number for number, is_prime in enumerate(prime_or_not) if is_prime}


if __name__ == "__main__":
    main()
