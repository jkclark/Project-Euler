#!/usr/bin/env python3
""""""

from collections import defaultdict
from math import floor, sqrt
from typing import Tuple
from helpers import measure_time_and_memory


{(1, 1, 2, 3): [1123, 3211, 3121]}


@measure_time_and_memory
def main():
    """Find the 12-digit number do you form by concatenating the three terms in this sequence."""
    LIMIT = 10_000
    prime_or_not = [True for _ in range(LIMIT)]
    prime_or_not[0] = False
    prime_or_not[1] = False
    for num in range(2, floor(sqrt(LIMIT)) + 1):
        if prime_or_not[num]:
            for multiple in range(num * num, LIMIT, num):
                prime_or_not[multiple] = False

    primes = [number for number, is_prime in enumerate(prime_or_not) if is_prime]

    digits_to_primes = defaultdict(list)
    for prime in primes:
        if prime < 1000:
            continue

        digits = get_sorted_digits(prime)
        digits_to_primes[digits].append(prime)

    digits_to_primes = {
        digits: primes
        for digits, primes in digits_to_primes.items()
        if len(primes) >= 3
    }

    answer_primes = []
    for primes in digits_to_primes.values():
        for low in range(len(primes) - 2):
            for high in range(low + 2, len(primes)):
                average = (primes[high] + primes[low]) / 2
                if average in primes:
                    answer_primes = [primes[low], int(average), primes[high]]
                    break

    print(f"12-digit number:\n\n\t{answer_primes}\n")


def get_sorted_digits(num: int) -> Tuple[int]:
    """Get num's digits sorted in increasing order."""
    return tuple(sorted(int(digit) for digit in str(num)))


if __name__ == "__main__":
    main()
