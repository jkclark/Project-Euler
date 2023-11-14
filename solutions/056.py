#!/usr/bin/env python3
"""
A googol (10 ^ 100) is a massive number: one followed by one-hundred zeros; 100
^ 100 is almost unimaginably large: one followed by two-hundred zeros. Despite
their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a ^ b, where a,b < 100, what is the
maximum digital sum?
"""
from helpers import measure_time_and_memory


@measure_time_and_memory
def main():
    """Find the maximum digit sum from the natural numbers a^b where a,b < 100."""
    maximum_digit_sum = max(
        sum(int(digit) for digit in str(a**b)) for a in range(100) for b in range(100)
    )

    print(
        f"The maximum digit sum from the natural numbers a^b | a,b < 100:\
          \n\n\t{maximum_digit_sum}\n"
    )


if __name__ == "__main__":
    main()
