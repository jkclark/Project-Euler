#!/usr/bin/env python3
"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

from helpers import print_memory_usage_report, print_time_elapsed
from time import time
import tracemalloc


def get_digits_of_number(num: int):
    while num > 0:
        yield num % 10
        num //= 10


def raise_to_fifth_and_sum_nums(nums: list[int]):
    return sum(num**5 for num in nums)


def can_be_written_as_sum_of_fifth_powers(num: int):
    """Returns True if num can be written as the sum of fifth powers of its digits, False otherwise."""
    return raise_to_fifth_and_sum_nums(list(get_digits_of_number(num))) == num


def main():
    # Keep track of time elapsed and memory used
    start_time = time()
    tracemalloc.start()

    # ********** Solution begins here ********** #

    LIMIT = 1_000_000
    sum_of_fifthable_numbers = sum(  # Arbitrarily start at 10 because we know single-digit nums don't work
        num for num in range(10, LIMIT) if can_be_written_as_sum_of_fifth_powers(num)
    )

    print(
        f"Sum of numbers that can be written as the sum of fifth powers of their digits:\n\n\t{sum_of_fifthable_numbers}\n"
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
