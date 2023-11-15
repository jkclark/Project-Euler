#!/usr/bin/env python3
"""
Consider the fraction, , where and are positive integers. If and , it is called
a reduced proper fraction.

If we list the set of reduced proper fractions for in ascending order of size,
we get:

It can be seen that is the fraction immediately to the left of .

By listing the set of reduced proper fractions for in ascending order of size,
find the numerator of the fraction immediately to the left of .
"""
from collections import defaultdict
import math
from typing import Dict, Set

from helpers import measure_time_and_memory


@measure_time_and_memory
def main():
    """Find the numerator of the fraction immediately to the left of 3/7."""
    limit = 1_000_000
    nums_to_factors = get_factors_of_nums_up_to_limit(limit)
    max_fraction = 0
    corresponding_numerator = 0
    for denominator in range(limit, 1, -1):
        ## Find the first numerator to check
        numerator = denominator * (3 / 7)

        # If this denominator is divisible by 7, subtract 1
        if denominator % 7 == 0:
            numerator -= 1

        # Otherwise, go to the next integer down
        else:
            numerator = math.floor(numerator)

        ## Check numerators going down until we find first reduced proper fraction
        while numerator >= 1:
            # Compare factors to find HCF
            hcf = max(nums_to_factors[numerator] & nums_to_factors[denominator])

            # If HCF is not 1, go to next numerator
            if hcf != 1:
                numerator -= 1
                continue

            # If HCF is 1, and this is better than the previous best fraction,
            # set best fraction
            if numerator / denominator > max_fraction:
                max_fraction = numerator / denominator
                corresponding_numerator = numerator

            # No (numerator / denominator) will come closer to 3/7 than this one did,
            # so go to next denominator
            break

    print(
        f"The numerator of the fraction immediately to the left of 3/7:\
          \n\n\t{corresponding_numerator}\n"
    )


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
