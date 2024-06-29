from collections.abc import Callable
from typing import Any
from typing import TypeVar

import pytest

T = TypeVar("T")


def assert_list_raises_not_minimum_length(
    attr_name: str, minimum_length: int, closure: Callable[[list[Any]], Any]
) -> None:
    invalid_list = list(range(minimum_length - 1))
    with pytest.raises(
        ValueError,
        match=f"Length of '{attr_name}' must be >= {minimum_length}: {len(invalid_list)}",
    ):
        closure(invalid_list)


def assert_frozenset_raises_not_minimum_length(
    attr_name: str, minimum_length: int, closure: Callable[[frozenset[Any]], Any]
) -> None:
    invalid_collection = frozenset(range(minimum_length - 1))
    with pytest.raises(
        ValueError,
        match=f"Length of '{attr_name}' must be >= {minimum_length}: {len(invalid_collection)}",
    ):
        closure(invalid_collection)


def with_the_only_one_in(collection: list[Any], closure: Callable[[Any], None]) -> None:
    assert len(collection) == 1
    closure(collection[0])


def assert_the_only_one_in(collection: list[T], expected_element: T) -> None:
    def assert_equals(element: T, another_element: T) -> None:
        assert element == another_element

    with_the_only_one_in(
        collection, lambda found_element: assert_equals(found_element, expected_element)
    )
