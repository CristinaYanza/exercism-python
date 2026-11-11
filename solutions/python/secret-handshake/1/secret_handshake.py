"""Convert binary code into secret handshake commands."""

def commands(binary_str):
    """Return the secret handshake actions."""

    actions = ["wink", "double blink", "close your eyes", "jump"]
    result = []

    for position in range(4):
        if binary_str[-(position + 1)] == "1":
            result.append(actions[position])

    if binary_str[0] == "1":
        result.reverse()

    return result