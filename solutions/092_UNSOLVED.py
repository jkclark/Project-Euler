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


def _get_number_chain_end(num: int) -> int:
    # TODO: Memoize -- make a global dictionary/array of numbers and their
    #       chain endings. That way, when we see a really high number, we can check
    #       if we've seen it in a chain before, and if so, return immediately.
    seen = set()
    while num not in seen:
        seen.add(num)
        num = sum([int(digit) ** 2 for digit in str(num)])

    return num


def main():
    # Keep track of time elapsed and memory used
    start_time = time()
    tracemalloc.start()

    # ********** Solution begins here ********** #

    chains_ending_in_89 = 0
    for num in range(10_000_000):
        chains_ending_in_89 += _get_number_chain_end(num) == 89

    print(f':\n\n\t{chains_ending_in_89}\n')

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
