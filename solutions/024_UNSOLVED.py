#!/usr/bin/python3
'''
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of
the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

from helpers import print_memory_usage_report, print_time_elapsed
from math import factorial
from time import time
import tracemalloc


def main():
    # Keep track of time elapsed and memory used
    start_time = time()
    tracemalloc.start()

    # ********** Solution begins here ********** #

    '''
    Reasoning:

    We have 10 digits to use. If we take 0 as the first digit, we have 9 digits left to use.
    There are 9! = 362,880 permutations of 9 digits that begin with 0.
    1,000,000 - 362,880 = 637,120 permutations to go.

    There are also 9! = 362,880 permutations that begin with 1.
    637,120 - 362,880 = 274,240 permutations to go. This means our target permutation begins with 2.

    There are 8! = 40,320 permutations that begin with 20. 274,240 - 40,320 = 233,920 permutations to go.
    We can continue to subtract 40,320 off of our "permutations remaining" number until we are left with
    fewer than 40,320 permutations.

    After all 20- permutations: 233,920
    After all 21- permutations: 193,600
    After all 22- permutations: 153,280
    After all 23- permutations: 112,960
    After all 24- permutations:  72,640
    After all 25- permutations:  32,320

    This means our target permutation begins with 26. We can continue this process to arrive at
    our target number.
    '''

    digits_left = [digit for digit in range(10)]
    perms_to_go = 1_000_000
    target_perm_prefix = ''

    while perms_to_go > 0:
        print(f'Perms to go: {perms_to_go}')
        digits_to_use = len(digits_left) - 1
        print(f'Digits to use: {digits_to_use}')
        for digit in digits_left:
            if factorial(digits_to_use) <= perms_to_go:
                perms_to_go -= factorial(digits_to_use)
                if factorial(digits_to_use) > 1000:
                    print(f'Subtracting {factorial(digits_to_use)}: {perms_to_go}')

            else:
                target_perm_prefix += str(digit)
                digits_left.remove(digit)

                print(f'Removing {digit}. New perm prefix: {target_perm_prefix}')
                print(f'Digits remaining: {len(digits_left)} -- {digits_left}')
                break

    print(f':\n\n\t{None}\n')

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
