from datetime import date
from digimon_card_game.banlists import Banlist
from digimon_card_game.cards import shadow_wing, biyomon, koromon
from digimon_card_game.decks import Deckset, Deck
from .assertions import assert_dict_raises_not_minimum_length
from pytest import raises


def test_01_cannot_create_banlist_without_cards():
    assert_dict_raises_not_minimum_length('number_of_copies_by_card', 1,
                                          lambda invalid_cards: Banlist(
                                              date=date.today(),
                                              number_of_copies_by_card=invalid_cards))


def test_02_cannot_create_banlist_with_negative_number_of_cards():
    today = date.today()
    invalid_number_of_copies_by_card = {shadow_wing(): -1}

    with raises(ValueError) as exception_info:
        Banlist(date=today, number_of_copies_by_card=invalid_number_of_copies_by_card)
    assert str(exception_info.value) == 'number_of_copies_by_card must not include negative values.'


def test_03_instance_creation_and_accessing():
    today = date.today()
    number_of_copies_by_card = {
        shadow_wing(): 3,
        biyomon(): 0
    }
    banlist = Banlist(date=today, number_of_copies_by_card=number_of_copies_by_card)

    assert banlist.date == today
    assert banlist.number_of_copies_by_card == number_of_copies_by_card


def test_04_card_is_allowed_when_not_in_the_banlist():
    number_of_copies_by_card = {biyomon(): 0}
    banlist = Banlist(date=date.today(), number_of_copies_by_card=number_of_copies_by_card)

    assert banlist.is_card_allowed(shadow_wing(), 1)


def test_05_card_is_allowed_when_is_in_the_banlist_but_number_of_copies_is_lower_than_the_allowed():
    number_of_copies_by_card = {shadow_wing(): 3}
    banlist = Banlist(date=date.today(), number_of_copies_by_card=number_of_copies_by_card)

    assert banlist.is_card_allowed(shadow_wing(), 1)


def test_06_card_is_allowed_when_is_in_the_banlist_but_number_of_copies_equals_the_allowed():
    number_of_copies_by_card = {shadow_wing(): 3}
    banlist = Banlist(date=date.today(), number_of_copies_by_card=number_of_copies_by_card)

    assert banlist.is_card_allowed(shadow_wing(), 3)


def test_07_card_is_not_allowed_when_is_in_the_banlist_but_number_of_copies_is_greater_than_the_allowed():
    number_of_copies_by_card = {biyomon(): 0}
    banlist = Banlist(date=date.today(), number_of_copies_by_card=number_of_copies_by_card)

    assert not banlist.is_card_allowed(biyomon(), 3)


def test_08_deck_is_allowed_when_all_cards_are_allowed():
    number_of_copies_by_card = {
        shadow_wing(): 3,
        biyomon(): 0
    }
    banlist = Banlist(date=date.today(), number_of_copies_by_card=number_of_copies_by_card)
    deck = Deck(cards=[shadow_wing()])

    assert banlist.is_deck_allowed(deck) is True


def test_09_deck_is_not_allowed_when_at_least_one_card_is_not_allowed():
    number_of_copies_by_card = {
        shadow_wing(): 3,
        biyomon(): 0
    }
    banlist = Banlist(date=date.today(), number_of_copies_by_card=number_of_copies_by_card)
    deck = Deck(cards=[biyomon()])

    assert not banlist.is_deck_allowed(deck)


def test_10_deckset_is_not_allowed_if_main_deck_is_not_allowed():
    number_of_copies_by_card = {biyomon(): 0}
    banlist = Banlist(date=date.today(), number_of_copies_by_card=number_of_copies_by_card)
    deck = Deck(cards=[biyomon()])
    deckset = Deckset(name="Deckset", main_deck=deck)

    assert not banlist.is_deckset_allowed(deckset)


def test_11_deckset_is_not_allowed_if_at_least_one_the_optional_decks_is_not_allowed():
    number_of_copies_by_card = {
        shadow_wing(): 3,
        biyomon(): 0
    }
    banlist = Banlist(date=date.today(), number_of_copies_by_card=number_of_copies_by_card)
    main_deck = Deck(cards=[shadow_wing()])
    biyomon_deck = Deck(cards=[biyomon()])
    optional_decks = {'Biyomon-Deck': biyomon_deck}
    deckset = Deckset(name="Deckset", main_deck=main_deck, optional_decks=optional_decks)

    assert not banlist.is_deckset_allowed(deckset)


def test_12_deckset_is_allowed_if_all_decks_are_allowed():
    number_of_copies_by_card = {
        shadow_wing(): 3,
        biyomon(): 0
    }
    banlist = Banlist(date=date.today(), number_of_copies_by_card=number_of_copies_by_card)
    main_deck = Deck(cards=[shadow_wing()])
    digi_egg_deck = Deck(cards=[koromon()])
    optional_decks = {'Digi-Egg': digi_egg_deck}
    deckset = Deckset(name="Deckset", main_deck=main_deck, optional_decks=optional_decks)

    assert banlist.is_deckset_allowed(deckset)
