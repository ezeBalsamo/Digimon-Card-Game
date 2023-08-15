from attr import frozen, field
from ..cards import Card
from attrs.validators import min_len
from datetime import date


@frozen(kw_only=True)
class Banlist:
    date: date
    number_of_copies_by_card: dict[Card, int] = field(validator=min_len(1))
