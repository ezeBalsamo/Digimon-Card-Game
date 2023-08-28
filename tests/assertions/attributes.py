from collections.abc import Callable
from typing import Any

import pytest

from .number import assert_raises_not_positive_because


def assert_attr_raises_not_blank(attr_name: str, closure: Callable[[str], Any]) -> None:
    for invalid_value in ["", " "]:
        with pytest.raises(ValueError, match=f"{attr_name} must not be blank."):
            closure(invalid_value)


def assert_attr_raises_not_within_range(
    attr_name: str, lower: int, upper: int, closure: Callable[[int], Any]
) -> None:
    for invalid_value in [lower - 1, upper + 1]:
        with pytest.raises(
            ValueError, match=f"{attr_name} must be between {lower} and {upper}."
        ):
            closure(invalid_value)


def assert_attr_raises_not_positive(
    attr_name: str, closure: Callable[[int], Any]
) -> None:
    assert_raises_not_positive_because(
        closure, lambda invalid_value: f"'{attr_name}' must be > 0: {invalid_value}"
    )
