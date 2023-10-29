#!/usr/bin/env python3
"""
(Problem contained too many equations to be worth typing out)

How many, not necessarily distinct, values of nCr for 1 <= n <= 100, are greater than one-million?
"""

from typing import List
from helpers import measure_time_and_memory


@measure_time_and_memory
def main():
    """Calculate the number of values greater than 1,000,000."""
    limit = 100
    factorials = memoize_factorials(limit)
    values_over_one_million = 0
    for n in range(1, limit + 1):
        for r in range(1, n + 1):
            if choose(n, r, factorials) > 1_000_000:
                values_over_one_million += 1

    print(f"Number of values greater than 1,000,000:\n\n\t{values_over_one_million}\n")


def memoize_factorials(limit: int) -> List[int]:
    """Retrun a list of n! for 0 <= n <= limit."""
    factorials = [1]
    for num in range(1, limit + 1):
        factorials.append(factorials[-1] * num)

    return factorials


def choose(n: int, r: int, factorials: List[int]) -> int:
    """Calculate n choose r."""
    return factorials[n] / (factorials[r] * factorials[n - r])


if __name__ == "__main__":
    main()
