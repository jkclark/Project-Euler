#!/usr/bin/python3
'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'),
a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route
to solve this problem, as there are 2^99 altogether! If you could check one trillion (10^12) routes
every second it would take over twenty billion years to check them all.
There is an efficient algorithm to solve it. ;o)
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

    if row == triangle_height - 1:  # This is the bottom of the triangle
        return current_value

    left_child = triangle[row + 1][col]
    right_child = triangle[row + 1][col + 1]

    if row == triangle_height - 2:  # This is the second-to-last row in the triangle
        return max(left_child, right_child) + current_value

    left_left_max_path_sum = left_child + _recursive_max_path_sum(row + 2, col)

    if left_child > right_child:
        middle_max_path_sum = left_child + _recursive_max_path_sum(row + 2, col + 1)
    else:
        middle_max_path_sum = right_child + _recursive_max_path_sum(row + 2, col + 1)

    right_right_max_path_sum = right_child + _recursive_max_path_sum(row + 2, col + 2)

    best = current_value + max(
        left_left_max_path_sum,
        middle_max_path_sum,
        right_right_max_path_sum
    )

    memo[(row, col)] = best
    return best


def main():
    # Keep track of time elapsed and memory used
    start_time = time()
    tracemalloc.start()

    # ********** Solution begins here ********** #
    global triangle, triangle_height

    # Parse triangle input into lists of ints
    with open('067_triangle.txt', 'r') as triangle_file:
        triangle = triangle_file.read()

    triangle = triangle.split('\n')
    triangle = triangle[:-1]  # Ignore the first and last newline chars
    triangle_height = len(triangle)

    for index in range(len(triangle)):
        triangle[index] = [int(num) for num in triangle[index].split()]

    # Find the max path via recursion
    max_path_sum = _recursive_max_path_sum(0, 0)

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
