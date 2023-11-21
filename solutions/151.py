#!/usr/bin/env python3
"""
A printing shop runs 16 batches (jobs) every week and each batch requires a
sheet of special colour-proofing paper of size A5.

Every Monday morning, the supervisor opens a new envelope, containing a large
sheet of the special paper with size A1.

The supervisor proceeds to cut it in half, thus getting two sheets of size A2.
Then one of the sheets is cut in half to get two sheets of size A3 and so on
until an A5-size sheet is obtained, which is needed for the first batch of the
week.

All the unused sheets are placed back in the envelope.

(Image here)

At the beginning of each subsequent batch, the supervisor takes from the
envelope one sheet of paper at random. If it is of size A5, then it is used. If
it is larger, then the 'cut-in-half' procedure is repeated until an A5-size
sheet is obtained, and any remaining sheets are always placed back in the
envelope.

Excluding the first and last batch of the week, find the expected number of
times (during each week) that the supervisor finds a single sheet of paper in
the envelope.

Give your answer rounded to six decimal places using the format x.xxxxxx .
"""
import random
from typing import List

from helpers import measure_time_and_memory


@measure_time_and_memory
def main():
    """Find the expected number of times a single piece of paper is found in the envelope."""
    iterations = 50_000_000
    total_single_paper_pulls = 0
    for iteration in range(iterations):
        if iteration % 1_000 == 0:
            print(f"Doing iteration = {iteration}")

        week_single_paper_pulls = 0

        # 2 pieces of size A2 (A2 can be split 3 times before becoming A5)
        envelope = [8, 8]  # Exclude first draw from envelope

        for _ in range(15):  # Exclude last draw from envelope
            if len(envelope) == 1:
                week_single_paper_pulls += 1

            pull_paper_and_update(envelope)

        total_single_paper_pulls += week_single_paper_pulls

    expected_times = total_single_paper_pulls / iterations

    print(
        f"The expected number of times a single piece of paper is found in the envelope:\
          \n\n\t{round(expected_times, 6)}\n"
    )


def pull_paper_and_update(envelope: List[int]):
    """Pull a random piece of paper from the envelope, and cut/add new pieces if necessary.

    NOTE: This function modifies its input argument.
    """
    # Get a random piece of paper
    piece = random.choice(envelope)

    # Remove chosen piece of paper from envelope
    envelope.remove(piece)

    # If our piece is bigger than size A5, cut it down to size
    # and add all new pieces of paper to the envelope
    while piece > 1:
        envelope.append(piece // 2)
        piece //= 2


if __name__ == "__main__":
    main()
