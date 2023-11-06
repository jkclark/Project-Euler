#!/usr/bin/env python3
"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""
from math import floor, sqrt
from typing import List

from helpers import measure_time_and_memory


@measure_time_and_memory
def main():
    """Find the prime less than 1M that can be written as the sum of the most consecutive primes.

    This function simply checks every (start_index, end_index) pair and checks if the sum is prime.
    There are some shortcuts taken to speed it up, but it's still O(n^2) (I think).
    """
    # Find primes up to 1,000,000
    primes_list = get_primes_up_to_limit(1_000_000)
    primes_set = set(primes_list)  # Useful for checking if a number is prime

    max_sequence_length = 0
    corresponding_prime = 0
    for start_index in range(len(primes_list)):
        # Start checking lists of at least length max_sequence_length
        for end_index in range(start_index + max_sequence_length, len(primes_list)):
            # start_index -> end_index, inclusive
            length = end_index - start_index + 1

            total = sum(primes_list[start_index : end_index + 1])

            # This "substring" of consecutive integers is already too big,
            # we can go to the next start_index
            if total > primes_list[-1]:
                break

            if total in primes_set:
                max_sequence_length = length
                corresponding_prime = total

    print(
        f"The prime < 1,000,000 that can be written as the sum of the most consecutive primes:\
          \n\n\t{corresponding_prime}\n"
    )


def get_primes_up_to_limit(limit: int) -> List[int]:
    """Find all primes < limit."""
    limit = 1_000_000
    prime_or_not = [True for _ in range(limit)]
    prime_or_not[0] = False
    prime_or_not[1] = False

    # Sieve of Eratosthenes
    for num in range(2, floor(sqrt(limit)) + 1):
        if prime_or_not[num]:
            for multiple in range(num * num, limit, num):
                prime_or_not[multiple] = False

    # Get a list of prime numbers < LIMIT
    return [number for number, is_prime in enumerate(prime_or_not) if is_prime]


if __name__ == "__main__":
    main()
