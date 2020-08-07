#!/usr/bin/python3
'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

from helpers import print_memory_usage_report, print_time_elapsed
from time import time
import tracemalloc

from math import floor, sqrt


def _get_sum_of_divisors(num: int) -> int:
    if num < 2:
        return 0

    SQUARE_ROOT = sqrt(num)

    sum_of_divisors = 1  # Every non-negative integer has 1 as a proper divisor except for 0 and 1
    for divisor in range(2, floor(SQUARE_ROOT)):
        if num % divisor == 0:
            sum_of_divisors += divisor + num // divisor

    # The the square root of num is an integer, only add it to the total once, not twice as loop above would
    if int(SQUARE_ROOT) == SQUARE_ROOT:
        sum_of_divisors += int(SQUARE_ROOT)

    return sum_of_divisors


def main():
    # Keep track of time elapsed and memory used
    start_time = time()
    tracemalloc.start()

    # ********** Solution begins here ********** #

    sums_of_divisors = [0 for _ in range(10_000)]
    sums_of_divisors[0] = sums_of_divisors[1] = 0

    for num in range(2, 10_000):
        sums_of_divisors[num] = _get_sum_of_divisors(num)

    evaluated_nums = set()
    sum_of_amicable_nums = 0
    for num in range(2, 10_000):
        if num in evaluated_nums:
            continue

        sum_of_divisors = sums_of_divisors[num]
        if sum_of_divisors >= 10_000:
            continue

        if num != sum_of_divisors and num == sums_of_divisors[sum_of_divisors]:
            sum_of_amicable_nums += num + sum_of_divisors
            evaluated_nums.add(num)
            evaluated_nums.add(sum_of_divisors)

    print(f'Sum of amicable numbers under 10,000:\n\n\t{sum_of_amicable_nums}\n')

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
