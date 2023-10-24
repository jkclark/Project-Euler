#!/usr/bin/env python3
"""
The series, 1^1 + 2^2 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + ... + 10^10.

Some thoughts:
- Can very quickly test doing this by brute force.
- We only need to add the first 10 digits of each number, since the rest
  don't apply to this problem. If we could implement addiiton ourselves,
  we could just get the value (like 27 for 3^3) and manually add the first
  10 digits to our current solution.
"""

from helpers import measure_time_and_memory


def add_self_powers(limit: int) -> int:
    """Add the self powers of numbers from 1 up to the limit, inclusive."""
    return sum(num**num for num in range(1, limit + 1))


@measure_time_and_memory
def main():
    print(
        f"The last ten digits of the series are:\n\n\t{str(add_self_powers(1000))[-10:]}\n"
    )


if __name__ == "__main__":
    main()
