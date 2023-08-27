from .assertions import assert_attr_raises_not_blank
from digimon_card_game.decks import Deck
from digimon_card_game.decks import Deckset
from digimon_card_game.duels import Duelist
from digimon_card_game.seeders import card_seeder


def deckset() -> Deckset:
    return Deckset(
        name="Starter Deck", main_deck=Deck(cards=[card_seeder.shadow_wing()])
    )


def test_01_cannot_create_duelist_with_blank_name() -> None:
    assert_attr_raises_not_blank(
        "name", lambda invalid_name: Duelist(name=invalid_name, deckset=deckset())
    )


def test_02_instance_creation_and_accessing() -> None:
    name = "Pepe Sand"
    the_deckset = deckset()
    duelist = Duelist(name=name, deckset=the_deckset)
    assert duelist.name == name
    assert duelist.deckset == the_deckset
