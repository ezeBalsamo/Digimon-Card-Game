from typing import Any
from attrs import Attribute


def not_blank(_instance: Any, attribute: Attribute, value: str):
    if value.strip() == "":
        raise ValueError(f'{attribute.name} must not be blank.')


def within_range(lower: int, upper: int):
    def wrapper(_instance: Any, attribute: Attribute, value: int):
        if not lower <= value <= upper:
            raise ValueError(f'{attribute.name} must be between {lower} and {upper}.')

    return wrapper
