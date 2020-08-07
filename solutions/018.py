#!/usr/bin/python3
'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
However, Problem 67, is the same challenge with a triangle containing one-hundred rows;
it cannot be solved by brute force, and requires a clever method! ;o)
'''

from helpers import print_memory_usage_report, print_time_elapsed
from time import time
import tracemalloc


triangle = []
triangle_height = 0

memo = {}


def _recursive_max_path_sum(row: int, col: int) -> int:
    if (row, col) in memo:  # Memoization
        return memo[(row, col)]

    current_value = triangle[row][col]

    if row == triangle_height - 1:  # This is the bottom row of the triangle
        return current_value

    left_child = triangle[row + 1][col]
    right_child = triangle[row + 1][col + 1]

    if row == triangle_height - 2:  # This is the second-to-last row in the triangle
        return max(left_child, right_child) + current_value

    # Do the path current -> left -> left
    left_left_max_path_sum = left_child + _recursive_max_path_sum(row + 2, col)

    # Choose the maximum of (left, right) and then pursue the middle path
    if left_child > right_child:
        middle_max_path_sum = left_child + _recursive_max_path_sum(row + 2, col + 1)
    else:
        middle_max_path_sum = right_child + _recursive_max_path_sum(row + 2, col + 1)

    # Do the path current -> right -> right
    right_right_max_path_sum = right_child + _recursive_max_path_sum(row + 2, col + 2)

    # Get the maximum value
    best = current_value + max(
        left_left_max_path_sum,
        middle_max_path_sum,
        right_right_max_path_sum
    )

    memo[(row, col)] = best
    return best


def _top_down_max_path_sum() -> int:
    '''Starting at the top, add to each node the greater of that node's parents. Return the max of the last row.'''
    for row in range(1, triangle_height):
        for col in range(row + 1):  # Row k has k + 1 elements
            if col == 0:  # The first element in each row has only one parent (except for the top row)
                triangle[row][col] += triangle[row - 1][col]

            elif col == row:  # The last element in each row has only one parent (except for the top row)
                triangle[row][col] += triangle[row - 1][col - 1]

            else:
                triangle[row][col] += max(triangle[row - 1][col - 1], triangle[row - 1][col])

    return max(triangle[triangle_height - 1])


def _bottom_up_max_path_sum() -> int:
    '''Starting at the bottom, add to each node the greater of that node's children. Return the top node's value.'''
    for row in range(triangle_height - 2, -1, -1):
        for col in range(row + 1):
            triangle[row][col] += max(triangle[row + 1][col], triangle[row + 1][col + 1])

    return triangle[0][0]


def main():
    # Keep track of time elapsed and memory used
    start_time = time()
    tracemalloc.start()

    # ********** Solution begins here ********** #
    global triangle, triangle_height
    triangle = '''
        75
        95 64
        17 47 82
        18 35 87 10
        20 04 82 47 65
        19 01 23 75 03 34
        88 02 77 73 07 63 67
        99 65 04 28 06 16 70 92
        41 41 26 56 83 40 80 70 33
        41 48 72 33 47 32 37 16 94 29
        53 71 44 65 25 43 91 52 97 51 14
        70 11 33 28 77 73 17 78 39 68 17 57
        91 71 52 38 17 14 91 43 58 50 27 29 48
        63 66 04 68 89 53 67 30 73 16 69 87 40 31
        04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
    '''

    # Parse triangle input into lists of ints
    triangle = triangle.split('\n')
    triangle = triangle[1:-1]  # Ignore the first and last newline chars
    triangle_height = len(triangle)

    for index in range(len(triangle)):
        triangle[index] = [int(num) for num in triangle[index].split()]

    # Find the max path sum
    #  max_path_sum = _recursive_max_path_sum(0, 0)
    #  max_path_sum = _top_down_max_path_sum()
    max_path_sum = _bottom_up_max_path_sum()

    print(f'Maximum total of adjacent numbers in the triangle from top to bottom:\n\n\t{max_path_sum}\n')

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
