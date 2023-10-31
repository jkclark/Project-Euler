#!/usr/bin/env python3
"""
In the game, Monopoly, the standard board is set up in the following way:

0084_monopoly_board.png

A player starts on the GO square and adds the scores on two 6-sided dice to
determine the number of squares they advance in a clockwise direction. Without
any further rules we would expect to visit each square with equal probability:
2.5%. However, landing on G2J (Go To Jail), CC (community chest), and CH
(chance) changes this distribution.

In addition to G2J, and one card from each of CC and CH, that orders the player
to go directly to jail, if a player rolls three consecutive doubles, they do not
advance the result of their 3rd roll. Instead they proceed directly to jail.

At the beginning of the game, the CC and CH cards are shuffled. When a player
lands on CC or CH they take a card from the top of the respective pile and,
after following the instructions, it is returned to the bottom of the pile.
There are sixteen cards in each pile, but for the purpose of this problem we are
only concerned with cards that order a movement; any instruction not concerned
with movement will be ignored and the player will remain on the CC/CH square.

Community Chest (2/16 cards):
1. Advance to GO
2. Go to JAIL

Chance (10/16 cards):
1. Advance to GO
2. Go to JAIL
3. Go to C1
4. Go to E3
5. Go to H2
6. Go to R1
7. Go to next R (railway company)
8. Go to next R
9. Go to next U (utility company)
10. Go back 3 squares.

The heart of this problem concerns the likelihood of visiting a particular
square. That is, the probability of finishing at that square after a roll. For
this reason it should be clear that, with the exception of G2J for which the
probability of finishing on it is zero, the CH squares will have the lowest
probabilities, as 5/8 request a movement to another square, and it is the final
square that the player finishes at on each roll that we are interested in. We
shall make no distinction between "Just Visiting" and being sent to JAIL, and we
shall also ignore the rule about requiring a double to "get out of jail",
assuming that they pay to get out on their next turn.

By starting at GO and numbering the squares sequentially from 00 to 39 we can
concatenate these two-digit numbers to produce strings that correspond with sets
of squares.

Statistically it can be shown that the three most popular squares, in order, are
JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO (3.09%) = Square 00. So
these three most popular squares can be listed with the six-digit modal string:
102400.

If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.
"""

from functools import partial
import random
from typing import Callable, List, Tuple

from helpers import measure_time_and_memory


@measure_time_and_memory
def main():
    """Find the 6-digit modal string resulting from using two 4-sided dice."""
    square_names = [
        "GO",
        "A1",
        "CC1",
        "A2",
        "T1",
        "R1",
        "B1",
        "CH1",
        "B2",
        "B3",
        "JAIL",
        "C1",
        "U1",
        "C2",
        "C3",
        "R2",
        "D1",
        "CC2",
        "D2",
        "D3",
        "FP",
        "E1",
        "CH2",
        "E2",
        "E3",
        "R3",
        "F1",
        "F2",
        "U2",
        "F3",
        "G2J",
        "G1",
        "G2",
        "CC3",
        "G3",
        "R4",
        "CH3",
        "H1",
        "T2",
        "H2",
    ]
    square_decks = {
        "CC1": "community chest",
        "CC2": "community chest",
        "CC3": "community chest",
        "CH1": "chance",
        "CH2": "chance",
        "CH3": "chance",
        "G2J": "go to jail",
    }
    squares = [
        Square(index, name, square_decks[name] if name in square_decks else None)
        for index, name in enumerate(square_names)
    ]

    board = Board(squares)

    dice_sides = 4
    turn_limit = 1_000_000
    for _ in range(turn_limit):
        board.do_turn(dice_sides)

    squares_by_popularity = sorted(
        [(square.id_number, square.times_landed_on) for square in squares],
        key=lambda s: s[1],
        reverse=True,
    )

    print(
        f"6-digit string resulting from using two 4-sided dice:\n\n\t\
        {''.join([str(square[0]) for square in squares_by_popularity][:3])}\n"
    )


