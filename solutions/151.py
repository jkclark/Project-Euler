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
from typing import List

from helpers import measure_time_and_memory


@measure_time_and_memory
def main():
    """Find the expected number of times a single piece of paper is found in the envelope.

    We're going to try a recursive approach where we statistically find the
    exact expected value.  Basically, we're going to traverse a probability tree
    where the value of each leaf node is the number of times exactly 1 piece of
    paper is seen in the envelope, multiplied by the probability of getting
    there. The probability of getting to any given node is the product of the
    probabilities of getting to all of that node's parents.
    """

    total = 0

    # NOTE: add probability as parameter, starting at 1
    #       one potential point of inaccuracy/imprecision is multiplying
    #       floats together. one option is to just multiply the denominator
    #       through recursive calls as an integer, and just dividing it at the end
    def dfs(envelope: List[int], probability: float, running_total: int):
        """Run a depth-first search from this envelope state."""
        nonlocal total

        # If we only have one piece of paper in the envelope
        if len(envelope) == 1:
            # If this is the the last piece of paper in the envelope,
            # we're done
            if envelope[0] == 1:
                total += running_total * probability
                return

            # Otherwise, this is the 'only one piece of paper' case, so add
            # to running total
            running_total += 1

        # Recurse through the envelope states available to us, multiplying the
        # current probability by the probability of giong to that state
        num_pieces = len(envelope)
        for piece in envelope:
            # Create copy of envelope
            new_envelope = envelope.copy()

            # Remove this piece of paper
            new_envelope.remove(piece)

            # Add newly created pieces of paper
            piece = piece // 2
            while piece >= 1:
                new_envelope.append(piece // 2)
                piece = piece // 2

            # Recurse
            dfs(new_envelope, probability * (1 / num_pieces), running_total)

    dfs([8, 8], 1, 0)

    print(
        f"The expected number of times a single piece of paper is found in the envelope:\
          \n\n\t{round(total, 6)}\n"
    )


if __name__ == "__main__":
    main()
