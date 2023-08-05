from pytest import raises
from src.cards import shadow_wing, koromon
from src.digimon_card_game import Deck, Deckset
from tests.assertions.attributes import assert_attr_raises_not_blank


def test_01_cannot_create_deckset_with_optional_decks_with_equivalent_identifiers():
    main_deck = Deck(cards=[shadow_wing()])
    invalid_optional_decks = {
        'Digi-Egg': Deck(cards=[koromon]),
        'Digi-EGG': Deck(cards=[koromon])
    }
    with raises(ValueError) as exception_info:
        Deckset(name='Starter Deck', main_deck=main_deck, optional_decks=invalid_optional_decks)
    assert str(exception_info.value) == 'optional_decks must not include equivalent identifiers (lowercase): digi-egg'


def test_02_name_must_not_be_blank():
    assert_attr_raises_not_blank('name',
                                 lambda invalid_name: Deckset(name=invalid_name,
                                                              main_deck=Deck(cards=[shadow_wing()])))


def test_03_deckset_without_optional_decks():
    main_deck = Deck(cards=[shadow_wing()])
    deckset = Deckset(name='Starter Deck', main_deck=main_deck)

    assert deckset.name == 'Starter Deck'
    assert deckset.main_deck == main_deck
    assert not deckset.optional_decks


def test_04_deckset_with_one_optional_deck():
    digi_egg_deck = Deck(cards=[koromon])
    optional_decks = {'Digi-Egg': digi_egg_deck}
    deckset = Deckset(name='Starter Deck', main_deck=Deck(cards=[shadow_wing()]), optional_decks=optional_decks)

    assert deckset.name == 'Starter Deck'
    assert deckset.optional_decks == optional_decks
    assert deckset.optional_deck_known_as('Digi-Egg') == digi_egg_deck


def test_05_should_fail_when_trying_to_get_optional_deck_with_invalid_identifier():
    digi_egg_deck = Deck(cards=[koromon])
    optional_decks = {'Digi-Egg': digi_egg_deck}
    deckset = Deckset(name='Starter Deck', main_deck=Deck(cards=[shadow_wing()]), optional_decks=optional_decks)
    with raises(ValueError) as exception_info:
        deckset.optional_deck_known_as('side')
    assert str(exception_info.value) == 'There is no optional deck identified by side.'
