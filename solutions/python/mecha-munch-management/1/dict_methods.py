"""Functions to manage a user's shopping cart items."""

def add_item(current_cart, items_to_add):
    """Add items to the shopping cart."""
    for item in items_to_add:
        current_cart[item] = current_cart.get(item, 0) + 1

    return current_cart

def read_notes(notes):
    """Create a shopping cart from an iterable of items."""
    cart = {}

    for item in notes:
        cart[item] = cart.get(item, 0) + 1

    return cart

def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary."""
    for recipe, ingredients in recipe_updates:
        ideas[recipe] = ingredients

    return ideas

def sort_entries(cart):
    """Sort the shopping cart alphabetically."""
    sorted_cart = dict(sorted(cart.items()))

    return sorted_cart

def send_to_store(cart, aisle_mapping):
    """Combine cart items with aisle and refrigeration information."""
    fulfillment_cart = {}

    for item in sorted(cart.keys(), reverse=True):
        fulfillment_cart[item] = [
            cart[item],
            aisle_mapping[item][0],
            aisle_mapping[item][1]
        ]

    return fulfillment_cart

def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order."""
    for item, details in fulfillment_cart.items():
        new_quantity = store_inventory[item][0] - details[0]

        if new_quantity == 0:
            store_inventory[item][0] = "Out of Stock"
        else:
            store_inventory[item][0] = new_quantity

    return store_inventory