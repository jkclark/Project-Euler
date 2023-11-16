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
from collections import defaultdict
from typing import Dict, Set

from helpers import measure_time_and_memory


@measure_time_and_memory
def main():
    """Find the number of elements in the set of reduced proper fractions for d <= 10^6."""
    limit = 1_000_000
    nums_to_factors = get_factors_of_nums_up_to_limit(limit)
    elements_count = 0
    for denominator in range(1, limit + 1):
        if denominator % 10_000 == 0:
            print(f"Doing denominator = {denominator}")

        # IDEA: Find all primes up to limit and short circuit for primes
        for numerator in range(1, denominator):
            # If HCF is 1, this will be an element in the set
            if max(nums_to_factors[numerator] & nums_to_factors[denominator]) == 1:
                elements_count += 1

    print(
        f"The number of elements in the set of reduced proper fractions for d <= 10^6:\
          \n\n\t{elements_count}\n"
    )


@measure_time_and_memory
def get_factors_of_nums_up_to_limit(limit: int) -> Dict[int, Set[int]]:
    """Get factors for all integers from 1 to limit, inclusive."""
    nums_to_factors = defaultdict(lambda: {1})
    for factor in range(2, limit + 1):
        num = factor
        while num <= limit:
            nums_to_factors[num].add(factor)
            num += factor

    return nums_to_factors


if __name__ == "__main__":
    main()
