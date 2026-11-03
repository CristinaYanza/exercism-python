"""Functions for compiling dishes and ingredients for a catering company."""


from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    """Remove duplicates from `dish_ingredients`."""
    
    ingredients = set(dish_ingredients)
    return (dish_name, ingredients)


def check_drinks(drink_name, drink_ingredients):
    """Append "Cocktail" (alcohol)  or "Mocktail" (no alcohol) to `drink_name`, based on `drink_ingredients`."""

    if set(drink_ingredients).isdisjoint(ALCOHOLS):
        return drink_name + " Mocktail"
    else: 
        return drink_name + " Cocktail"


def categorize_dish(dish_name, dish_ingredients):
    """Categorize `dish_name` based on `dish_ingredients`."""

    ingredients = set(dish_ingredients)
    category = ""

    if ingredients.issubset(VEGAN):
        category = "VEGAN"
    elif ingredients.issubset(VEGETARIAN):
        category = "VEGETARIAN"
    elif ingredients.issubset(PALEO):
        category = "PALEO"
    elif ingredients.issubset(KETO):
        category = "KETO"
    elif ingredients.issubset(OMNIVORE):
        category = "OMNIVORE"

    return f"{dish_name}: {category}"


def tag_special_ingredients(dish):
    """Compare `dish` ingredients to `SPECIAL_INGREDIENTS`."""

    dish_name, dish_ingredients = dish 
    special = set(dish_ingredients).intersection(SPECIAL_INGREDIENTS)
    return (dish_name, special)


def compile_ingredients(dishes):
    """Create a master list of ingredients."""

    ingredients = set()

    for dish in dishes:
        ingredients = ingredients.union(dish)
    
    return ingredients


def separate_appetizers(dishes, appetizers):
    """Determine which `dishes` are designated `appetizers` and remove them."""

    appetizer_names = set(appetizers)
    separated_dishes = []

    for dish in dishes:
        if dish not in appetizer_names and dish not in separated_dishes:
            separated_dishes.append(dish)

    return separated_dishes


def singleton_ingredients(dishes, intersection):
    """Find singleton ingredients within the group of dishes (ingredients that only appear once across dishes)."""

    all_ingredients = compile_ingredients(dishes)
    return all_ingredients.difference(intersection)
