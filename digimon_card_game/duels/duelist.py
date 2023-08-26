from attr import field
from attr import frozen

from ..decks import Deckset
from ..extensions.attrs.validators import not_blank


@frozen(kw_only=True)
class Duelist:
    name: str = field(validator=not_blank)
    deckset: Deckset
