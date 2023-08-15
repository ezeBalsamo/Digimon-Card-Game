from attr import frozen, field
from ..cards import Card
from ..extensions.attrs.validators import not_blank
from attrs.validators import min_len
"""
El nombre quedaría en caso de mantener la idea de varias banlist, en caso de tener una sola como aparentemente
tiene el juego el nombre podría removerse
"""


@frozen(kw_only=True)
class Banlist:
    name: str = field(validator=not_blank)
    number_of_copies_by_card: dict[Card, int] = field(validator=min_len(1))
"""
class BanlistV2:
    date: Date
    number_of_copies_by_card: dict[Card, int]


banlist = Banlist(date=Date.today(), 
                  restricted_cards=[
                      RestrictedCard(card=Card(), number_of_copies=2),
                      RestrictedCard(card=Card(), number_of_copies=1)
                  ])

banlist = BanlistV2(date=Date.today(),
                    number_of_copies_by_card={
                      Card(): 2,
                      Card(): 1
                    })
"""
