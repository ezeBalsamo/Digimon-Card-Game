from typing import Callable, Any
from pytest import raises
from ..number import assert_raises_not_positive_because


def assert_attr_raises_not_blank(attr_name: str, closure: Callable[[str], Any]):
    for invalid_value in ['', ' ']:
        with raises(ValueError) as exception_info:
            closure(invalid_value)
        assert str(exception_info.value) == f'{attr_name} must not be blank.'


def assert_attr_raises_not_within_range(attr_name: str, lower: int, upper: int, closure: Callable[[int], Any]):
    for invalid_value in [lower - 1, upper + 1]:
        with raises(ValueError) as exception_info:
            closure(invalid_value)
        assert str(exception_info.value) == f'{attr_name} must be between {lower} and {upper}.'


def assert_attr_raises_not_positive(attr_name: str, closure: Callable[[int], Any]):
    assert_raises_not_positive_because(closure, lambda invalid_value: f"'{attr_name}' must be > 0: {invalid_value}")
