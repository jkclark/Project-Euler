#!/usr/bin/env python3
'''
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''

from helpers import print_memory_usage_report, print_time_elapsed
from time import time
import tracemalloc


def _get_num_digits(num: int) -> int:
    '''Get the number of digits in a number.'''
    return len(str(num))


def _get_nth_digit_of_num(n: int, num: int) -> int:
    '''Get the nth digit from the left of a number, starting at 1.'''
    return int(str(num)[max(0, n - 1)])


def main():
    # Keep track of time elapsed and memory used
    start_time = time()
    tracemalloc.start()

    # ********** Solution begins here ********** #

    final_product = current = next_significant_place = 1
    digits_used = 0

    while next_significant_place < 10_000_000:
        curr_num_digits = _get_num_digits(current)

        # This number is going to contain a significant digit
        if digits_used + curr_num_digits >= next_significant_place:
            final_product *= _get_nth_digit_of_num(
                next_significant_place - digits_used,
                current
            )

            next_significant_place *= 10

        digits_used += curr_num_digits
        current += 1

    print(f'Product of digits:\n\n\t{final_product}\n')

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
