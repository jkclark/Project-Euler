#!/usr/bin/env python3
'''
The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

from helpers import print_memory_usage_report, print_time_elapsed
from time import time
import tracemalloc


def _is_palindrome(string: str) -> bool:
    LENGTH = len(string)
    for index in range(LENGTH // 2):
        if string[index] != string[LENGTH - 1 - index]:
            return False

    return True


def main():
    # Keep track of time elapsed and memory used
    start_time = time()
    tracemalloc.start()

    # ********** Solution begins here ********** #

    '''
    Since the palindromic number may not include leading zeros, no palindromic number may end in a zero.
    Since all even numbers end in a zero in binary, we don't need to check any even numbers.
    '''
    sum_palindromes = 0
    for num in range(1, 1_000_000, 2):
        sum_palindromes += num if _is_palindrome(str(num)) and _is_palindrome(bin(num)[2:]) else 0

    print(f'Sum of numbers < 1,000,000 which are palindromic in base 10 and base 2:\n\n\t{sum_palindromes}\n')

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
