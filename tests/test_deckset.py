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


def test_02_deckset_without_optional_decks():
    main_deck = Deck(cards=[shadow_wing()])
    deckset = Deckset(main_deck=main_deck)

    assert deckset.main_deck == main_deck
    assert not deckset.optional_decks


def test_03_deckset_with_one_optional_deck():
    main_deck = Deck(cards=[shadow_wing()])
    digi_egg_deck = Deck(cards=[koromon])
    optional_decks = {'Digi-Egg': digi_egg_deck}
    deckset = Deckset(main_deck=main_deck, optional_decks=optional_decks)

    assert deckset.optional_decks == optional_decks
    assert deckset.optional_deck_known_as('Digi-Egg') == digi_egg_deck
