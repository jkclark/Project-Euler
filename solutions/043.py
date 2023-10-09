#!/usr/bin/env python3
"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
each of the digits 0 to 9 in some order, but it also has a rather interesting
sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note
the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

from helpers import measure_time_and_memory


@measure_time_and_memory
def main():
    numbers_with_property = set()

    def recurse_all_permutations(number: str, digits: set) -> None:
        # Base case
        if len(digits) == 0 and number_has_properties(number):
            numbers_with_property.add(int(number))

        for digit in digits:
            # Make copy of set without current digit
            removed = digits.copy()
            removed.remove(digit)

            # Recursive call with longer number and smaller set
            recurse_all_permutations(number + digit, removed)

    recurse_all_permutations("", {str(digit) for digit in range(10)})

    print(
        f"The sum of all 0 to 9 pandigital numbers with this property:\n\n\t{sum(numbers_with_property)}\n"
    )


def number_has_properties(number: str) -> bool:
    """Return True if the number's 'substrings' have the required properties.

    Some thoughts:
        - d4 must be even for d2d3d4 to be divisible by 2
        - d6 must be 0 or 5 for d4d5d6 to be divisible by 5
    """
    return (
        int(number[3]) % 2 == 0
        and int(number[2:5]) % 3 == 0
        and int(number[5]) % 5 == 0
        and int(number[4:7]) % 7 == 0
        and int(number[5:8]) % 11 == 0
        and int(number[6:9]) % 13 == 0
        and int(number[7:]) % 17 == 0
    )


if __name__ == "__main__":
    main()