class Board:
    """Represents a Monopoly board."""

    def __init__(self, squares: List["Square"]) -> None:
        self.player_location = 0
        self.doubles_streak = 0

        self.squares = squares

        # Prepare decks
        def stay_still(location):
            return location

        self.jail_location = self.get_jail_location()
        self.railway_locations = self.get_company_locations("R")
        self.utility_locations = self.get_company_locations("U")
        self.decks = {
            "community chest": Deck(
                [lambda location: 0, lambda location: 10, *[stay_still] * 14]
            ),
            "chance": Deck(
                [
                    lambda location: 0,  # GO
                    lambda location: 10,  # JAIL
                    lambda location: 11,  # C1
                    lambda location: 24,  # E3
                    lambda location: 39,  # H2
                    lambda location: 5,  # R1
                    partial(self.get_next_company_location, self.railway_locations),
                    partial(self.get_next_company_location, self.railway_locations),
                    partial(self.get_next_company_location, self.utility_locations),
                    lambda location: (location - 3) % len(self.squares),
                    *[stay_still] * 6,
                ]
            ),
            "go to jail": Deck([lambda location: self.jail_location]),
        }

        # Shuffle decks
        for deck in self.decks.values():
            deck.shuffle()

    def do_turn(self, dice_sides: int) -> None:
        """Simulate one turn."""
        # Determine roll
        roll = self.roll_n_sided_dice(dice_sides)

        # Deal with doubles
        if roll[0] == roll[1]:
            self.doubles_streak += 1

            # Go to jail for 3 consecutive doubles
            if self.doubles_streak >= 3:
                self.player_location = self.jail_location
                self.squares[self.player_location].times_landed_on += 1

                # Reset doubles streak
                self.doubles_streak = 0

                return
        else:
            self.doubles_streak = 0

        # Determine new location
        self.player_location = (self.player_location + sum(roll)) % len(self.squares)

        # Draw cards until we don't move or there is no deck to draw from
        previous_square = None
        while previous_square != self.player_location:
            # Remember where we are
            previous_square = self.player_location

            # If this square has no deck, we're done
            try:
                deck = self.decks[self.squares[self.player_location].deck]
            except KeyError:
                break

            # Go to square indicated by card
            self.player_location = deck.get_next_card()(self.player_location)

        # Add one to new square's "landed on" count
        self.squares[self.player_location].times_landed_on += 1

    def get_jail_location(self):
        """Get the location of the jail square."""
        for index, square in enumerate(self.squares):
            if square.name == "JAIL":
                return index

    def get_company_locations(self, prefix: str) -> List[int]:
        """Get the indexes of each square whose name starts with the given prefix."""
        return [
            index
            for index, square in enumerate(self.squares)
            if square.name.startswith(prefix)
        ]

    def get_next_company_location(
        self,
        company_locations: int,
        player_location: int,
    ) -> int:
        """Get the location of the next company square.

        company_locations should be in increasing order.
        """
        for company_location in company_locations:
            if player_location < company_location:
                return company_location

        return company_locations[0]

    @staticmethod
    def roll_n_sided_dice(sides: int) -> Tuple[int]:
        """Roll two n-sided dice and return the sum of their values."""
        return (random.randint(1, sides), random.randint(1, sides))


class Square:
    """Represents a square on a Monopoly board."""

    def __init__(self, id_number: int, name: str, deck: "Deck") -> None:
        self.id_number = id_number
        self.name = name
        self.deck = deck

        self.times_landed_on = 0


Card = Callable[[int], int]


class Deck:
    """Represents a deck of cards in a game of Monopoly.

    The deck's cards are represented by functions which take an integer and return another.
    """

    def __init__(self, cards: List[Card]) -> None:
        self.index = 0
        self.cards = cards

    def get_next_card(self) -> Card:
        """Get the next card and increment the pointer."""
        next_card = self.cards[self.index]
        self.index = (self.index + 1) % len(self.cards)
        return next_card

    def shuffle(self) -> None:
        """Shuffle the deck."""
        random.shuffle(self.cards)


def generate_next_int():
    """Yield consecutive integers starting at 0"""


if __name__ == "__main__":
    main()
