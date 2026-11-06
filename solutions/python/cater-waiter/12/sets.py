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
    drink_type = "Mocktail" if ingredients.isdisjoint(ALCOHOLS) else "Cocktail"
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
        (name for group, name in categories if ingredients.issubset(group)),
        "",
    )
    return f"{dish_name}: {category}"

def tag_special_ingredients(
    dish: tuple[str, Iterable[str]]
) -> tuple[str, set[str]]:
    """Return the dish name and its special ingredients."""
    dish_name, ingredients = dish
    # Usamos el operador de intersección directamente sobre el conjunto
    return dish_name, set(ingredients) & SPECIAL_INGREDIENTS

def compile_ingredients(
    dishes: Iterable[Iterable[str]]
) -> set[str]:
    """Return all unique ingredients from the dishes."""
    # El operador de unión del tipo set (|) o set.union(*dishes) es óptimo aquí.
    # También se puede usar set().union(*dishes) como tenías, o una comprensión anidada si prefieres claridad:
    return {ingredient for dish in dishes for ingredient in dish}

def separate_appetizers(
    dishes: Iterable[str], appetizers: Iterable[str]
) -> list[str]:
    """Return unique dishes without the appetizers."""
    appetizer_names = set(appetizers)
    # dict.fromkeys() es excelente para eliminar duplicados manteniendo el orden.
    return [
        dish for dish in dict.fromkeys(dishes) 
        if dish not in appetizer_names
    ]

def singleton_ingredients(
    dishes: Iterable[Iterable[str]], intersection: set[str]
) -> set[str]:
    """Return ingredients that appear in only one dish."""
    return compile_ingredients(dishes) - intersection