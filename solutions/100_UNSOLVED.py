#!/usr/bin/env python3
"""
If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 10^12 = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain.
"""

from helpers import print_memory_usage_report, print_time_elapsed
from time import time
import tracemalloc

import decimal
from math import sqrt


MINIMUM = 10**12


def calculate_two_blue_disc_probability(blue_discs: int, red_discs: int) -> float:
    total_discs = blue_discs + red_discs
    return (blue_discs / total_discs) * ((blue_discs - 1) / (total_discs - 1))


def find_red_given_blue(blue_discs: int) -> bool:
    """Binary search for a corresponding number of red discs."""
    low = blue_discs * 0.35
    high = blue_discs * 0.45
    while low < high:
        mid = (low + high) // 2
        prob = calculate_two_blue_disc_probability(blue_discs, mid)
        # print(f"prob: {prob}")
        # prob = round(prob, 15)

        if prob == 0.5:
            break

        if prob < 0.5:
            if high == mid:
                break
            high = mid
        else:
            if low == mid:
                break
            low = mid

    if prob == 0.5:
        total = blue_discs + mid
        enough = total > MINIMUM
        print(f"FOUND: Blue/Total: {blue_discs}/{total:,}, total enough? : {enough}")
        return enough

    # else:
    #     print(f"Did not find red for blue = {blue_discs}")

    return False


def get_prob_of_two_blues(blues, total):
    return (blues / total) * ((blues - 1) / (total - 1))


def polynomial(n: int):
    return (1 + sqrt(1 + ((n * (n - 1)) / 2))) / 2


def second_polynomial(n: int):
    n = decimal.Decimal(n)
    return (1 + (1 + 2 * (n ** decimal.Decimal(2.0) - n)) ** decimal.Decimal(0.5)) / 2


def binary_search_for_b(constant: int):
    """Find (or fail to find) an integer b where b^2 - b = constant."""
    low = 6 * 10**11
    # low = 0
    high = 8 * 10**11
    # high = 50
    while low < high:
        mid = low + (high - low) // 2
        calc = mid**2 - mid

        if calc == constant:
            print("success!")
            return mid

        if calc > constant:
            if high == mid:
                break
            high = mid
        else:
            if low == mid:
                break
            low = mid

    return 0


def main():
    # Keep track of time elapsed and memory used
    start_time = time()
    tracemalloc.start()

    # ********** Solution begins here ********** #

    # good blue so far is 707106802629
    # for blue in range(707_105_702_000, 800_000_000_000):
    #     if find_red_given_blue(blue):
    #         break

    decimal.getcontext().prec = 100

    # Highest n checked: 1,000,034,650,000
    # n = MINIMUM
    n = 1_000_540_000_000
    while n < 2 * MINIMUM:
        if n % 10_000 == 0:
            print(f"Doing {n:,}")
        # n_dec = decimal.Decimal(n)
        # constant = (n_dec ** decimal.Decimal(2) - n_dec) / decimal.Decimal(2)
        # print(f"Constant: {constant}")
        root = second_polynomial(n)
        if root == int(root):
            print(f"Found integer solution for n = {n}")
            probability = get_prob_of_two_blues(root, n)
            # print(f"Probability: {probability}")
            if probability == 0.5:
                print(f"blues, total: {int(root)},{n}")
                break
        n += 1

    print(f":\n\n\t{None}\n")

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
