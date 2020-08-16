#!/usr/bin/python3
'''
In the United Kingdom the currency is made up of pound (£) and pence (p).
There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''

from helpers import print_memory_usage_report, print_time_elapsed
from time import time
import tracemalloc


def main():
    # Keep track of time elapsed and memory used
    start_time = time()
    tracemalloc.start()

    # ********** Solution begins here ********** #

    COINS = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [{0}]

    for num in range(1, 201):
        ways_for_num = set()
        for index, coin in enumerate(COINS):
            if coin > num:
                break

            for way in ways[num - coin]:
                ways_for_num.add(10 ** index + way)

        ways.append(ways_for_num)

    print(f'Number of ways £2 be made using any number of coins:\n\n\t{len(ways[-1])}\n')

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
