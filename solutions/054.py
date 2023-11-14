#!/usr/bin/env python3
"""
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand	 	Player 1	 	Player 2	 	Winner
1	 	5H 5C 6S 7S KD
Pair of Fives
 	2C 3S 8S 8D TD
Pair of Eights
 	Player 2
2	 	5D 8C 9S JS AC
Highest card Ace
 	2C 5C 7D 8S QH
Highest card Queen
 	Player 1
3	 	2D 9C AS AH AC
Three Aces
 	3D 6D 7D TD QD
Flush with Diamonds
 	Player 2
4	 	4D 6S 9H QH QC
Pair of Queens
Highest card Nine
 	3D 6D 7H QD QS
Pair of Queens
Highest card Seven
 	Player 1
5	 	2H 2D 4C 4D 4S
Full House
With Three Fours
 	3C 3D 3S 9S 9D
Full House
with Three Threes
 	Player 1
The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
"""
from collections import Counter
from enum import Enum, auto
from typing import List

from helpers import measure_time_and_memory


@measure_time_and_memory
def main():
    """Calculate the number of hands won by player 1."""
    with open("./solutions/054_poker.txt", "r", encoding="utf-8") as poker_hands_file:
        hands = poker_hands_file.readlines()

    player_1_wins = 0
    for hand_cards in hands:
        cards = [
            Card(card_str[0], card_str[1]) for card_str in hand_cards.strip().split(" ")
        ]
        player_1_wins += Hand(cards[:5]).beats(Hand(cards[5:]))

    print(f"Number of hands won by Player 1:\n\n\t{player_1_wins}\n")


class Card:
    """A representation of a single card."""

    def __init__(self, value: str, suit: str) -> None:
        self.suit = suit
        self.str = f"{value}{suit}"

        try:
            self.value = CardValue[value].value
        except KeyError:
            self.value = int(value)

    def __str__(self) -> str:
        return self.str


class HandRank(Enum):
    """
    An enumeration of the different poker hand ranks.

    Notice that a royal flush is just a straight flush with high card Ace.
    """

    HIGH_CARD = auto()
    ONE_PAIR = auto()
    TWO_PAIRS = auto()
    THREE_OF_A_KIND = auto()
    STRAIGHT = auto()
    FLUSH = auto()
    FULL_HOUSE = auto()
    FOUR_OF_A_KIND = auto()
    STRAIGHT_FLUSH = auto()


class Hand:
    """A representation of a hand of cards."""

    def __init__(self, cards: List[Card]) -> None:
        if len(cards) != 5:
            raise ValueError("Hand does not have exactly 5 cards")

        self.single_cards = []
        self.pairs = []
        self.three_of_a_kind = None  # There can only be one
        self.four_of_a_kind = None  # There can only be one
        self.straight = self.are_cards_consecutive(cards)
        self.flush = len(Counter([card.suit for card in cards])) == 1

        # Iterate over hand card values and their counts
        for value, count in Counter([card.value for card in cards]).items():
            if count == 1:
                self.single_cards.append(value)

            if count == 2:
                self.pairs.append(value)

            if count == 3:
                self.three_of_a_kind = value

            if count == 4:
                self.four_of_a_kind = value

        self.single_cards = list(reversed(sorted(self.single_cards)))
        self.pairs = list(reversed(sorted(self.pairs)))

        self.rank = self.get_rank()

    @staticmethod
    def are_cards_consecutive(cards: List[Card]) -> bool:
        "Return True if cards are consecutive values, False otherwise."
        values = [card.value for card in cards]
        return sorted(values) == list(range(min(values), max(values) + 1))

    def get_rank(self) -> HandRank:
        "Determine this hand's rank."
        if self.straight and self.flush:
            return HandRank.STRAIGHT_FLUSH.value

        if self.four_of_a_kind:
            return HandRank.FOUR_OF_A_KIND.value

        if self.three_of_a_kind and self.pairs:
            return HandRank.FULL_HOUSE.value

        if self.flush:
            return HandRank.FLUSH.value

        if self.straight:
            return HandRank.STRAIGHT.value

        if self.three_of_a_kind:
            return HandRank.THREE_OF_A_KIND.value

        if len(self.pairs) == 2:
            return HandRank.TWO_PAIRS.value

        if self.pairs:
            return HandRank.ONE_PAIR.value

        return HandRank.HIGH_CARD.value

    def beats(self, other: "Hand") -> bool:
        """Return True if this hand beats the given hand, False otherwise."""
        if self.rank > other.rank:
            return True

        if self.rank < other.rank:
            return False

        # Compare 4's of a kind
        if (
            self.four_of_a_kind is not None
            and self.four_of_a_kind != other.four_of_a_kind
        ):
            return self.four_of_a_kind > other.four_of_a_kind

        # Compare 3's of a kind
        if (
            self.three_of_a_kind is not None
            and self.three_of_a_kind != other.three_of_a_kind
        ):
            return self.three_of_a_kind > other.four_of_a_kind

        # Compare pairs
        for own_pair, other_pair in zip(self.pairs, other.pairs):
            if own_pair != other_pair:
                return own_pair > other_pair

        # Compare high cards
        for own_single, other_single in zip(self.single_cards, other.single_cards):
            if own_single != other_single:
                return own_single > other_single

        raise ValueError("Hands are exactly tied!")


class CardValue(Enum):
    """An enumeration of the non-digit card values."""

    T = 10
    J = 11
    Q = 12
    K = 13
    A = 14


if __name__ == "__main__":
    main()
