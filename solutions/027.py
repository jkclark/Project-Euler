#!/usr/bin/env python3
'''
TODO: Add problem description
'''

from helpers import print_memory_usage_report, print_time_elapsed
from time import time
import tracemalloc

from math import floor, prod, sqrt


def _is_prime(num: int) -> bool:
    if num <= 1:
        return False

    for potential_factor in range(2, floor(sqrt(num)) + 1):
        if num % potential_factor == 0:
            return False

    return True


def main():
    # Keep track of time elapsed and memory used
    start_time = time()
    tracemalloc.start()

    # ********** Solution begins here ********** #

    best_a_b = (None, None)
    best_n = None

    for a in range(-999, 1000, 1):
        for b in range(-1000, 1001, 1):
            n = 0
            curr_is_prime = True
            while curr_is_prime:
                expr_value = n ** 2 + (a * n) + b
                curr_is_prime = _is_prime(expr_value)
                n += 1

            if best_n is None or (best_n < n):
                #  print(f"Found better n and (a, b): {n}, {(a, b)} ")
                best_n = n
                best_a_b = (a, b)

    print(f'The product of the coefficients which produce max primes:\n\n\t{prod(best_a_b)}\n')

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
