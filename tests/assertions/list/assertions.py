from typing import Any
from typing import Callable

from pytest import raises


def assert_list_raises_not_minimum_length(
    attr_name: str, minimum_length: int, closure: Callable[[list[Any]], Any]
) -> None:
    invalid_list = list(range(minimum_length - 1))
    with raises(ValueError) as exception_info:
        closure(invalid_list)
    assert (
        str(exception_info.value)
        == f"Length of '{attr_name}' must be => {minimum_length}: {len(invalid_list)}"
    )


def assert_frozenset_raises_not_minimum_length(
    attr_name: str, minimum_length: int, closure: Callable[[frozenset[Any]], Any]
) -> None:
    invalid_collection = frozenset(range(minimum_length - 1))
    with raises(ValueError) as exception_info:
        closure(invalid_collection)
    assert (
        str(exception_info.value)
        == f"Length of '{attr_name}' must be => {minimum_length}: {len(invalid_collection)}"
    )


def with_the_only_one_in(collection: list[Any], closure: Callable[[Any], None]) -> None:
    assert len(collection) == 1
    closure(collection[0])


def assert_the_only_one_in(collection: list[Any], expected_element: Any) -> None:
    def assert_equals(element: Any, another_element: Any) -> None:
        assert element == another_element

    with_the_only_one_in(
        collection, lambda found_element: assert_equals(found_element, expected_element)
    )
