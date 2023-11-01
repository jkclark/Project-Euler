#!/usr/bin/env python3
"""

"""
from math import log
import math
from typing import List, Tuple

from helpers import measure_time_and_memory


@measure_time_and_memory
def main():
    print(f":\n\n\t{None}\n")


def find_triples(total: int) -> List[Tuple[int]]:
    """Find distinct triples that add to total."""
    triples = set()
    for a in range(1, total - 2):
        for b in range(a, total - 1):
            if a + b + 1 > total:
                break

            c = total - (a + b)
            triples.add(tuple(sorted([a, b, c])))

    return list(triples)


def h(bean_plates: List[int]) -> int:
    """Find h(*bean_plates)"""
    sorted_plates = sorted(bean_plates, reverse=True)
    return max(
        find_minimum_splits_for_beans(sorted_plates[0] + 1),
        find_minimum_splits_for_beans(sorted_plates[1]) + 2,
        find_minimum_splits_for_beans(sorted_plates[2]) + 2,
    )


def find_minimum_splits_for_beans(beans: int) -> int:
    """Find the minimum number of splits needed to find the magic bean."""
    return math.ceil(log(beans, 2))


if __name__ == "__main__":
    main()
