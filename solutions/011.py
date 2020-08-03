#!/usr/bin/python3
'''
In the 20×20 grid below, four numbers along a diagonal line
have been marked in red (you can't see it here).

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the
same direction (up, down, left, right, or diagonally) in the 20×20 grid?
'''

from helpers import print_memory_usage_report, print_time_elapsed
from time import time
import tracemalloc

from functools import reduce
from operator import mul


GRID_SIZE = 20
num_grid = []


def _get_grid_value(row: int, col: int) -> int:
    '''Get the value of the grid at (row, col), or 1 if (row, col) is an invalid location.'''
    if row < 0 or col < 0 or row >= GRID_SIZE or col >= GRID_SIZE:
        return 1

    return num_grid[row][col]


def _straight(row: int, col: int, direction: str) -> int:
    '''Get the product of four adjacent numbers starting at (row, col) and moving "towards" direction.

    Args:
        row (int): The row at which to begin
        col (int): The column at which to begin
        direction (str): Either 'S' (for South) or 'E' (for East)
    '''
    return reduce(
        mul,
        [
            _get_grid_value(row + delta, col) if direction == 'S' else _get_grid_value(row, col + delta)
            for delta in range(4)
        ],
        1
    )


def _diagonal(row: int, col: int, direction: str) -> int:
    '''Get the product of four adjacent numbers starting at (row, col) and moving "towards" direction.

    Args:
        row (int): The row at which to begin
        col (int): The column at which to begin
        direction (str): Either 'SE' (for Southeast) or 'NE' (for Northeast)
    '''
    return reduce(
        mul,
        [
            _get_grid_value(row + d, col + d) if direction == 'SE' else _get_grid_value(row - d, col + d)
            for d in range(4)
        ],
        1
    )


def main():
    # Keep track of time elapsed and memory used
    start_time = time()
    tracemalloc.start()

    # ********** Solution begins here ********** #
    # Load number grid
    global num_grid
    num_grid = '''
        08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
        49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
        81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
        52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
        22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
        24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
        32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
        67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
        24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
        21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
        78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
        16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
        86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
        19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
        04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
        88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
        04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
        20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
        20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
        01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
    '''

    # Format number grid into GRID_SIZE lists of length GRID_SIZE
    num_grid = num_grid.split()
    num_grid = [
        [
            int(num)
            for num in num_grid[index: index + GRID_SIZE]
        ]
        for index in range(0, GRID_SIZE ** 2, GRID_SIZE)
    ]

    # Iterate over every position, checking down, right, down-right (Southeast) and up-right (Northeast)
    max_product = 0
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            max_product = max(
                max_product,
                _straight(row, col, 'S'),
                _straight(row, col, 'E'),
                _diagonal(row, col, 'SE'),
                _diagonal(row, col, 'NE')
            )

    print(f'Greatest product of four adjacent numbers:\n\n\t{max_product}\n')

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
