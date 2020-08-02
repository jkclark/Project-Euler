#!/usr/bin/python3
'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

from math import floor, sqrt
from time import time


def main():
    LIMIT = 2_000_000
    prime_or_not = [True for _ in range(LIMIT)]
    prime_or_not[0] = False
    prime_or_not[1] = False

    # Sieve of Eratosthenes
    for num in range(2, floor(sqrt(LIMIT)) + 1):
        if prime_or_not[num]:
            for multiple in range(num * num, LIMIT, num):
                prime_or_not[multiple] = False

    # Add up the value of each prime
    sum_of_primes = 0
    for num in range(LIMIT):
        if prime_or_not[num]:
            sum_of_primes += num

    print(f'Sum of primes below two million: {sum_of_primes}')


if __name__ == '__main__':
    start = time()
    main()
    print(f'Time: {time() - start}s')
