#!/usr/bin/env python3
"""

"""
from collections import Counter
from math import log
import math
from typing import Iterable, List, Tuple

from helpers import measure_time_and_memory


@measure_time_and_memory
def main():
    print(f":\n\n\t{None}\n")


def H(n: int) -> int:
    """Find H(n)."""
    total = 0
    for num in range(2, n + 1):
        triples = find_triples(num)
        print(triples)
        for triple in triples:
            total += h(triple)

    return total


def find_triples(total: int) -> List[Tuple[int]]:
    """Find distinct triples that add to total."""
    triples = []
    for a in range(0, total + 1):
        for b in range(0, total + 1):
            for c in range(0, total + 1):
                if a + b + c == total:
                    triples.append(tuple([a, b, c]))

    return list(set(triples))


def h(bean_plates: Iterable[int]) -> int:
    """Find h(*bean_plates)"""
    sorted_plates = sorted(bean_plates, reverse=True)

    zeroes = Counter(bean_plates)[0]

    if zeroes == 0:
        return max(
            find_minimum_splits_for_beans(sorted_plates[0] + 1),
            find_minimum_splits_for_beans(sorted_plates[1]) + 2,
            find_minimum_splits_for_beans(sorted_plates[2]) + 2,
        )

    if zeroes == 1:
        return 1 + max(
            find_minimum_splits_for_beans(sorted_plates[0]),
            find_minimum_splits_for_beans(sorted_plates[1]),
        )

    if zeroes == 2:
        return find_minimum_splits_for_beans(sorted_plates[0])

    raise ValueError("No plates have beans!")


def find_minimum_splits_for_beans(beans: int) -> int:
    """Find the minimum number of splits needed to find the magic bean."""
    return math.ceil(log(beans, 2))


if __name__ == "__main__":
    h([1, 2, 3])
    main()
