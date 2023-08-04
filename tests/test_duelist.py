from cards import shadow_wing
from digimon_card_game import Deckset, Deck
from duels.duelist import Duelist
from tests.assertions.attributes import assert_attr_raises_not_blank


def test_01_cannot_create_duelist_with_blank_name():
    assert_attr_raises_not_blank('name',
                                 lambda invalid_name: Duelist(name=invalid_name,
                                                              deckSet=Deckset(main_deck=Deck(cards=[shadow_wing()]))))
