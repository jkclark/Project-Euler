#!/usr/bin/env python3
"""
A common security method used for online banking is to ask the user for three
random characters from a passcode. For example, if the passcode was 531278, they
may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file
so as to determine the shortest possible secret passcode of unknown length
"""
from typing import List

import networkx as nx

from helpers import measure_time_and_memory


@measure_time_and_memory
def main():
    """Find the shortest possible secret passcode.

    In the end, this is a topological-ordering graph problem. See the docstring below
    for more.
    """
    # Shorter path required for running in interactive window (without messing with settings)
    # with open("./079_keylog.txt", "r", encoding="ascii") as keylog_file:
    with open("./solutions/079_keylog.txt", "r", encoding="ascii") as keylog_file:
        attempts = [int(attempt) for attempt in keylog_file.readlines()]

    attempts = sorted(list(set(attempts)))

    graph_connections(attempts)

    print(
        "The shortest possible secret passcode:\n\n\t(Solved by hand with help from graph)\n"
    )


def graph_connections(attempts: List[int]) -> None:
    """Graph the connections between digits in attempts.

    Each node represents a digit and directed connection to another node
    represents the source-node digit preceding the destination-node digit
    in an attempt. The weights represent the number of times this occurs
    in all attempts.

    I solved this problem by noticing nodes that only had either incoming OR
    outgoing edges, not both. At first, we see that 7 has only outgoing edges,
    so no digit precedes it in the passcode. This means we can set 7 as the first
    digit of the passcode. At the same time, 0 has only incoming edges, so it can
    serve as the last digit of the passcode.

    After that, I redrew the graph without those two nodes. A similar pattern emerged:
    9 had only incoming edges, so it could be the second-to-last digit in the passcode.
    Continuing in this way we find the whole shortest possible passcode.
    """
    graph = nx.DiGraph()

    # Add nodes
    # Step 0: graph.add_nodes_from(range(10))
    # Step 1a: 4 and 5 are not included in any attempts
    # Step 1b: 7 is not preceded by any digit
    # Step 1c: 0 does not precede any digit
    # Step 2: With the above nodes removed, 9 does not precede any digits
    # Step 3: With the above nodes removed, 3 is not preceded by any digit
    # Step 4: With the above nodes removed, 1 is not preceded by any digit
    # Step 5a: With the above nodes removed, 6 is not preceded by any digit
    # Step 5b: With the above nodes removed, 8 does not precede any digits
    nodes = [2, 6, 8]
    graph.add_nodes_from(nodes)

    # Add edges
    for attempt in attempts:
        digits = get_digits_of_attempt(attempt)

        ## Add first digit -> second digit edge
        first_edge = [digits[0], digits[1]]
        # Only add edge if both digits in graph
        if all(digit in nodes for digit in first_edge):
            graph.add_edge(*first_edge)

        ## Add second digit -> third digit edge
        second_edge = [digits[1], digits[2]]
        # Only add edge if both digits in graph
        if all(digit in nodes for digit in second_edge):
            graph.add_edge(*second_edge)

    # Set node positions
    positions = {
        0: (0, 2.5),
        1: (1, 1.5),
        2: (2, 0.5),
        3: (2, -0.5),
        4: (1, -1.5),
        5: (0, -2.5),
        6: (-1, -1.5),
        7: (-2, -0.5),
        8: (-2, 0.5),
        9: (-1, 1.5),
    }

    nx.draw_networkx(graph, positions)


def get_digits_of_attempt(attempt: int) -> List[int]:
    """Convert an attempt into a list of its digits."""
    return [int(digit) for digit in str(attempt)]


if __name__ == "__main__":
    main()
