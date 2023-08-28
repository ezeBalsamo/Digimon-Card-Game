from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any
    from typing import TypeVar

    T = TypeVar("T")
    from collections.abc import Callable
    from collections.abc import Iterable
    from enum import Enum

    from attrs import Attribute


def not_blank(_instance: object, attribute: Attribute[str], value: str) -> None:
    if value.strip() == "":
        raise ValueError(f"{attribute.name} must not be blank.")


def within_range(lower: int, upper: int) -> Callable[[Any, Attribute[int], int], None]:
    def wrapper(_instance: object, attribute: Attribute[int], value: int) -> None:
        if not lower <= value <= upper:
            raise ValueError(f"{attribute.name} must be between {lower} and {upper}.")

    return wrapper


def all_elements_are_member_of_enum(
    enum: type[Enum],
) -> Callable[[Any, Attribute[Any], Any], None]:
    def wrapper(
        _instance: object, attribute: Attribute[Any], value: Iterable[T]
    ) -> None:
        for element in value:
            if element not in enum:
                raise ValueError(
                    f"{attribute.name}: all elements must be a member of {enum.__name__} enum."
                )

    return wrapper
