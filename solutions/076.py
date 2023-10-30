#!/usr/bin/env python3
"""
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?

Notes:
1:  1
2:  1 + 1: 
        (1 + 1)
3:  2 + 1:
        (1 + 1) + (1)
        (2) + (1)
4:  3 + 1:
        (1 + 1 + 1) + (1)
        (2 + 1) + (1)
        (3) + (1)
    2 + 2:
        (1 + 1) + (1 + 1)           *
        (1 + 1) + (2)               *
        (2) + (1 + 1)               *
        (2) + (2)
5:  4 + 1:
        (1 + 1 + 1 + 1) + (1)
        (2 + 1 + 1) + (1)
        (3 + 1) + (1)
        (2 + 2) + (1)
        (4) + (1)
    3 + 2:
        (1 + 1 + 1) + (1 + 1)           *
        (1 + 1 + 1) + (2)               *
        (2 + 1) + (1 + 1)               *
        (2 + 1) + (2)                   *
        (3) + (1 + 1)                   *
        (3) + (2)
6:  5 + 1:
        (1 + 1 + 1 + 1 + 1) + (1)
        (2 + 1 + 1 + 1) + (1)
        (3 + 1 + 1) + (1)
        (4 + 1) + (1)
        (2 + 1 + 2) + (1)
        (3 + 2) + (1)
        (5) + (1)
    4 + 2:
        (1 + 1 + 1 + 1) + (1 + 1)       *
        (1 + 1 + 1 + 1) + (2)           *
        (2 + 1 + 1) + (1 + 1)           *
        (2 + 1 + 1) + (2)               *
        (3 + 1) + (1 + 1)               *
        (3 + 1) + (2)                   *
        (2 + 2) + (1 + 1)               *
        (2 + 2) + (2)
        (4) + (1 + 1)                   *
        (4) + (2)
    3 + 3:
        (1 + 1 + 1) + (1 + 1 + 1)       *
        (1 + 1 + 1) + (2 + 1)           *
        (1 + 1 + 1) + (3)               *
        (2 + 1) + (1 + 1 + 1)           *
        (2 + 1) + (2 + 1)               *
        (2 + 1) + (3)                   *
        (3) + (1 + 1 + 1)               *
        (3) + (2 + 1)                   *
        (3) + (3)
7:  6 + 1:
        (1 + 1 + 1 + 1 + 1 + 1) + (1)
        (2 + 1 + 1 + 1 + 1) + (1)
        (3 + 1 + 1 + 1) + (1)
        (4 + 1 + 1) + (1)
        (2 + 1 + 2 + 1) + (1)
        (3 + 2 + 1) + (1)
        (5 + 1) + (1)
        (2 + 2 + 2) + (1)
        (4 + 2) + (1)
        (3 + 3) + (1)
        (6) + (1)
    5 + 2:
        (1 + 1 + 1 + 1 + 1) + (1 + 1)   *
        (1 + 1 + 1 + 1 + 1) + (2)       *
        (2 + 1 + 1 + 1) + (1 + 1)       *
        (2 + 1 + 1 + 1) + (2)           *
        (3 + 1 + 1) + (1 + 1)           *
        (3 + 1 + 1) + (2)               *
        (2 + 2 + 1) + (1 + 1)           *
        (2 + 2 + 1) + (2)               *
        (4 + 1) + (1 + 1)               *
        (4 + 1) + (2)                   *
        (3 + 2) + (1 + 1)               *
        (3 + 2) + (2)
        (5) + (1 + 1)                   *
        (5) + (2)
    4 + 3:
        (1 + 1 + 1 + 1) + (1 + 1 + 1)   *
        (1 + 1 + 1 + 1) + (2 + 1)       *
        (1 + 1 + 1 + 1) + (3)           *
        (2 + 1 + 1) + (1 + 1 + 1)       *
        (2 + 1 + 1) + (2 + 1)           *
        (2 + 1 + 1) + (3)               *
        (3 + 1) + (1 + 1 + 1)           *
        (3 + 1) + (2 + 1)               *
        (3 + 1) + (3)                   *
        (2 + 2) + (1 + 1 + 1)           *
        (2 + 2) + (2 + 1)               *
        (2 + 2) + (3)                   *
        (4) + (1 + 1 + 1)               *
        (4) + (2 + 1)                   *
        (4) + (3)

Results (not counting number itself):
1: 1
2: 1
3: 2
4: 4
5: 6
6: 10
7: 14
"""
from helpers import measure_time_and_memory


@measure_time_and_memory
def main():
    """Calculate the number of ways 100 can be written as a sum of at least two positive integers."""
    # Ways is 1-indexed, but sublists are 0-indexed
    ways = {}
    ways[1] = {1: 1}
    ways[2] = {1: 1, 2: 1}
    ways[3] = {1: 2, 2: 0, 3: 1}

    for num in range(4, 6):
        ways_with_minimum = {}
        for minimum in range(1, num // 2 + 1):
            # TODO: I think we need to sum ALL ways that have a minimum number (e.g., cumulative)
            ways_with_minimum[minimum] = ways[num - minimum][minimum]

        ways_with_minimum[num] = 1
        ways[num] = ways_with_minimum

    print(
        f"Number of ways 100 can be written as sum of at least two positive integers:\n\n\t{None}\n"
    )


if __name__ == "__main__":
    main()
