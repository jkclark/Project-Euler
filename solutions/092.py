#!/usr/bin/env python3
'''
A number chain is created by continuously adding the square of the digits in a number
to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop.
What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
'''

from helpers import print_memory_usage_report, print_time_elapsed
from time import time
import tracemalloc


chain_endings = [None for _ in range(568)]
chain_endings[1] = 1
chain_endings[89] = 89


def _get_sum_of_squares_of_digits(num: int) -> int:
    sum_squares_digits = 0
    while num > 0:
        sum_squares_digits += (num % 10) ** 2
        num //= 10

    return sum_squares_digits


def _get_number_chain_end(num: int):
    global chain_endings

    seen = set()
    while num not in (1, 89):
        if chain_endings[num] is not None:
            num = chain_endings[num]
            break

        seen.add(num)

        num = _get_sum_of_squares_of_digits(num)

    for chain_piece in seen:
        chain_endings[chain_piece] = num


def main():
    # Keep track of time elapsed and memory used
    start_time = time()
    tracemalloc.start()

    # ********** Solution begins here ********** #

    '''
    The maximum sum of squares of digits for any number less than 10,000,000 is the sum of the squares of
    the digits in the number 9,999,999. That sum is 9 ^ 2 * 7 = 567. To save on space and time, we can
    precompute the ends of the chains for all of the integers between 1 and 567, inclusive. Then, for every
    integer between 568 and 9,999,999, inclusive, we calculate the sum of the squares of the digits, check
    where that number's chain ends, and increment the counter if necessary.
    '''
    chains_ending_in_89 = 0
    for num in range(2, 568):
        _get_number_chain_end(num)
        chains_ending_in_89 += chain_endings[num] == 89

    for num in range(568, 10_000_000):
        chains_ending_in_89 += chain_endings[_get_sum_of_squares_of_digits(num)] == 89

    print(f'Numbers < 10,000,000 whose square digit chains end in 89:\n\n\t{chains_ending_in_89}\n')

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
