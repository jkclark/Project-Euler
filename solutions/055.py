#!/usr/bin/env python3
"""
A number that never forms a palindrome through the reverse and add process is
called a Lychrel number.

In addition you are given that for every number below ten-thousand, it will
either (i) become a palindrome in less than fifty iterations, or, (ii) no one,
with all the computing power that exists, has managed so far to map it to a
palindrome.

How many Lychrel numbers are there below ten-thousand?
"""

from helpers import measure_time_and_memory


@measure_time_and_memory
def main():
    """Calculate the number of Lychrel numbers below 10,000"""
    lychrel_number_count = sum(not is_lychrel_number(num) for num in range(10_000))

    print(f"Number of Lyrchrel numbers below 10,000:\n\n\t{lychrel_number_count}\n")


def is_lychrel_number(num: int) -> bool:
    """Return True if num is a Lychrel number, False otherwise."""
    iteration_limit = 50
    for _ in range(iteration_limit):
        palindrome_candidate = num + reverse_number(num)

        if is_palindrome(palindrome_candidate):
            return True

        num = palindrome_candidate

    return False


def reverse_number(num: int) -> int:
    """Return the number resulting from reversing the digits of num.

    E.g.: 47 -> 74
    E.g.: 123 -> 321
    """
    return int("".join(reversed(str(num))))


def is_palindrome(num: int) -> bool:
    """Retrun True if num is a palindrome, False otherwise."""
    return str(num) == "".join(reversed(str(num)))


if __name__ == "__main__":
    main()
