"""Functions for compiling dishes and ingredients for a catering company."""

from sets_categories_data import (
    VEGAN,
    VEGETARIAN,
    KETO,
    PALEO,
    OMNIVORE,
    ALCOHOLS,
    SPECIAL_INGREDIENTS,
)


def clean_ingredients(
    dish_name: str, dish_ingredients: list[str]
) -> tuple[str, set[str]]:
    """Return the dish name and its unique ingredients."""

    ingredients = set(dish_ingredients)
    return dish_name, ingredients


def check_drinks(
    drink_name: str, drink_ingredients: list[str]
) -> str:
    """Classify a drink as a cocktail or mocktail."""

    if set(drink_ingredients).isdisjoint(ALCOHOLS):
        return f"{drink_name} Mocktail"

    return f"{drink_name} Cocktail"


def categorize_dish(
    dish_name: str, dish_ingredients: list[str]
) -> str:
    """Return the category that matches the dish ingredients."""

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


def tag_special_ingredients(
    dish: tuple[str, list[str]]
) -> tuple[str, set[str]]:
    """Return the dish name and its special ingredients."""

    dish_name, dish_ingredients = dish
    special = set(dish_ingredients).intersection(SPECIAL_INGREDIENTS)

    return dish_name, special


def compile_ingredients(dishes: list[set[str]]) -> set[str]:
    """Return a set containing all unique dish ingredients."""

    ingredients = set()

    for dish in dishes:
        ingredients = ingredients.union(dish)

    return ingredients


def separate_appetizers(
    dishes: list[str], appetizers: list[str]
) -> list[str]:
    """Return unique dishes excluding the appetizers."""

    appetizer_names = set(appetizers)

    return list(dict.fromkeys(
        dish for dish in dishes if dish not in appetizer_names
    ))


def singleton_ingredients(
    dishes: list[set[str]], intersection: set[str]
) -> set[str]:
    """Return ingredients that appear in only one dish."""

    all_ingredients = compile_ingredients(dishes)

    return all_ingredients.difference(intersection)