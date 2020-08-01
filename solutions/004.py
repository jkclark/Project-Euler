#!/usr/bin/python3
'''
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

from time import time


def isPalindrome(num):
    string_num = str(num)
    return string_num == string_num[::-1]


def main():
    max_palindrome = 0
    for a in range(100, 1000):
        for b in range(100, 1000):
            product = a * b
            if isPalindrome(product):
                max_palindrome = max(max_palindrome, product)

    print(f'Largest palindrome made from the product of two 3-digit numbers: {max_palindrome}')


if __name__ == '__main__':
    start = time()
    main()
    print(f'Time: {time() - start}s')
