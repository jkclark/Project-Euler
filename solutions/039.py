#!/usr/bin/env python3
'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''

from helpers import print_memory_usage_report, print_time_elapsed
from time import time
import tracemalloc

from math import ceil, floor, sqrt


def _is_right_triangle(a: int, b: int, c: int) -> bool:
    '''Return whether or not the given lengths form a right triangle.'''
    return a ** 2 + b ** 2 == c ** 2


def _find_a_b_given_c_p(c: int, p: int):
    '''Find the integer pair (a, b) given hypotenuse length c, if it exists.'''
    # Binary search
    # TODO: Implement binary search

    # Linear search
    for a in range(1, c):
        if _is_right_triangle(a, (p - c - a), c):
            return True

    return False

def _find_right_triangles_given_perimeter(perimeter: int) -> int:
    '''Find the number of solutions for right triangle lengths given the triangle's perimeter.'''
    # What is the best upper bound we can find for c given perimeter?
    # We know that c < p/2, since the sum of any two sides of a triangle is greater than the third.
    # We also know that c < p/2, since a^2 + a^2 < (2a) ^ 2 and also 1^2 + (p/2-1)^2 < (p/2)^2

    # What is the best lower bound we can find for c given perimeter?
    # What if c starts at p/3, meaning a = b = c
    # Well, then
    solutions = 0
    for c in range(floor(perimeter / 3), ceil(perimeter / 2) + 1):
        if _find_a_b_given_c_p(c, perimeter):
            solutions += 1

    return solutions


def main():
    # Keep track of time elapsed and memory used
    start_time = time()
    tracemalloc.start()

    # ********** Solution begins here ********** #

    '''
    a + b + c = p
    a^2 + b^2 = c^2

    We can fix c and then vary a/b
    p - c = a + b

    How to find (a, b)? Can we do binary search?
    a^2 + b^2 = c^2
    We have c^2
    a,b can be swapped WLG
    Idea: Maybe we can start with a = b = (p - c)/2 (break if any non ints involved)
    - If the sum is too high (a^2 + b^2 > c^2)

    p = 12
    c = 2 (loop var)
    a = b = (p - c) / 2 = (12 - 2) / 2 = 5
    This would mean 5^2 + 5^2 = 2^2... obviously untrue
    We can vary a,b to the following values:
    4, 6 => 4^2 + 6^2 = 52
    3, 7 => 3^2 + 7^2 = 58
    2, 8 => 2^2 + 8^2 = 68
    1, 9 => 1^2 + 9^2 = 82

    From this it would appear that starting with a = b yields the lowest possible value
    and that a = 1, b = (p - c) / 2 - 1 yields the highest possible value. I think
    binary search is applicable here.

    Given this the algorithm's runtime can be described in the following way:

    Loop 1 -> 1000 (called n):                 O(1)
        Loop 1 -> n (called c):                O(n^2)
            Binary search for (a, b)           O(log(c))

    Question: Can there be multiple solutions (a, b) where a^2 + b^2 = c^2 ?
    It feels like the answer is yes. If you draw one side of a triangle (hypotenuse),
    have you fixed the location of where (a, b) meet, and therefore their lengths? It
    seems like it..?

    Given p, what is the highest number we need to check for c?
    It is certain that c < p/2, because the sum of any two sides of a triangle
    is greater than the length of the third side. Additionally,
    If c = p/2, that means that a^2 + b^2 =?= c^2 where a + b = c.
    This will never be the case, so that's a starting point.

    Given p, what is the lowest number we need to check for c?
    If c = p/3, then a = b = c. This is an equilateral triangle, where
    all angles are 60deg. If we want one of the angles to be bigger (i.e., 90deg),
    we need to lengthen one of the sides (i.e., the hypotenuse).

    It would seem that we can check c where p/3 < c < p/2.
    '''

    max_perimeter = None
    max_solutions = 0

    for perimeter in range(1, 1001):
        if (number_of_solutions := _find_right_triangles_given_perimeter(perimeter)) > max_solutions:
            max_perimeter = perimeter
            max_solutions = number_of_solutions

    print(f'The value of p which maximizes the number of solutions:\n\n\t{max_perimeter}\n')

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
