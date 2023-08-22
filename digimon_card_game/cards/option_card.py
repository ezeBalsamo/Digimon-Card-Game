from attr import frozen, field
from attr.validators import in_, min_len
from .information import CardColor, CardRarity
from ..extensions.attrs.validators import not_blank, within_range, all_elements_are_member_of_enum


@frozen(kw_only=True)
class OptionCard:
    name: str = field(validator=not_blank)
    colors: frozenset[CardColor] = field(validator=[min_len(1), all_elements_are_member_of_enum(CardColor)])
    identifier: str = field(validator=not_blank)
    rarity: CardRarity = field(validator=in_(list(CardRarity)))
    cost: int = field(validator=within_range(0, 20))
