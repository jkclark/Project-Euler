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

(* denotes a duplicate expression)

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
    """Calculate the number of ways 100 can be written as a sum of >= two positive integers.

    The algorithm implemented here is a bottom-up DP solution, but it's a bit
    convoluted. Basically, we want to keep track of the number of ways to
    express a number n, so that n + 1 can be calculated.  That way we can get
    the value for 100. The complexity here comes from the fact that there are
    many duplicates to be considered. We can express n through:
    - all of the ways we can express (n - 1) + 1
    - all of the ways we can express (n - 2) + 2, excluding duplicates from (n - 1) + 1
    - ...

    The question becomes: how can we know if an expression of (n - 2) + 2 is
    already present in all of the ways we can express (n - 1) + 1? One
    realization I had in solving this problem is that any expression of (n - 2)
    + 2 that contains a 1 must already be present in the expressions of (n - 1)
    + 1. Imagine our expression of (n - 2) + 2 begins with a 1. This means that
    the remainder of the expression must equal (n - 2) + 2 - 1 = n - 1. This
    means our expression comes out to 1 + (n - 1), which is definitely in our
    expressions of (n - 1) + 1.

    All of that is to say that after we get all expressions of (n - 1) + 1, we
    can ignore all expressions of (n - 2) + 2 that contain a 1. We can continue
    this pattern -- any expression of (n - 3) + 3 may not include 1 or 2.

    For each n, we are going to keep track of expressions by grouping them by
    their minimum term. For example, 3 has 2 expressions whose minimum terms are
    1: (1 + 1 + 1) and (2 + 1). 3 has 1 expression whose minimum term is 3: (3).
    To calculate the values for 4, we start by counting the number of ways we
    can express (4 - 1) = 3, using all terms (there are 3 ways). Then, we look
    to 2, but we only consider the ways that 2 can be expressed without using
    the number 1. There is only 1 way (2). Adding these numbers together, we get
    that there are (3 + 1) = 4 ways to express 4 as a sum of at least 2
    integers.
    """
    ways = {}
    ways[1] = {1: 1}
    ways[2] = {1: 1, 2: 1}
    ways[3] = {1: 2, 3: 1}

    for num in range(4, 100 + 1):
        ways_with_minimum = {}
        for minimum in range(1, num // 2 + 1):
            ways_with_minimum[minimum] = sum_over_keys_values_gte(
                ways[num - minimum], minimum
            )

        ways_with_minimum[num] = 1  # There is one way to express the number by itself
        ways[num] = ways_with_minimum

    # Subtract one because we aren't counting 100 by itself (need two operands)
    print(
        f"Number of ways 100 can be written as sum of at least two positive integers:\
          \n\n\t{sum_over_keys_values_gte(ways[100], 0) - 1}\n"
    )


def sum_over_keys_values_gte(keys_and_values: dict, minimum_key: int) -> int:
    """Sum the values of keys which are greater than or equal to the given minimum."""
    return sum(value for key, value in keys_and_values.items() if key >= minimum_key)


if __name__ == "__main__":
    main()
