#!/usr/bin/env python3
"""
The cube, 41063625 (345)^3, can be permuted to produce two other cubes: 56623104 (384)^3
and 66430125 (405)^3. In fact, 41063625 is the smallest cube which has exactly three
permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""

from collections import defaultdict
import math
from typing import Tuple

from helpers import measure_time_and_memory


@measure_time_and_memory
def main():
    """Find the smallest cube for which exactly five permutations of its digits are cube."""
    num_digits = 1
    while True:
        # These are the smallest and largest numbers which we have to cube in order
        # to cover the range of all cubes with num_digits digits
        smallest_base = math.ceil((10 ** (num_digits - 1)) ** (1 / 3))
        biggest_base = math.floor(((10**num_digits) - 1) ** (1 / 3))

        # We can uniquely identify a set of digits by sorting them
        # We will store each number in a list with other numbers whose
        # cubes have the same digits
        digit_sets_to_cubes = defaultdict(list)
        for base in range(smallest_base, biggest_base + 1):
            cube = base**3
            digit_sets_to_cubes[get_digit_set(cube)].append(cube)

        # Keep track of the smallest cube to have this property
        smallest_cube = math.inf
        for cubes in digit_sets_to_cubes.values():
            if len(cubes) == 5:
                smallest_cube = min(smallest_cube, cubes[0])

        # If we found a number with this property, we're done
        if smallest_cube != math.inf:
            break

        num_digits += 1

    print(
        f"Smallest cube for which exactly five permutations of its digits are a cube:\
        \n\n\t{smallest_cube}\n"
    )


def get_digit_set(num: int) -> Tuple[int]:
    """Return a tuple containing num's digits, in increasing order."""
    return tuple(sorted(str(num)))


if __name__ == "__main__":
    main()

    x = {(1, 2, 3): 34}
