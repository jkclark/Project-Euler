#!/usr/bin/env python3
"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

from helpers import print_memory_usage_report, print_time_elapsed
from time import time
import tracemalloc

from itertools import permutations


def create_num_from_iterable(iterable):
    num = 0
    for digit in iterable:
        num *= 10
        num += digit

    return num


def check_equation_truth(multiplicand, multiplier, product):
    return multiplicand * multiplier == product


def main():
    # Keep track of time elapsed and memory used
    start_time = time()
    tracemalloc.start()

    # ********** Solution begins here ********** #
    valid_products = set()
    PANDIGITAL_NUM_LENGTH = 10
    digits = [digit for digit in range(1, 10)]

    # Iterate over all pandigital numbers
    for index, permutation in enumerate(permutations(digits)):
        for mult_index in range(1, PANDIGITAL_NUM_LENGTH - 3):
            for eq_index in range(mult_index + 1, PANDIGITAL_NUM_LENGTH - 2):
                multiplicand = create_num_from_iterable(permutation[:mult_index])
                multiplier = create_num_from_iterable(permutation[mult_index:eq_index])
                product = create_num_from_iterable(permutation[eq_index:])
                if check_equation_truth(multiplicand, multiplier, product):
                    valid_products.add(product)

    pandigital_sum = sum(product for product in valid_products)
    print(
        f"The sum of all products whose m/m/p identity can be written as a 1-9 pandigital:\n\n\t{pandigital_sum}\n"
    )

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
