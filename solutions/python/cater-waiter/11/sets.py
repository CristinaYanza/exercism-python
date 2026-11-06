"""Functions for compiling dishes and ingredients for a catering company."""

from collections.abc import Iterable

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
    dish_name: str, dish_ingredients: Iterable[str]
) -> tuple[str, set[str]]:
    """Return the dish name and its unique ingredients."""
    return dish_name, set(dish_ingredients)

def check_drinks(
    drink_name: str, drink_ingredients: Iterable[str]
) -> str:
    """Return the drink name and its cocktail classification."""
    ingredients = set(drink_ingredients)

    drink_type = (
        "Mocktail" if ingredients.isdisjoint(ALCOHOLS) else "Cocktail"
    )

    return f"{drink_name} {drink_type}"

def categorize_dish(
    dish_name: str, dish_ingredients: Iterable[str]
) -> str:
    """Return the category that matches the dish ingredients."""
    ingredients = set(dish_ingredients)

    categories = (
        (VEGAN, "VEGAN"),
        (VEGETARIAN, "VEGETARIAN"),
        (PALEO, "PALEO"),
        (KETO, "KETO"),
        (OMNIVORE, "OMNIVORE"),
    )

    category = next(
        (
            name
            for group, name in categories
            if ingredients.issubset(group)
        ),
        "",
    )

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
    return set().union(*dishes)

def separate_appetizers(
    dishes: Iterable[str], appetizers: Iterable[str]
) -> list[str]:
    """Return unique dishes without the appetizers."""
    appetizer_names = set(appetizers)

    return list(dict.fromkeys(
        dish for dish in dishes if dish not in appetizer_names
    ))

def singleton_ingredients(
    dishes: Iterable[Iterable[str]], intersection: set[str]
) -> set[str]:
    """Return ingredients that appear in only one dish."""
    return compile_ingredients(dishes) - intersection