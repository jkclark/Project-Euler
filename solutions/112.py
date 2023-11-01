#!/usr/bin/env python3
"""
Working from left-to-right if no digit is exceeded by the digit to its left it
is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a
decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a
"bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half
of the numbers below one-thousand (525) are bouncy. In fact, the least number for
which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we
reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.
"""
from helpers import measure_time_and_memory


@measure_time_and_memory
def main():
    """Find the least number for which the proportion of bouncy numbers is exactly 99%."""
    num = 1
    bouncy_nums = 0
    ratio = 0
    while ratio != 0.99:
        num += 1
        bouncy_nums += is_bouncy(num)
        ratio = bouncy_nums / num

    print(f"Least number to have 99% bouny number proportion:\n\n\t{num}\n")


def is_bouncy(num: int) -> bool:
    """Determine if a number is bouncy or not."""
    decreasing = increasing = True
    # num > 9 because we don't need to compare left-most digit to anything
    while num > 9 and (increasing or decreasing):
        right_digit = num % 10

        num = num // 10
        next_right_digit = num % 10

        if right_digit > next_right_digit:
            decreasing = False
        elif right_digit < next_right_digit:
            increasing = False

    return not (increasing or decreasing)


if __name__ == "__main__":
    main()
