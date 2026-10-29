"""Functions to help play and score a game of blackjack.

How to play blackjack: https://bicyclecards.com/how-to-play/blackjack/
Standard playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""

def value_of_card(card):
    """Determine the scoring value of a card."""
    if card in ("J", "Q", "K"):
        return 10
    if card == "A":
        return 1
    return int(card)

def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand."""
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    if value_one > value_two:
        return card_one
    if value_two > value_one:
        return card_two
    return card_one, card_two

def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card."""
    total = value_of_card(card_one) + value_of_card(card_two)

    if "A" in (card_one, card_two):
        return 1
    if total + 11 <= 21:
        return 11
    return 1

def is_blackjack(card_one, card_two):
    """Determine if the hand is a natural blackjack."""
    cards = (card_one, card_two)

    return "A" in cards and any(
        card in ("10", "J", "Q", "K") for card in cards
    )

def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand."""
    return value_of_card(card_one) == value_of_card(card_two)

def can_double_down(card_one, card_two):
    """Determine if the hand can be doubled down."""
    total = value_of_card(card_one) + value_of_card(card_two)
    return total in (9, 10, 11)
