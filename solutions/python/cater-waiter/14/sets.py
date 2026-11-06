"""Functions for compiling dishes and ingredients for a catering company."""

from collections.abc import Iterable

from sets_categories_data import (
    ALCOHOLS,
    KETO,
    OMNIVORE,
    PALEO,
    SPECIAL_INGREDIENTS,
    VEGAN,
    VEGETARIAN,
)


def clean_ingredients(
    dish_name: str, dish_ingredients: Iterable[str]
) -> tuple[str, set[str]]:
    """Return the dish name and its unique ingredients."""
    return dish_name, set(dish_ingredients)


def check_drinks(
    drink_name: str, drink_ingredients: Iterable[str]
) -> str:
    """Classify a drink as a cocktail or mocktail."""
    ingredients = set(drink_ingredients)

    if ingredients.isdisjoint(ALCOHOLS):
        return f"{drink_name} Mocktail"

    return f"{drink_name} Cocktail"


def categorize_dish(
    dish_name: str, dish_ingredients: Iterable[str]
) -> str:
    """Return the category that matches the dish ingredients."""
    ingredients = set(dish_ingredients)

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
    else:
        category = ""

    return f"{dish_name}: {category}"


def tag_special_ingredients(
    dish: tuple[str, Iterable[str]]
) -> tuple[str, set[str]]:
    """Return the dish name and its special ingredients."""
    dish_name, ingredients = dish

    return dish_name, set(ingredients) & SPECIAL_INGREDIENTS


def compile_ingredients(
    dishes: Iterable[Iterable[str]]
) -> set[str]:
    """Return all unique ingredients from the dishes."""
    return {
        ingredient
        for dish in dishes
        for ingredient in dish
    }


def separate_appetizers(
    dishes: Iterable[str], appetizers: Iterable[str]
) -> list[str]:
    """Return unique dishes excluding the appetizers."""
    appetizer_names = set(appetizers)

    return [
        dish
        for dish in dict.fromkeys(dishes)
        if dish not in appetizer_names
    ]


def singleton_ingredients(
    dishes: Iterable[Iterable[str]], intersection: set[str]
) -> set[str]:
    """Return ingredients that appear in only one dish."""
    return compile_ingredients(dishes) - intersection