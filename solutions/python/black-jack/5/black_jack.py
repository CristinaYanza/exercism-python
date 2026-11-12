"""Functions to help play and score a game of blackjack."""

def value_of_card(card):
    """Determine the scoring value of a card."""

    if card in ["J", "Q", "K"]:
        return 10
    elif card == "A":
        return 1
    else:
        return int(card)

def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand."""

    value1 = value_of_card(card_one)
    value2 = value_of_card(card_two)

    if value1 > value2:
        return card_one
    elif value2 > value1:
        return card_two
    else:
        return card_one, card_two

def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card."""

    def card_value(card):
        """Determine the value of a card, considering an ace as 11."""

        if card in ["J", "Q", "K"]:
            return 10
        elif card == "A":
            return 11
        else:
            return int(card)

    total = card_value(card_one) + card_value(card_two)

    if total + 11 <= 21:
        return 11
    else:
        return 1

def is_blackjack(card_one, card_two):
    """Determine if the hand is a natural blackjack."""

    cards = {card_one, card_two}

    return "A" in cards and any(
        card in cards for card in ["10", "J", "Q", "K"]
    )

def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands."""

    return value_of_card(card_one) == value_of_card(card_two)

def can_double_down(card_one, card_two):
    """Determine if the hand can be doubled down."""

    total = value_of_card(card_one) + value_of_card(card_two)

    return total in [9, 10, 11]