#!/usr/bin/env python3
"""
It can be seen that the number, 125874, and its double, 251748, contain exactly
the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain
the same digits.
"""

from collections import Counter
from helpers import measure_time_and_memory


@measure_time_and_memory
def main():
    """Find the smallest positive integer whose multiples contain the same digits."""
    candidate = 1
    while not multiples_contain_same_digits(candidate):
        candidate += 1

    print(
        f"The smallest positive integer whose multiples contain the same digits:\n\n\t{candidate}\n"
    )


def multiples_contain_same_digits(num: int) -> bool:
    """Return True if num's multiples contain the same digits, False otherwise."""
    digits = Counter(str(num))

    min_multiple = 2
    max_multiple = 6
    for multiple in range(min_multiple, max_multiple + 1):
        if Counter(str(num * multiple)) != digits:
            return False

    return True


if __name__ == "__main__":
    main()
