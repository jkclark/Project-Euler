#!/usr/bin/env python3
"""
The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the
left column and finishing in any cell in the right column, and only moving up,
down, and right, is indicated in red and bold; the sum is equal to 994.

[
    [131, 673, 234, 103,  18],
    [201,  96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524,  37, 331],
]

Find the minimal path sum from the left column to the right column in matrix.txt
(right click and "Save Link/Target As..."), a 31K text file containing an 80 by
80 matrix.
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
    matrix = read_matrix("./solutions/082_matrix.txt")
    # matrix = [
    #     [131, 673, 234, 103, 18],
    #     [201, 96, 342, 965, 150],
    #     [630, 803, 746, 422, 111],
    #     [537, 699, 497, 121, 956],
    #     [805, 732, 524, 37, 331],
    # ]
    MATRIX_NUM_ROWS = len(matrix)
    MATRIX_NUM_COLS = len(matrix[0])

    # Keep track of MPS values
    mps_values = [[0] * MATRIX_NUM_COLS for _ in matrix]

    # Set the last column of mps_values equal to the last column of matrix
    for row in range(MATRIX_NUM_ROWS):
        mps_values[row][-1] = matrix[row][-1]

    # Iterate from right to left, starting at the second-from-the-right column
    for col in range(MATRIX_NUM_COLS - 2, -1, -1):
        down_and_right_mps_values = get_down_and_right_mps_values_for_col(
            col, matrix, mps_values
        )
        up_and_right_mps_values = get_up_and_right_mps_values(col, matrix, mps_values)

        # Set each number's MPS value to the min of these two
        for row in range(MATRIX_NUM_ROWS):
            mps_values[row][col] = min(
                down_and_right_mps_values[row], up_and_right_mps_values[row]
            )

    overall_mps = min([mps_values[row][0] for row in range(MATRIX_NUM_ROWS)])

    print(
        f"The minimal path sum from the left column to the right column:\n\n\t{overall_mps}\n"
    )


def read_matrix(filepath: str) -> list[list[int]]:
    # Parse matrix input into lists of ints
    with open(filepath, "r", encoding="utf-8") as matrix_file:
        unparsed_matrix = matrix_file.read()

    unparsed_matrix = unparsed_matrix.split("\n")
    unparsed_matrix = unparsed_matrix[:-1]
    matrix = []
    for line in unparsed_matrix:
        matrix.append([int(num) for num in line.split(",")])

    return matrix


def get_down_and_right_mps_values_for_col(
    col: int, matrix: list[list[int]], mps_values: list[list[int]]
) -> list[int]:
    # Prepare the output list
    down_and_right_mps_values = [0 for _ in range(len(matrix))]

    # The bottom-most number can only go to the right
    down_and_right_mps_values[-1] = matrix[-1][col] + mps_values[-1][col + 1]

    # Every other number can either go right or go down
    for row in range(len(matrix) - 2, -1, -1):
        down_and_right_mps_values[row] = matrix[row][col] + min(
            down_and_right_mps_values[row + 1], mps_values[row][col + 1]
        )

    return down_and_right_mps_values


def get_up_and_right_mps_values(
    col: int, matrix: list[list[int]], mps_values: list[list[int]]
) -> list[int]:
    # Prepare the output list
    up_and_right_mps_values = [0 for _ in range(len(matrix))]

    # The top-most number can only go to the right
    up_and_right_mps_values[0] = matrix[0][col] + mps_values[0][col + 1]

    # Every other number can either go right or go up
    for row in range(1, len(matrix)):
        up_and_right_mps_values[row] = matrix[row][col] + min(
            up_and_right_mps_values[row - 1], mps_values[row][col + 1]
        )

    return up_and_right_mps_values


if __name__ == "__main__":
    main()
