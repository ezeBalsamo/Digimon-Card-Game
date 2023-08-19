from __future__ import annotations
from typing import Any, Callable
from attrs import Attribute


def not_blank(_instance: Any, attribute: Attribute[str], value: str) -> None:
    if value.strip() == "":
        raise ValueError(f'{attribute.name} must not be blank.')


def within_range(lower: int, upper: int) -> Callable[[Any, Attribute[int], int], None]:
    def wrapper(_instance: Any, attribute: Attribute[int], value: int) -> None:
        if not lower <= value <= upper:
            raise ValueError(f'{attribute.name} must be between {lower} and {upper}.')

    return wrapper
