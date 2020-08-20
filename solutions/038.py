#!/usr/bin/env python3
'''
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576.
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
and 5, giving the pandigital, 918273645, which is the concatenated product
of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed
as the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''

from helpers import print_memory_usage_report, print_time_elapsed
from time import time
import tracemalloc


def main():
    # Keep track of time elapsed and memory used
    start_time = time()
    tracemalloc.start()

    # ********** Solution begins here ********** #

    max_pandigital = 918273645  # Given in the question
    for num in range(90, 10_000):  # The source number can't be 5 digits long, because 2 * 5 digits = at least 5 digits
        concatenated = str(num)
        multiple = 2
        while len(concatenated) < 9:
            concatenated += str(num * multiple)
            multiple += 1

        # 49 is the ASCII code for '1' and 57 is the ASCII code for '9'
        if len(concatenated) == 9 and all(chr(code) in concatenated for code in range(49, 58)):
            max_pandigital = max(max_pandigital, int(concatenated))

    print(f'Largest pandigital 9-digit number formed as concatenated product:\n\n\t{max_pandigital}\n')

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
