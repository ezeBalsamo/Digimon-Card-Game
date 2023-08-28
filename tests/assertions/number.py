from collections.abc import Callable
from typing import Any

import pytest


def assert_raises_not_positive(closure: Callable[[int], Any], explanation: str) -> None:
    assert_raises_not_positive_because(closure, lambda _: explanation)


def assert_raises_not_positive_because(
    closure: Callable[[int], Any], explanation_closure: Callable[[int], str]
) -> None:
    for invalid_value in [-1, 0]:
        with pytest.raises(ValueError, match=explanation_closure(invalid_value)):
            closure(invalid_value)
