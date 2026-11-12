"""Flatten a nested list."""

def flatten(iterable):
    """Return a flattened list without None values."""

    result = []

    for item in iterable:
        if isinstance(item, list):
            result.extend(flatten(item))

        elif item is not None:
            result.append(item)

    return result