#!/usr/bin/env python3
"""
NOTE: collections.Counter.total requires Python 3.10+

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

from helpers import print_memory_usage_report, print_time_elapsed
from time import time
import tracemalloc

from collections import Counter


def nums_share_only_one_digit(num1: int, num2: int) -> bool:
    """Returns True if the two numbers share only one digit, False otherwise."""
    c1 = Counter(str(num1))
    c2 = Counter(str(num2))
    return (c1 - c2).total() == 1 and (c2 - c1).total() == 1


def do_wrong_simplify(numerator: int, denominator: int) -> list[int]:
    """'Cancel' common digits to return remaining digits of two numbers.

    This function assumes that the two arguments share only one digit.
    E.g., 34 and 44 share only one digit.
    """
    c1 = Counter(str(numerator))
    c2 = Counter(str(denominator))
    return [int(next((c1 - c2).elements())), int(next((c2 - c1).elements()))]


def check_fraction_pair(numerator: int, denominator: int) -> bool:
    """Returns True if the (numerator, denominator) pair 'simplifies.'"""
    if nums_share_only_one_digit(numerator, denominator):
        new_numerator, new_denominator = do_wrong_simplify(numerator, denominator)
        try:
            return numerator / denominator == new_numerator / new_denominator
        except ZeroDivisionError:
            return False


def main():
    # Keep track of time elapsed and memory used
    start_time = time()
    tracemalloc.start()

    # ********** Solution begins here ********** #

    """
    Reasoning:
    
    There aren't very many fractions that we need to check. Each numerator n has (100 - n) denominators
    that need to be checked. There are 100 numerators, and on average each one has 50 denominators. That
    is to say there are 5,000 (numerator, denominator) pairs to check. Not too bad. (There are actually
    fewer than that because single-digit numbers are invalid).

    For each of these 5,000 pairs, there are 3 possible cases:
        - The two numbers share no digits --> trivial, cannot be simplified
        - The two numbers share exactly one digit --> cancel those digits, and do the check
        - The two numbers share both digits --> by cancelling either shared digit, the resulting fraction = 1
            - We know this does not work, because the problem states the answer fractions are "less than 1 in value"
    
    Therefore, we only need to check fraction pairs that share exactly one digit. For each such pair, we see if
    the "cancelled" version has the same value as the original version. We multiply all qualifying pairs together and
    we're done.
    """

    START = 10
    END = 100
    product = 1
    for numerator in range(START, END):
        for denominator in range(numerator + 1, END):
            # Ignore trivial cases
            if numerator % 10 == 0 and denominator % 10 == 0:
                continue

            if check_fraction_pair(numerator, denominator):
                product *= numerator / denominator

    print(f"Product of 4 such fractions:\n\n\t{product}\n")

    # ********** Solution ends here ********** #

    # Stop tracking time and memory
    snapshot = tracemalloc.take_snapshot()
    end_time = time()
    tracemalloc.stop()

    # Print time elapsed and memory used
    print_time_elapsed(start_time, end_time)
    print_memory_usage_report(snapshot)


if __name__ == "__main__":
    main()
