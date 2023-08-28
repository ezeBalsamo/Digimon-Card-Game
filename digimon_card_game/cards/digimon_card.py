from attr import field
from attr import frozen
from attr.validators import gt
from attr.validators import in_
from attr.validators import min_len
from attr.validators import optional

from ..extensions.attrs.validators import all_elements_are_member_of_enum
from ..extensions.attrs.validators import not_blank
from ..extensions.attrs.validators import within_range
from .information import CardColor
from .information import CardRarity
from .information import DigimonAttribute
from .information import DigimonForm
from .information import DigimonType


@frozen(kw_only=True)
class DigimonCard:
    name: str = field(validator=not_blank)
    colors: frozenset[CardColor] = field(
        validator=[min_len(1), all_elements_are_member_of_enum(CardColor)]
    )
    identifier: str = field(validator=not_blank)
    rarity: CardRarity = field(validator=in_(list(CardRarity)))
    form: DigimonForm = field(validator=in_(DigimonForm))
    attribute: DigimonAttribute = field(validator=in_(DigimonAttribute))
    types: frozenset[DigimonType] = field(
        validator=[min_len(1), all_elements_are_member_of_enum(DigimonType)]
    )
    cost: int = field(validator=within_range(0, 20))
    power: int = field(validator=gt(0))
    level: int | None = field(
        default=None, validator=optional(within_range(lower=2, upper=7))
    )
