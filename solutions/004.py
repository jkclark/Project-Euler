#!/usr/bin/python3
"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from helpers import measure_time_and_memory


def _is_palindrome(num: int) -> bool:
    string_num = str(num)
    return string_num == string_num[::-1]


@measure_time_and_memory
def main():
    max_palindrome = 0
    for a in range(100, 1000):
        for b in range(100, 1000):
            product = a * b
            if _is_palindrome(product):
                max_palindrome = max(max_palindrome, product)

    print(
        f"Largest palindrome made from the product of two 3-digit numbers:\n\n\t{max_palindrome}\n"
    )


if __name__ == "__main__":
    main()
