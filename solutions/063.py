#!/usr/bin/env python3
"""
The 5-digit number, 16807 = 7^5, is also a fifth power. Similarly, the 9-digit
number, 134217728 = 8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""
import matplotlib.pyplot as plt

from helpers import measure_time_and_memory


@measure_time_and_memory
def main():
    """Find the number of n-digit numbers which are also nth powers."""
    ### Graphs show all qualifying numbers for this problem.
    # show_plots()

    # Count all qualifying integers
    total = 1  # 1^1 = 1, the only power of 1 which qualifies
    for base in range(2, 10):  # Only go up to 10, as demonstrated by graphs
        power = 1
        length = len(str(base**power))
        while power <= length:
            total += power == length
            power += 1
            length = len(str(base**power))

    print(f"The number of n-digit numbers which are also nth powers:\n\n\t{total}\n")


def show_plots():
    """Graph some interesting info for thinking about this problem.

    From the graphs shown here, we can see that starting from a base of 1,
    only n = 1 is a solution to this problem. Bases of 2 and 3 also only have
    n = 1 as a solution. 4 has 4^1 = 4 (1 digit) and 4^2 = 16. Bases 5-9
    also have multiple solutions. Once we get to 10, we can see that 10^2 already
    has 3 digits, so we can stop checking at base = 10.
    """
    base = 1
    max_power = 10
    powers = list(range(max_power))
    _, ax = plt.subplots(
        nrows=4,
        ncols=5,
    )
    for row in ax:
        for col in row:
            lengths = [len(str(base**power)) for power in range(max_power)]
            col.plot(powers, lengths)
            col.plot(powers, powers)
            col.set(
                title=f"{base}",
            )

            base += 1

    plt.show()


if __name__ == "__main__":
    main()
