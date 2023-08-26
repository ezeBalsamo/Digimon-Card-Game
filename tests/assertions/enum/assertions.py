from enum import Enum
from typing import Type, Set, Any


def assert_expected_enum_values(
    enum_class: Type[Enum], expected_enum_values: Set[Any]
) -> None:
    enum_values = set(map(lambda enum_item: enum_item.value, list(enum_class)))
    assert enum_values == expected_enum_values
