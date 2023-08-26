from enum import Enum
from typing import Any


def assert_expected_enum_values(
    enum_class: type[Enum], expected_enum_values: set[Any]
) -> None:
    enum_values = {enum_item.value for enum_item in list(enum_class)}
    assert enum_values == expected_enum_values
