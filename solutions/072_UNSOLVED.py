#!/usr/bin/env python3
"""
Consider the fraction,  , where and are positive integers. If and , it is called
a reduced proper fraction.

If we list the set of reduced proper fractions for in ascending order of size,
we get:

It can be seen that there are elements in this set.

How many elements would be contained in the set of reduced proper fractions for
?
"""
from collections import Counter, namedtuple
import math
from typing import Dict, Set

from helpers import measure_time_and_memory


@measure_time_and_memory
def main():
    """Find the number of elements in the set of reduced proper fractions for d <= 10^6."""
    limit = 1_000_000
    primes = get_primes_up_to_limit(limit)
    prime_factorizations = get_distinct_prime_factors_of_nums_up_to_limit(limit, primes)
    nums_to_multiples = get_multiples_of_nums_up_to_limit(primes, limit)
    elements_count = limit - 1  # Count all of the (1/d)'s (limit / limit is invalid)

    for numerator in range(2, limit):  # limit will never be a numerator
        if numerator % 10_000 == 0:
            print(f"Doing numerator = {numerator}")

        # Consider the total number of possible denominators for this numerator
        # (All numbers less than numerator cannot be a denominator)
        num_denominators = limit - numerator

        # Find all distinct multiples of prime factors of this numerator
        # NOTE: I think the problem is that there are 500,000 multiples of 2,
        #       333,333 multiples of 3, etc. I tried using the smallest factor's multiples
        #       as the "base set" for the union ("set()" below), but that didn't signifcantly
        #       decrease the runtime.
        multiples_of_prime_factors = set().union(
            *[nums_to_multiples[factor] for factor in prime_factorizations[numerator]]
        )

        # None of the multiples of prime factors can be denominators for this numerator
        # Filter out the multiples which are <= numerator
        # NOTE: Even without this filter we are far too slow
        valid_multiples = {
            multiple for multiple in multiples_of_prime_factors if multiple > numerator
        }
        num_denominators -= len(valid_multiples)

        # Add to total (numerator / denominator) count
        elements_count += num_denominators

    print(
        f"The number of elements in the set of reduced proper fractions for d <= 10^6:\
          \n\n\t{elements_count}\n"
    )


def get_primes_up_to_limit(limit: int) -> Set[int]:
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


def get_multiples_of_nums_up_to_limit(nums: Set[int], limit) -> Dict[int, Set[int]]:
    """Get multiples of all integers from 1 to limit, inclusive."""
    nums_to_multiples = {}
    for base in nums:
        nums_to_multiples[base] = set()
        multiple = base
        while multiple <= limit:
            nums_to_multiples[base].add(multiple)
            multiple += base

    return nums_to_multiples


def get_distinct_prime_factors_of_nums_up_to_limit(
    limit: int, primes: Set[int]
) -> Dict[int, Set[int]]:
    """Get the distinct prime factors of each integer from 1 to the given limit.

    Args:
        limit: The highest integer for which prime factors will be found
        primes: All prime numbers <= limit

    Example: 12 = 2 * 2 * 3 -- this function will return {2, 3}
    """

    Factor = namedtuple("Factor", "base power")

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
        while potential_factor <= math.floor(math.sqrt(num)):
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

    prime_factorizations = {}
    for num in range(2, limit + 1):
        # If num is prime, its prime factorization is itself
        # and we need to add it to the dict
        if num in primes:
            prime_factorizations[num] = {num: 1}

        # NOTE: This function call modifies prime_factorizations
        get_prime_factorization(num, prime_factorizations, primes)

    distinct_prime_factors = {}
    for num, prime_factors in prime_factorizations.items():
        distinct_prime_factors[num] = set(prime_factors.keys())

    return distinct_prime_factors


if __name__ == "__main__":
    main()
