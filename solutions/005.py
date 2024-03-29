#!/usr/bin/python3
"""
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
"""

import operator
from functools import reduce

from helpers import measure_time_and_memory


@measure_time_and_memory
def main():
    """
    The idea: we need to mutliply every number between 1 and 20 into our target number. Equivalently,
    we need to be able to describe each number between 1 and 20 as the product of numbers in the prime
    factorization of our target number.

    The algorithm:
    collection = []
    for num = 1 --> 20:
        add to collection any numbers required to create the prime factorization of num
        without using any number more than once
    target = multiply collection together

    EDIT: The problem thread enlightened me with this: for every prime number smaller than 20,
    find the highest power of that prime number that is also smaller than 20 and multiply them
    together.
    """
    prime_factors = [
        2,  # (1), 2
        3,  # 3
        2,  # 4 = 2 * 2
        5,  # 5, (6)
        7,  # 7
        2,  # 8 = 2 * 2 * 2
        3,  # 9 = 3 * 3, (10)
        11,  # 11, (12)
        13,  # 13, (14), (15)
        2,  # 16 = 2 * 2 * 2 * 2
        17,  # 17, (18)
        19,  # 19, (20)
    ]
    smallest = reduce(operator.mul, prime_factors)

    print(
        f"Smallest positive number evenly divisible by all numbers from 1 to 20:\n\n\t{smallest}\n"
    )


if __name__ == "__main__":
    main()
