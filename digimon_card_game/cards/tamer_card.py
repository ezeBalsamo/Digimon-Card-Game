from attr import field
from attr import frozen
from attr.validators import in_
from attr.validators import min_len

from ..extensions.attrs.validators import all_elements_are_member_of_enum
from ..extensions.attrs.validators import not_blank
from ..extensions.attrs.validators import within_range
from .information import CardColor
from .information import CardRarity


@frozen(kw_only=True)
class TamerCard:
    name: str = field(validator=not_blank)
    colors: frozenset[CardColor] = field(
        validator=[min_len(1), all_elements_are_member_of_enum(CardColor)]
    )
    identifier: str = field(validator=not_blank)
    rarity: CardRarity = field(validator=in_(list(CardRarity)))
    cost: int = field(validator=within_range(0, 20))
