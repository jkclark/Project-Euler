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
from collections import Counter

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
    # Memoization
    # Here were storing envelope states and their corresponding values
    # The value of any envelope state is the sum of the values of all children
    # envelopes
    envelopes_to_probabilities = {}

    def dfs(envelope: Counter, level: int):
        """Run a depth-first search from this envelope state."""
        nonlocal envelopes_to_probabilities

        # If we've seen this envelope before, we're done
        fset = convert_counter_to_frozenset(envelope)
        if fset in envelopes_to_probabilities:
            return envelopes_to_probabilities[fset]

        # Base case: only 1 A5 piece of paper is in the envelope
        # if envelope.total() == 1:  # Python 3.12 being annoying on Windows machine
        if sum(envelope.values()) == 1 and 1 in envelope:
            return 0

        # Recurse through the envelope states available to us
        this_envelope_value = 0
        for piece in envelope:
            # Create copy of envelope
            child_envelope = envelope.copy()

            # Find the "probability" of choosing this piece
            this_piece_probability = child_envelope[piece] / sum(
                child_envelope.values()
            )

            # Remove this piece of paper
            remove_piece_from_envelope(piece, child_envelope)

            # Add newly created pieces of paper
            add_new_pieces_from_piece_to_envelope(piece, child_envelope)

            # Check if child-envelope state has only 1 piece of non-A5 paper
            child_envelope_has_one_piece = (
                sum(child_envelope.values()) == 1 and 1 not in child_envelope
            )

            # Recurse
            child_values = dfs(child_envelope, level + 1)

            # The value for this child envelope state is:
            # (probability of choosing a piece of this size) * (
            #   (1 if there is only one piece of paper in this child envelope, 0 otherwise)
            #   +
            #   (the EV for this child-envelope state)
            # )
            this_envelope_value += this_piece_probability * (
                child_envelope_has_one_piece + child_values
            )

        # Memoize
        envelopes_to_probabilities[fset] = this_envelope_value

        return this_envelope_value

    initial_envelope = Counter([16])
    dfs(initial_envelope, 0)

    answer = round(
        envelopes_to_probabilities[convert_counter_to_frozenset(initial_envelope)], 6
    )
    print(
        f"The expected number of times a single piece of paper is found in the envelope:\
          \n\n\t{answer}\n"
    )


def remove_piece_from_envelope(piece: int, envelope: Counter) -> None:
    """Remove a piece of paper of the given size from the envelope.

    NOTE This function modifies its input arguments.
    """
    if envelope[piece] == 1:
        del envelope[piece]
    else:
        envelope[piece] -= 1


def add_new_pieces_from_piece_to_envelope(piece: int, envelope: Counter) -> None:
    """Add new pieces torn from the given piece to the envelope.

    NOTE: This function modifies its input arguments.
    """
    size_to_add = piece // 2
    while size_to_add >= 1:
        envelope[size_to_add] += 1
        size_to_add = size_to_add // 2


def convert_counter_to_frozenset(counter: Counter) -> frozenset:
    """Convert the Counter to a frozenset.

    This is useful for hashing and memoization.
    """
    return frozenset(counter.items())


if __name__ == "__main__":
    main()
