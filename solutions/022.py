#!/usr/bin/python3
'''
Using names.txt (right click and 'Save Link/Target As...'),
a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order,
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

from helpers import print_memory_usage_report, print_time_elapsed
from time import time
import tracemalloc


def main():
    # Keep track of time elapsed and memory used
    start_time = time()
    tracemalloc.start()

    # ********** Solution begins here ********** #

    with open('022_names.txt', 'r') as names_file:
        names = names_file.read()

    names = [name.strip().replace('\"', '') for name in sorted(names.split(','))]

    total_score = 0
    for index, name in enumerate(names):
        sum_of_letter_values = 0
        for letter in name:
            sum_of_letter_values += ord(letter.lower()) - ord('a') + 1
        total_score += sum_of_letter_values * (index + 1)

    print(f'Sum of all names scores in the file:\n\n\t{total_score}\n')

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
