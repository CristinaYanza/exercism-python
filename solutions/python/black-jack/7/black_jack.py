"""Functions to help play and score a game of blackjack.

How to play blackjack: https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""

def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.
    """

    if card in 'JQK':
        return 10

    if card == 'A':
        return 1

    return int(card)

def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt.
    :return: higher value card - str. Tuple of both cards if equal.
    """

    if value_of_card(card_one) > value_of_card(card_two):
        return card_one

    if value_of_card(card_one) < value_of_card(card_two):
        return card_two

    return card_one, card_two

def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - cards dealt.
    :return: int - value of the upcoming ace card (1 or 11).
    """

    if card_one == 'A' or card_two == 'A':
        return 1

    return 11 if value_of_card(card_one) + value_of_card(card_two) <= 10 else 1

def is_blackjack(card_one, card_two):
    """Determine if the hand is a natural blackjack.

    :param card_one, card_two: str - cards dealt.
    :return: bool - whether the hand is a blackjack.
    """

    return (card_one == 'A' and value_of_card(card_two) == 10) or (
        card_two == 'A' and value_of_card(card_one) == 10
    )

def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - whether the cards have the same value.
    """

    return value_of_card(card_one) == value_of_card(card_two)

def can_double_down(card_one, card_two):
    """Determine if a player can double down.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - whether the hand totals 9, 10 or 11 points.
    """

    return 9 <= value_of_card(card_one) + value_of_card(card_two) <= 11