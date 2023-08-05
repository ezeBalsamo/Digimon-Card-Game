from cards import shadow_wing
from digimon_card_game import Deckset, Deck
from duels.duelist import Duelist
from tests.assertions.attributes import assert_attr_raises_not_blank


def test_01_cannot_create_duelist_with_blank_name():
    assert_attr_raises_not_blank('name',
                                 lambda invalid_name: Duelist(name=invalid_name,
                                                              deckset=Deckset(main_deck=Deck(cards=[shadow_wing()]))))


def test_02_instance_creation_and_accessing():
    duelist = Duelist(name='Pepe Sand',
                      deckset=Deckset(main_deck=Deck(cards=[shadow_wing()])))
    assert duelist.name == 'Pepe Sand'
    assert duelist.deckset == Deckset(main_deck=Deck(cards=[shadow_wing()]))
