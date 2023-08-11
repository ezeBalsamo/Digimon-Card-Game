from typing import Callable, Any
from pytest import raises


def assert_list_raises_not_minimum_length(attr_name: str, minimum_length: int, closure: Callable[[list], Any]):
    invalid_list = list(range(minimum_length - 1))
    with raises(ValueError) as exception_info:
        closure(invalid_list)
    assert str(exception_info.value) == f"Length of '{attr_name}' must be => {minimum_length}: {len(invalid_list)}"


def with_the_only_one_in(collection, closure):
    assert len(collection) == 1
    closure(collection[0])


def assert_the_only_one_in(collection, expected_element):
    def assert_equals(element, another_element):
        assert element == another_element

    with_the_only_one_in(collection, lambda found_element: assert_equals(found_element, expected_element))
