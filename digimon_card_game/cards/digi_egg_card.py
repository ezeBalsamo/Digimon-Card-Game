from attr import field
from attr import frozen
from attr.validators import in_
from attr.validators import optional

from ..extensions.attrs.validators import not_blank
from ..extensions.attrs.validators import within_range
from .information import CardColor
from .information import CardRarity
from .information import DigimonForm
from .information import DigimonType


@frozen(kw_only=True)
class DigiEggCard:
    name: str = field(validator=not_blank)
    color: CardColor = field(validator=in_(CardColor))
    identifier: str = field(validator=not_blank)
    rarity: CardRarity = field(validator=in_(list(CardRarity)))
    type: DigimonType = field(validator=in_(DigimonType))
    level: int | None = field(
        default=None, validator=optional(within_range(lower=2, upper=7))
    )

    @property
    def form(self) -> DigimonForm:
        return DigimonForm.IN_TRAINING
