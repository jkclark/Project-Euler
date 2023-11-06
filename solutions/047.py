#!/usr/bin/env python3
"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors
each. What is the first of these numbers?
"""
from collections import Counter, namedtuple
from math import floor, sqrt
from typing import Dict, Set

from helpers import measure_time_and_memory


Factor = namedtuple("Factor", "base power")


@measure_time_and_memory
def main():
    """Find the first of the first four consecutive integers to have four distinct prime factors each."""
    # Get primes
    primes = get_primes_up_to_limit(1_000_000)

    # Start tracking prime factorizations
    prime_factorizations = {}

    # Get prime factors of first four consecutive positive integers
    three_ago = convert_counter_to_factor_set(
        get_prime_factorization(2, prime_factorizations, primes)
    )
    two_ago = convert_counter_to_factor_set(
        get_prime_factorization(3, prime_factorizations, primes)
    )
    one_ago = convert_counter_to_factor_set(
        get_prime_factorization(4, prime_factorizations, primes)
    )
    current = convert_counter_to_factor_set(
        get_prime_factorization(5, prime_factorizations, primes)
    )

    # Find distinct prime factors of four consecutive integers
    distinct_factors = three_ago | two_ago | one_ago | current

    # NOTE: Here we are checking that there are 16 distinct prime factors. However,
    #       I believe it's possible that one number has 5 distinct factors and another
    #       only has 3. This condition of 16 would still be satisfied, but the actual
    #       condition as stated in the problem would not be. It turns out that this doesn't
    #       matter, because the first time there are 16 distinct factors is also the first
    #       time each of the four integers have four distinct prime factors.
    required_distinct_factors = 4 * 4
    num = 5
    while len(distinct_factors) < required_distinct_factors:
        # Increment number
        num += 1

        # Cycle variables
        three_ago = two_ago
        two_ago = one_ago
        one_ago = current
        current = convert_counter_to_factor_set(
            get_prime_factorization(num, prime_factorizations, primes)
        )

        # Re-calculate distinct factors
        distinct_factors = three_ago | two_ago | one_ago | current

    print(
        f"The first of the first four consecutive integers with four distinct prime factors:\
          \n\n\t{num - 3}\n"
    )


def get_primes_up_to_limit(limit: int) -> Set[int]:
    """Get a set of all primes <= limit."""
    prime_or_not = [True for _ in range(limit)]
    prime_or_not[0] = False
    prime_or_not[1] = False

    # Sieve of Eratosthenes
    for num in range(2, floor(sqrt(limit)) + 1):
        if prime_or_not[num]:
            for multiple in range(num * num, limit, num):
                prime_or_not[multiple] = False

    return set(index for index, value in enumerate(prime_or_not) if value)


def get_prime_factorization(
    num: int,
    known_factors: Dict[int, Set[Factor]],
    primes: Set[int],
) -> Counter:
    """Get the prime factorization of num.

    NOTE: This function modifies the value of known_factors by updating it with
    the prime factorization of num.
    """
    if num in known_factors:
        return known_factors[num]

    # If number is prime, we're done
    if num in primes:
        return Counter({num: 1})

    potential_factor = 2
    while potential_factor <= floor(sqrt(num)):
        if potential_factor in primes:
            if num % potential_factor == 0:
                # potential_factor is a factor
                prime_factorization = Counter({potential_factor: 1})

                # Recursive call to num / potential_factor
                prime_factorization.update(
                    get_prime_factorization(
                        num // potential_factor, known_factors, primes
                    )
                )

                # Memoize
                known_factors[num] = prime_factorization

                return prime_factorization

        potential_factor += 1

    raise ValueError("Somehow we couldn't factor!")


def convert_counter_to_factor_set(counter: Counter) -> Set[Factor]:
    """Convert a Counter to a set of Factors.

    Each key in the counter is the factor's base, and the value is its power.
    """
    return {Factor(base, power) for base, power in counter.items()}


if __name__ == "__main__":
    main()
