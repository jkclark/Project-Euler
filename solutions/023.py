#!/usr/bin/python3
'''
A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number.  For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than
n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24.  By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers.  However, this upper limit
cannot be reduced any further by analysis even though it is known that the
greatest number that cannot be expressed as the sum of two abundant numbers is
less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.
'''

from helpers import print_memory_usage_report, print_time_elapsed
from time import time
import tracemalloc

from math import floor, sqrt
from typing import List


# Every number >= this number can be written as the sum of two abundant integers
MIN_GUARANTEE_SUM_OF_TWO = 28124


def _find_sum_of_proper_divisors(num: int) -> int:
    '''Find the sum of a number's proper divisors.'''
    divisors = {1}
    for divisor in range(2, floor(sqrt(num)) + 1):
        if num % divisor == 0:
            divisors.add(divisor)
            divisors.add(num / divisor)

    return sum(divisors)


def _find_all_abundant_numbers() -> List[int]:
    '''Get a list of all relevant abundant numbers.'''
    return [
        num
        for num in range(1, MIN_GUARANTEE_SUM_OF_TWO)
        if _find_sum_of_proper_divisors(num) > num
    ]


def _can_be_written_as_sum_of_list_pair(
    num: int,
    num_list: List[int]
) -> bool:
    '''Can a given number be written as the sum of two numbers from a list?

    Args:
        num: The number to check
        num_list: The *sorted* list of candidate addends
    '''
    low, high = 0, len(num_list) - 1
    while low <= high:
        pair_sum = num_list[low] + num_list[high]
        if pair_sum == num:
            return True
        elif pair_sum > num:
            high -= 1
        else:
            low += 1

    return False


def main():
    # Keep track of time elapsed and memory used
    start_time = time()
    tracemalloc.start()

    # ********** Solution begins here ********** #

    sum = 0
    abundant_nums = _find_all_abundant_numbers()
    for num in range(1, MIN_GUARANTEE_SUM_OF_TWO):
        if not _can_be_written_as_sum_of_list_pair(num, abundant_nums):
            sum += num

    print(f'Sum of integers non-writable as sums of abundants:\n\n\t{sum}\n')

    # ********** Solution ends here ********** #

    # Stop tracking time and memory
    snapshot = tracemalloc.take_snapshot()
    end_time = time()
    tracemalloc.stop()

    # Print time elapsed and memory used
    print_time_elapsed(start_time, end_time)
    print_memory_usage_report(snapshot)


if __name__ == '__main__':
    main()
