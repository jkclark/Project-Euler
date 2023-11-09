#!/usr/bin/env python3
"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

from helpers import measure_time_and_memory


@measure_time_and_memory
def main():
    """Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part."""
    max_cycle_length = 0
    corresponding_denominator = 0
    for denominator in range(1, 1000):
        if (
            cycle_length := get_reciprocal_cycle_length(denominator)
        ) > max_cycle_length:
            max_cycle_length = cycle_length
            corresponding_denominator = denominator

    print(
        f"The value of d < 1000 for which 1/d has the longest recurring cycle:\
        \n\n\t{corresponding_denominator}\n"
    )


def get_reciprocal_cycle_length(denominator: int) -> int:
    """Find the length of the recurring cycle of 1/denominator.

    This function implements long division and keeps track of the "remainders"
    that occur at each decimal place. Once we see a remainder for the second time,
    the digits in the decimal part of the fraction will begin to repeat.
    """
    # remainders is a {remainder: place} map, where place indicates the decimal place
    # the remainder corresponds to
    remainders = {}
    remainder_count = 0
    remainder = 1

    while True:
        # Find the number we're going to subtract (in long division)
        multiple = remainder // denominator * denominator

        # Do the subtraction
        remainder = remainder - multiple

        # If there is no difference, this number does not repeat
        if remainder == 0:
            return 0

        # Multiply by 10 for the next decimal place
        remainder *= 10

        # If this number still isn't big enough to divide into,
        # "take" another decimal place.
        while remainder < denominator:
            remainders[remainder] = remainder_count
            remainder_count += 1
            remainder *= 10

        # If we've seen this remainder before, we've begun to repeat
        if remainder in remainders:
            return remainder_count - remainders[remainder]

        remainders[remainder] = remainder_count
        remainder_count += 1


if __name__ == "__main__":
    main()
