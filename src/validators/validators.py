from typing import Any
from attrs import Attribute


def not_blank(_instance: Any, attribute: Attribute, value: str):
    if value.strip() == "":
        raise ValueError(f'{attribute.name} must not be blank.')

