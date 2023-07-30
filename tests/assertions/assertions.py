from enum import Enum
from typing import Any, Type, Set, Callable
from pytest import raises


def assert_expected_enum_values(enum_class: Type[Enum], expected_enum_values: Set[Any]):
    enum_values = set(map(lambda enum_item: enum_item.value, list(enum_class)))
    assert enum_values == expected_enum_values


def assert_raises_not_blank(attr_name: str, closure: Callable[[str], Any]):
    for invalid_value in ['', ' ']:
        with raises(ValueError) as exception_info:
            closure(invalid_value)
        assert str(exception_info.value) == f'{attr_name} must not be blank.'


def assert_raises_not_within_range(attr_name: str, lower: int, upper: int, closure: Callable[[int], Any]):
    for invalid_value in [lower - 1, upper + 1]:
        with raises(ValueError) as exception_info:
            closure(invalid_value)
        assert str(exception_info.value) == f'{attr_name} must be between {lower} and {upper}.'
