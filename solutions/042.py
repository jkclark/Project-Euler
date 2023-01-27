#!/usr/bin/env python3
"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values
we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is
a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly
two-thousand common English words, how many are triangle words?
"""

from helpers import print_memory_usage_report, print_time_elapsed
from time import time
import tracemalloc


def get_letter_value(letter: str):
    """Get a letter's 'value.' A = 1, J = 10, Z = 26."""
    return ord(letter) - 65 + 1  # 65 = 'A' 's ASCII value, +1 because A is 1 not 0 in this problem


def get_triangle_numbers(num_to_get):
    """Return an array of triangle numbers num_to_get long."""
    return [int(0.5 * n * (n + 1)) for n in range(1, num_to_get + 1)]


def main():
    # Keep track of time elapsed and memory used
    start_time = time()
    tracemalloc.start()

    # ********** Solution begins here ********** #

    with open("./042_words.txt") as words_file:
        words = words_file.read().replace('"', "").split(",")

    triangle_nums = set(get_triangle_numbers(20))

    num_triangle_words = 0
    for word in words:
        word_value = sum(get_letter_value(letter) for letter in word)
        if word_value in triangle_nums:
            num_triangle_words += 1

    print(f"Number of triangle words in text file:\n\n\t{num_triangle_words}\n")

    # ********** Solution ends here ********** #

    # Stop tracking time and memory
    snapshot = tracemalloc.take_snapshot()
    end_time = time()
    tracemalloc.stop()

    # Print time elapsed and memory used
    print_time_elapsed(start_time, end_time)
    print_memory_usage_report(snapshot)


if __name__ == "__main__":
    main()
