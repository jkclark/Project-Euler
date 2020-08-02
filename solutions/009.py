#!/usr/bin/python3
'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

from math import sqrt
from time import time


def main():
    for a in range(1, 1001):
        for b in range(1, 1001):
            c = sqrt(a ** 2 + b ** 2)
            if c == int(c) and a + b + c == 1000:
                product = int(a * b * c)
                break

    print(f'Product of Pythagorean triplet which sums to 1000: {product}')


if __name__ == '__main__':
    start = time()
    main()
    print(f'Time: {time() - start}s')
