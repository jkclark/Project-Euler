#!/usr/bin/env python3
'''
A positive fraction whose numerator is less than its denominator is called a proper fraction.
For any denominator, d, there will be d−1 proper fractions; for example, with d = 12:
1/12 , 2/12 , 3/12 , 4/12 , 5/12 , 6/12 , 7/12 , 8/12 , 9/12 , 10/12 , 11/12 .

We shall call a fraction that cannot be cancelled down a resilient fraction.
Furthermore we shall define the resilience of a denominator, R(d), to be the ratio of its proper fractions that are resilient; for example, R(12) = 4/11 .
In fact, d = 12 is the smallest denominator having a resilience R(d) < 4/10 .

Find the smallest denominator d, having a resilience R(d) < 15499/94744 .
'''

from helpers import print_memory_usage_report, print_time_elapsed
from time import time
import tracemalloc

from math import ceil


def _find_gcd(big: int, small: int) -> int:
    while (remainder := big % small) != 0:
        big = small
        small = remainder

    return small


def main():
    # Keep track of time elapsed and memory used
    start_time = time()
    tracemalloc.start()

    # ********** Solution begins here ********** #

    '''
    As far as I understand this problem, R(d) describes how many positive integers less than d
    are coprime with d, divided by d. We can use Euclid's algorithm to determine the GCD of two numbers.
    If the GCD of two numbers is 1, they are coprime, and their proper fraction is resilient.

    For any d, we can check the GCD of every number between 1 and d, and then we've found R(d).
    '''

    MAX_RESILIENCE = 15499 / 94744
    #  denominator = 12
    denominator = 104832  # Algo was too slow first run, got here and stopped
    while True:
        print(f'Denominator: {denominator}')
        resilient_count = 0
        max_resilients_allowed = ceil(MAX_RESILIENCE * denominator)

        for numerator in range(1, denominator):
            if _find_gcd(denominator, numerator) == 1:
                resilient_count += 1

                if resilient_count > max_resilients_allowed:
                    break

        if resilient_count / (denominator - 1) < MAX_RESILIENCE:
            smallest_denominator = denominator
            break

        denominator += 2

    print(f'The smallest denominator having a resilience R(d) < 15499/94744:\n\n\t{smallest_denominator}\n')

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
