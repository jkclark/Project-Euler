#!/usr/bin/python3
'''
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers
and the square of the sum.
'''

from time import time


def main():
    # Find the sum of the squares
    sum_of_squares = sum(num ** 2 for num in range(1, 101))

    # Find the square of the sum
    square_of_sum = sum(num for num in range(1, 101)) ** 2

    # Find the difference
    difference = square_of_sum - sum_of_squares
    print(f'Difference between sum of squares and square of sum: {difference}')


if __name__ == '__main__':
    start = time()
    main()
    print(f'Time: {time() - start}s')
