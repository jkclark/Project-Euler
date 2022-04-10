#!/usr/bin/env python3
'''
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.

(There was a matrix written in LaTeX but it didn't copy over.)

Find the minimal path sum from the top left to the bottom right by only moving right and down in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.
'''

from helpers import print_memory_usage_report, print_time_elapsed
from time import time
import tracemalloc


minimum_path_sums = None
matrix = None


def _find_minimum_path_sum_to_coordinate(row: int, col: int) -> int:
    # Base case/memoization case
    if minimum_path_sums[row][col] is not None:
        return minimum_path_sums[row][col]

    # Find minimum path sum if come from left
    if col <= 0:  # We are on the left side of the matrix
        left_minimum_path_sum = float('inf')
    else:
        left_minimum_path_sum = _find_minimum_path_sum_to_coordinate(row, col - 1)

    # Find minimum path sum if come from above
    if row <= 0:  # We are at the top of the matrix
        up_minimum_path_sum = float('inf')
    else:
        up_minimum_path_sum = _find_minimum_path_sum_to_coordinate(row - 1, col)

    # Compare, save, and return
    minimum_path_sum = matrix[row][col] + min(left_minimum_path_sum, up_minimum_path_sum)
    minimum_path_sums[row][col] = minimum_path_sum
    return minimum_path_sum


def main():
    # Keep track of time elapsed and memory used
    start_time = time()
    tracemalloc.start()

    # ********** Solution begins here ********** #

    '''
    We need to make 79 moves to the right and 79 moves down. The problem asks us to choose the order
    of these right and down moves to minimize the sum of the numbers encountered.

    Obviously, we can't check every path through the matrix. Also obviously, we need to visit every
    number at least once.

    It seems to me we could approch this recursively, but I'm not sure if it's the best approach yet.
    We can view it like this: let's start at the end. From the end, we need to decide if we want to
    have come from the top or from the left. The minimum path sum which comes from either direction
    will be equal to the minimum path sum which goes to that number, plus the value of that number.

    We can remember what the minimum path sum to any given number storing minimum path sums in an array
    (memoization).
    '''

    global matrix, minimum_path_sums

    # Parse matrix input into lists of ints
    with open('081_matrix.txt', 'r') as matrix_file:
        unparsed_matrix = matrix_file.read()

    unparsed_matrix = unparsed_matrix.split('\n')
    unparsed_matrix = unparsed_matrix[:-1]
    matrix = []
    for line in unparsed_matrix:
        matrix.append([int(num) for num in line.split(',')])

    # Prepare memoization grid
    minimum_path_sums = [
        [None for _ in range(len(matrix[0]))]
        for _ in range(len(matrix))
    ]

    # Insert the top-left number into the memo grid
    minimum_path_sums[0][0] = matrix[0][0]

    # Find minimum path sum to bottom-right corner recursively
    minimum_path_sum = _find_minimum_path_sum_to_coordinate(len(matrix) - 1, len(matrix[-1]) - 1)

    print(f'The minimal path sum from the top left to the bottom right by only moving right and down:\n\n\t{minimum_path_sum}\n')

    # ********** Solution ends here ********** #

    # Stop tracking time and memory
    snapshot = tracemalloc.take_snapshot()
    end_time = time()
    tracemalloc.stop()

    # Print time elapsed and memory used
    print_time_elapsed(start_time, end_time)
    print_memory_usage_report(snapshot)


if __name__ == '__main__':
    main()
