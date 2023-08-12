from attr import frozen, field
from ..extensions.attrs.validators import not_blank


@frozen(kw_only=True)
class Banlist:
    name: str = field(validator=not_blank)
