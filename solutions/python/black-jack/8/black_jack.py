"""Functions to help play and score a game of blackjack."""


def value_of_card(card: str) -> int:
    """Return the scoring value of a card."""

    if card in {"J", "Q", "K"}:
        return 10

    if card == "A":
        return 1

    return int(card)


def higher_card(card_one: str, card_two: str) -> str | tuple[str, str]:
    """Return the higher card or both cards if their values are equal."""

    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    if value_one > value_two:
        return card_one

    if value_two > value_one:
        return card_two

    return card_one, card_two


def value_of_ace(card_one: str, card_two: str) -> int:
    """Return the most advantageous value for an upcoming ace."""

    total = value_of_card(card_one) + value_of_card(card_two)

    if "A" in {card_one, card_two}:
        return 1

    return 11 if total <= 10 else 1


def is_blackjack(card_one: str, card_two: str) -> bool:
    """Check whether the hand is a natural blackjack."""

    cards = {card_one, card_two}

    return "A" in cards and any(
        card in {"10", "J", "Q", "K"} for card in cards
    )


def can_split_pairs(card_one: str, card_two: str) -> bool:
    """Check whether two cards can be split into separate hands."""

    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one: str, card_two: str) -> bool:
    """Check whether the hand qualifies for a double down."""

    total = value_of_card(card_one) + value_of_card(card_two)

    return total in {9, 10, 11}