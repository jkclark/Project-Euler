#!/usr/bin/env python3
'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''

from helpers import print_memory_usage_report, print_time_elapsed
from time import time
import tracemalloc

from itertools import permutations


def _check_identity(multiplicand: int, multiplier: int, product: int) -> bool:
    return multiplicand * multiplier == product


def _form_identity_components(permutation):
    # TODO: I realize that we have to decide where to break the tuple into
    #       multiplicand, mulitplier, and product. This adds another layer of complexity...


def main():
    # Keep track of time elapsed and memory used
    start_time = time()
    tracemalloc.start()

    # ********** Solution begins here ********** #

    pandigital_sum = 0
    included_pandigitals = set()
    for perm in permutations([digit for digit in range(1, 10)]):
        (multiplicand, multiplier, product) = *_form_identity_components(perm)

        if product in included_pandigitals:
            continue

        if _check_identity(multiplicand, multiplier, product):
            included_pandigitals.add(product)
            pandigital_sum += product


    print(f'The sum of all products whose m/m/p identity can be written as a 1-9 pandigital:\n\n\t{pandigital_sum}\n')

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
