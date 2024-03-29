#!/usr/bin/env python3
"""
Pentagonal numbers are generated by the formula, Pn=n(3n-1)/2. The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 - 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk - Pj| is minimised; what is the value of D?
"""

from typing import List
from helpers import print_memory_usage_report, print_time_elapsed
from time import time
import tracemalloc


def get_n_pentagonal_numbers(n: int) -> List[int]:
    """Get the first n pentagonal numbers."""
    return [num * (3 * num - 1) // 2 for num in range(1, n + 1)]


def is_pentagonal(num: int, pentagonal_numbers: List[int]) -> bool:
    return num in pentagonal_numbers


def main():
    # Keep track of time elapsed and memory used
    start_time = time()
    tracemalloc.start()

    # ********** Solution begins here ********** #

    LIMIT = 10_000
    pentagonal_numbers = get_n_pentagonal_numbers(LIMIT)

    for j in range(1, LIMIT):
        for k in range(j + 1, LIMIT):
            p_j = pentagonal_numbers[j]
            p_k = pentagonal_numbers[k]
            if is_pentagonal(p_j + p_k, pentagonal_numbers) and is_pentagonal(
                p_k - p_j, pentagonal_numbers
            ):
                print(
                    f"Minimized difference of pentagonal numbers whose sum/difference are pentagonal:\n\n\t{p_k - p_j}\n"
                )
                break

    # ********** Solution ends here ********** #

    # Stop tracking time and memory
    snapshot = tracemalloc.take_snapshot()
    end_time = time()
    tracemalloc.stop()

    # Print time elapsed and memory used
    print_time_elapsed(start_time, end_time)
    print_memory_usage_report(snapshot)


if __name__ == "__main__":
    main()
