#!/usr/bin/python3
'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import math
from time import time


def isPrime(num: int) -> bool:
    for potential_factor in range(2, math.floor(math.sqrt(num)) + 1):
        if num % potential_factor == 0:
            return False

    return True


def main():
    largest_prime_factor = None
    GIVEN_NUMBER = 600851475143
    for potential_factor in range(math.floor(math.sqrt(GIVEN_NUMBER)) + 1, 1, -1):
        if GIVEN_NUMBER % potential_factor == 0 and isPrime(potential_factor):
            largest_prime_factor = potential_factor
            break

    print(f'Largest prime factor of 600851475143: {largest_prime_factor}')


if __name__ == '__main__':
    start = time()
    main()
    print(f'Time: {time() - start}s')
