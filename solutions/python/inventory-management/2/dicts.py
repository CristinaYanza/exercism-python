"""Functions to keep track and alter inventory."""

def create_inventory(items):
    """Create a dictionary with the count of each item."""
    inventory = {}

    for item in items:
        inventory[item] = inventory.get(item, 0) + 1

    return inventory

def add_items(inventory, items):
    """Add or increment items in the inventory."""
    for item in items:
        inventory[item] = inventory.get(item, 0) + 1

    return inventory

def decrement_items(inventory, items):
    """Decrease the count of each item by one."""
    for item in items:
        if inventory.get(item, 0) > 0:
            inventory[item] -= 1

    return inventory

def remove_item(inventory, item):
    """Remove an item from the inventory."""
    inventory.pop(item, None)

    return inventory

def list_inventory(inventory):
    """Return a list of items with a count greater than zero."""
    available_items = []

    for item, count in inventory.items():
        if count > 0:
            available_items.append((item, count))

    return available_items