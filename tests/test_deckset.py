from pytest import raises
from src.cards import shadow_wing, koromon
from src.digimon_card_game import Deck, Deckset


def test_01_cannot_create_deckset_with_optional_decks_with_equivalent_identifiers():
    main_deck = Deck(cards=[shadow_wing()])
    invalid_optional_decks = {
        'Digi-Egg': Deck(cards=[koromon]),
        'Digi-EGG': Deck(cards=[koromon])
    }
    with raises(ValueError) as exception_info:
        Deckset(main_deck=main_deck, optional_decks=invalid_optional_decks)
    assert str(exception_info.value) == 'optional_decks must not include equivalent identifiers (lowercase): digi-egg'
