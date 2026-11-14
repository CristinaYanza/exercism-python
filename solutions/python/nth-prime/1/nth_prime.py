"""Find the nth prime number."""

def prime(number):
    """Return the nth prime number."""

    if number < 1:
        raise ValueError("there is no zeroth prime")

    count = 0
    candidate = 1

    while count < number:
        candidate += 1

        if candidate > 2 and candidate % 2 == 0:
            continue

        is_prime = True
        divisor = 3

        while divisor * divisor <= candidate:
            if candidate % divisor == 0:
                is_prime = False
                break

            divisor += 2

        if is_prime:
            count += 1

    return candidate