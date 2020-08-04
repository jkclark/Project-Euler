#!/usr/bin/python3
'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

from helpers import print_memory_usage_report, print_time_elapsed
from time import time
import tracemalloc


memo = {1: 1}


def _iterative_count_collatz_sequence_length(num: int) -> int:
    length = 1
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1

        length += 1

    return length


def _recursive_count_collatz_sequence_length(num: int) -> int:
    if num in memo:
        return memo[num]

    if num % 2 == 0:
        length = _recursive_count_collatz_sequence_length(num // 2)
    else:
        length = _recursive_count_collatz_sequence_length(3 * num + 1)

    memo[num] = length + 1
    return memo[num]


def main():
    # Keep track of time elapsed and memory used
    start_time = time()
    tracemalloc.start()

    # ********** Solution begins here ********** #

    longest_sequence_num = 1
    longest_sequence_length = 1
    for num in range(1, 1_000_000):
        # Iterative solution (Time: 29.436s, memory: 370 B)
        #  sequence_length = _iterative_count_collatz_sequence_length(num)

        # Recursive/DP solution (Time: 2.104s, memory: 140.296 MiB)
        sequence_length = _recursive_count_collatz_sequence_length(num)

        if sequence_length > longest_sequence_length:
            longest_sequence_length = sequence_length
            longest_sequence_num = num

    print(f'The number under one million with the longest Collatz sequence:\n\n\t{longest_sequence_num}\n')

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
