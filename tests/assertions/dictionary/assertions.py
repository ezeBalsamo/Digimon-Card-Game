from typing import Any
from typing import Callable

from pytest import raises


def assert_dict_raises_not_minimum_length(attr_name: str, minimum_length: int,
                                          closure: Callable[[dict[Any, Any]], Any]) -> None:
    invalid_dict = {f'key_{i}': f'value_{i}' for i in range(minimum_length - 1)}
    with raises(ValueError) as exception_info:
        closure(invalid_dict)
    assert str(exception_info.value) == f"Length of '{attr_name}' must be => {minimum_length}: {len(invalid_dict)}"
