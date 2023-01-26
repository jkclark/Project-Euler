#!/usr/bin/env python3
"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of
the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

from helpers import print_memory_usage_report, print_time_elapsed
from time import time
import tracemalloc

from itertools import permutations


def main():
    # Keep track of time elapsed and memory used
    start_time = time()
    tracemalloc.start()

    # ********** Solution begins here ********** #
    digits = [digit for digit in range(10)]
    answer = list(permutations(digits, r=len(digits)))[999_999]
    print(
        f"Millionth lexicographic permutation of the digits 0-9:\n\n\t{''.join([str(digit) for digit in answer])}\n"
    )

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
