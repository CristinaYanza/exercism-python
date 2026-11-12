"""Implement basic list operations."""

def append(list1, list2):
    """Return a new list with the elements of list2 added to list1."""
    result = list1[:]

    for element in list2:
        result += [element]

    return result

def concat(lists):
    """Combine all lists into a single list."""
    result = []

    for current_list in lists:
        result = append(result, current_list)

    return result

def filter(function, list):
    """Return elements that satisfy the given function."""
    result = []

    for element in list:
        if function(element):
            result += [element]

    return result

def length(list):
    """Return the number of elements in a list."""
    count = 0

    for element in list:
        count += 1

    return count

def map(function, list):
    """Apply a function to every element and return a new list."""
    result = []

    for element in list:
        result += [function(element)]

    return result

def foldl(function, list, initial):
    """Reduce the list from left to right."""
    accumulator = initial

    for element in list:
        accumulator = function(accumulator, element)

    return accumulator

def foldr(function, list, initial):
    """Reduce the list from right to left."""
    accumulator = initial

    for element in reverse(list):
        accumulator = function(accumulator, element)

    return accumulator

def reverse(list):
    """Return a new list with the elements in reverse order."""
    result = []

    for element in list:
        result = [element] + result

    return result