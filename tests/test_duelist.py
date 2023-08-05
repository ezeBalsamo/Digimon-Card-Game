from cards import shadow_wing
from digimon_card_game import Deckset, Deck
from duels import Duelist
from tests.assertions.attributes import assert_attr_raises_not_blank


def deckset():
    return Deckset(name='Starter Deck', main_deck=Deck(cards=[shadow_wing()]))


def test_01_cannot_create_duelist_with_blank_name():
    assert_attr_raises_not_blank('name',
                                 lambda invalid_name: Duelist(name=invalid_name, deckset=deckset()))


def test_02_instance_creation_and_accessing():
    name = 'Pepe Sand'
    the_deckset = deckset()
    duelist = Duelist(name=name, deckset=the_deckset)
    assert duelist.name == name
    assert duelist.deckset == the_deckset
