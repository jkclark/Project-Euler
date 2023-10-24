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


def get_len_consecutive_prime_sum_sequence(primes: List[int], target: int) -> int:
    """Get the length of the sequence of consecutive primes that sum to target."""
    running_total = primes[0]
    low = 0
    high = 23
    while (
        running_total != target
        and low <= high
        and low < len(primes)
        and high < len(primes)
    ):
        if running_total < target:
            high += 1
            running_total += primes[high]

        elif running_total > target:
            running_total -= primes[low]
            low += 1

    return high - low + 1 if running_total == target else 0


@measure_time_and_memory
def main():
    LIMIT = 1_000_000
    prime_or_not = [True for _ in range(LIMIT)]
    prime_or_not[0] = False
    prime_or_not[1] = False

    # Sieve of Eratosthenes
    for num in range(2, floor(sqrt(LIMIT)) + 1):
        if prime_or_not[num]:
            for multiple in range(num * num, LIMIT, num):
                prime_or_not[multiple] = False

    # Get a list of prime numbers < LIMIT
    primes = [number for number, is_prime in enumerate(prime_or_not) if is_prime]

    max_len_sequence = 0
    corresponding_max_prime = 2
    for prime_index, prime in enumerate(primes[170:]):
        if prime_index % 100 == 0:
            print(f"Doing {prime_index}th prime")

        sequence_len = get_len_consecutive_prime_sum_sequence(primes, prime)
        if sequence_len > max_len_sequence:
            max_len_sequence = sequence_len
            corresponding_max_prime = prime

    print(
        f"The prime below one million that can be written as the sum of the most consecutive primes:\n\n\t{corresponding_max_prime}\n"
    )


if __name__ == "__main__":
    main()
