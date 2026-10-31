"""Functions for tracking poker hands and assorted card tasks."""

def get_rounds(number):
    return [number, number + 1, number + 2]

def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2

def list_contains_round(rounds, number):
    return number in rounds

def card_average(hand):
    return sum(hand) / len(hand)

def approx_average_is_average(hand):
    promedio = sum(hand) / len(hand)
    promedio_extremos = (hand[0] + hand[-1]) / 2
    mediana = hand[len(hand) // 2]

    return promedio_extremos == promedio or mediana == promedio

def average_even_is_average_odd(hand):
    pares = hand[::2]
    impares = hand[1::2]

    promedio_pares = sum(pares) / len(pares)
    promedio_impares = sum(impares) / len(impares)

    return promedio_pares == promedio_impares

def maybe_double_last(hand):
    resultado = hand.copy()

    if resultado[-1] == 11:
        resultado[-1] *= 2

    return resultado
