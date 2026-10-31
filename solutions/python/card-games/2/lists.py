"""Functions for tracking poker hands and assorted card tasks."""

def get_rounds(number):
    """Returns the current round and the next two rounds."""
    return [number, number + 1, number + 2]

def concatenate_rounds(rounds_1, rounds_2):
    """Combines two lists of rounds."""
    return rounds_1 + rounds_2

def list_contains_round(rounds, number):
    """Checks whether a round exists in the list."""
    return number in rounds

def card_average(hand):
    """Calculates the average value of the cards."""
    return sum(hand) / len(hand)

def approx_average_is_average(hand):
    """Checks whether an approximate average matches the actual average."""
    promedio = card_average(hand)
    promedio_extremos = (hand[0] + hand[-1]) / 2
    mediana = hand[len(hand) // 2]

    return promedio in (promedio_extremos, mediana)

def average_even_is_average_odd(hand):
    """Checks whether even and odd index averages are equal."""
    pares = hand[::2]
    impares = hand[1::2]

    promedio_pares = card_average(pares)
    promedio_impares = card_average(impares)

    return promedio_pares == promedio_impares

def maybe_double_last(hand):
    """Doubles the last card if it is a Jack (11)."""
    resultado = hand.copy()

    if resultado[-1] == 11:
        resultado[-1] *= 2

    return resultado