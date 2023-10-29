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
"""

from collections import defaultdict

from helpers import measure_time_and_memory


@measure_time_and_memory
def main():
    """Calculate the number of ways 100 can be written as a sum of at least two positive integers."""
    num_to_ways = [1, 1, 1]

    for target in range(3, 100 + 1):
        low = 1
        high = target - 1
        ways = 1
        while high >= low:
            # I think the issue is here. Are there duplicate ways being counted?
            ways += num_to_ways[high] * num_to_ways[low]
            low += 1
            high -= 1

        num_to_ways.append(ways)

    print(
        f"Number of ways 100 can be written as sum of at least two positive integers:\n\n\t{None}\n"
    )


if __name__ == "__main__":
    main()
