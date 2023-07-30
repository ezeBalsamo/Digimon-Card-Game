from typing import Any, Callable
from pytest import raises


def assert_raises_not_positive(closure: Callable[[int], Any], explanation: str):
    assert_raises_not_positive_because(closure, lambda _: explanation)


def assert_raises_not_positive_because(closure: Callable[[int], Any], explanation_closure: Callable[[int], str]):
    for invalid_value in [-1, 0]:
        with raises(ValueError) as exception_info:
            closure(invalid_value)
        assert str(exception_info.value) == explanation_closure(invalid_value)
