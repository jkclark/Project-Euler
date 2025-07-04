#!/usr/bin/env python3
"""

"""

from helpers import measure_time_and_memory


@measure_time_and_memory
def main():
    """
    I think we basically need to work right to left throughout the matrix, memoizing the lowest
    cost to get from the current number to the right side of the screen. For numbers in the rightmost
    column, the minimum path sum (MPS) is obviously just their value. For numbers in the second rightmost column,
    their MPS is the minimum of their top, right, and down neighbors, plus their own value.

    I think one strategy is to do one column at a time, starting from the right. (Again, the rightmost column is straightforward)
    We evaluate each square by first considering only down and right moves.
    This means evaluating from the bottom of the column to the top.
    The bottommost number's value is simply its own value plus its right neighbor's value. The next one up
    is either it's right neighbor or it's downward neighbor's MPS. We do this until we get to the top of the row.
    Then we do the same for the same column, but we only consider *up* and right moves, starting from the top.
    Once we have both of these arrays (down/right and up/right), we can iterate over both of them to determine
    the minimum value for each number in that column. Then we can restart this algorithm with the next column over,
    and using the previous column's MPS's. We continue to iterate until we compute these values for the leftmost
    column.

    I feel like there might be a hole in this algorithm, but I'm gonna leave it like this for now.
    """
    # Read matrix
    matrix = read_matrix("082_matrix.txt", "r")

    print(f":\n\n\t{None}\n")


def read_matrix(filepath: str) -> list[list[int]]:
    # Parse matrix input into lists of ints
    with open(filepath, 'r') as matrix_file:
        unparsed_matrix = matrix_file.read()

    unparsed_matrix = unparsed_matrix.split('\n')
    unparsed_matrix = unparsed_matrix[:-1]
    matrix = []
    for line in unparsed_matrix:
        matrix.append([int(num) for num in line.split(',')])



if __name__ == "__main__":
    main()
