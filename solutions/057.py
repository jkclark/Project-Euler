#!/usr/bin/env python3
"""
It is possible to show that the square root of two can be expressed as an
infinite continued fraction.

By expanding this for the first four iterations, we get:

The next three expansions are , , and , but the eighth expansion, , is the first
example where the number of digits in the numerator exceeds the number of digits
in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator
with more digits than the denominator?
"""
from typing import Union
from helpers import measure_time_and_memory


@measure_time_and_memory
def main():
    """Find the number of expansions containing a numerator longer than the denominator.

    I think there is a simpler way that doesn't involve working with so many fractions,
    but this is what I came up with.
    """
    prev_part = Fraction(0, 1)
    qualifying_expansions = 0
    for _ in range(1000):
        # Find current expansion's value
        new_prev_part = Fraction(1, Fraction(2, 1) + prev_part)
        result = Fraction(1, 1) + new_prev_part

        # Increment counter if numerator longer than denominator
        if result.numerator_length > result.denominator_length:
            qualifying_expansions += 1

        # Update prev_part
        prev_part = new_prev_part

    print(
        f"The number of expansions with a longer numerator than denominator:\
          \n\n\t{qualifying_expansions}\n"
    )


class Fraction:
    """
    A class representing a fraction.
    """

    def __init__(
        self, numerator: Union[int, "Fraction"], denominator: Union[int, "Fraction"]
    ) -> None:
        if isinstance(numerator, int) and isinstance(denominator, int):
            self.numerator = numerator
            self.denominator = denominator

        # If either numerator or denominator is a Fraction, simplify
        else:
            if isinstance(numerator, int):
                numerator = Fraction(numerator, 1)

            if isinstance(denominator, int):
                denominator = Fraction(denominator, 1)

            simplified = numerator * denominator.reciprocal

            self.numerator = simplified.numerator
            self.denominator = simplified.denominator

    @property
    def numerator_length(self):
        """Get the number of digits in this Fraction's numerator."""
        return len(str(self.numerator))

    @property
    def denominator_length(self):
        """Get the number of digits in this Fraction's denominator."""
        return len(str(self.denominator))

    @property
    def reciprocal(self):
        """Get the reciprocal of this Fraction."""
        return Fraction(self.denominator, self.numerator)

    def __add__(self, other: "Fraction") -> "Fraction":
        """Add a Fraction to this Fraction, returning a new Fraction."""
        return Fraction(
            self.numerator * other.denominator + other.numerator * self.denominator,
            self.denominator * other.denominator,
        )

    def __mul__(self, other: "Fraction") -> "Fraction":
        """Multiply this Fraction with another Fraction, returning a new Fraction."""
        return Fraction(
            self.numerator * other.numerator, self.denominator * other.denominator
        )

    def __repr__(self) -> str:
        """Return a string representation of this Fraction.

        Useful for debugging.
        """
        return f"({self.numerator} / {self.denominator})"


if __name__ == "__main__":
    main()
