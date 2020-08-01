#!/usr/bin/python3
'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
'''

import math
from time import time


def isPrime(num: int) -> bool:
    for potential_factor in range(2, math.floor(math.sqrt(num)) + 1):
        if num % potential_factor == 0:
            return False

    return True


def main():
    prime_count = 0
    candidate = 2
    while prime_count < 10001:
        if isPrime(candidate):
            prime_count += 1
        candidate += 1

    # When the above loop terminates, we've added 1 to the number which was the 10,001st prime
    print(f'10,001st prime number: {candidate - 1}')


if __name__ == '__main__':
    start = time()
    main()
    print(f'Time: {time() - start}s')
