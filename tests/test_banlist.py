from datetime import UTC
from datetime import datetime

import pytest

from digimon_card_game.banlists import Banlist
from digimon_card_game.cards import Card
from digimon_card_game.decks import Deck
from digimon_card_game.decks import Deckset
from digimon_card_game.seeders import card_seeder

from .assertions import assert_dict_raises_not_minimum_length

shadow_wing: Card = card_seeder.shadow_wing()
biyomon: Card = card_seeder.biyomon()
date = datetime.now(tz=UTC).date()


def test_01_cannot_create_banlist_without_cards() -> None:
    assert_dict_raises_not_minimum_length(
        "number_of_copies_by_card",
        1,
        lambda invalid_number_of_copies_by_card: Banlist(
            date=date, number_of_copies_by_card=invalid_number_of_copies_by_card
        ),
    )


def test_02_cannot_create_banlist_with_negative_number_of_cards() -> None:
    invalid_number_of_copies_by_card = {shadow_wing: -1}

    with pytest.raises(
        ValueError, match="number_of_copies_by_card must not include negative values."
    ):
        Banlist(date=date, number_of_copies_by_card=invalid_number_of_copies_by_card)


def test_03_instance_creation_and_accessing() -> None:
    number_of_copies_by_card = {shadow_wing: 3, biyomon: 0}
    banlist = Banlist(date=date, number_of_copies_by_card=number_of_copies_by_card)

    assert banlist.date == date
    assert banlist.number_of_copies_by_card == number_of_copies_by_card


def test_04_card_is_allowed_when_not_in_the_banlist() -> None:
    number_of_copies_by_card = {biyomon: 0}
    banlist = Banlist(date=date, number_of_copies_by_card=number_of_copies_by_card)

    assert banlist.is_card_allowed(shadow_wing, 1)


def test_05_card_is_allowed_when_is_in_the_banlist_and_number_of_copies_is_lower_than_the_allowed() -> (
    None
):
    number_of_copies_by_card = {shadow_wing: 3}
    banlist = Banlist(date=date, number_of_copies_by_card=number_of_copies_by_card)

    assert banlist.is_card_allowed(shadow_wing, 1)


def test_06_card_is_allowed_when_is_in_the_banlist_and_number_of_copies_equals_the_allowed() -> (
    None
):
    number_of_copies_by_card = {shadow_wing: 3}
    banlist = Banlist(date=date, number_of_copies_by_card=number_of_copies_by_card)

    assert banlist.is_card_allowed(shadow_wing, 3)


def test_07_card_is_not_allowed_when_is_in_the_banlist_and_number_of_copies_is_greater_than_the_allowed() -> (
    None
):
    number_of_copies_by_card = {biyomon: 0}
    banlist = Banlist(date=date, number_of_copies_by_card=number_of_copies_by_card)

    assert not banlist.is_card_allowed(biyomon, 3)


def test_08_deck_is_allowed_when_all_cards_are_allowed() -> None:
    number_of_copies_by_card = {shadow_wing: 3, biyomon: 0}
    banlist = Banlist(date=date, number_of_copies_by_card=number_of_copies_by_card)
    deck = Deck(cards=[shadow_wing])

    assert banlist.is_deck_allowed(deck)


def test_09_deck_is_not_allowed_when_at_least_one_card_is_not_allowed() -> None:
    number_of_copies_by_card = {shadow_wing: 3, biyomon: 0}
    banlist = Banlist(date=date, number_of_copies_by_card=number_of_copies_by_card)
    deck = Deck(cards=[biyomon])

    assert not banlist.is_deck_allowed(deck)


def test_10_deckset_is_not_allowed_if_main_deck_is_not_allowed() -> None:
    number_of_copies_by_card = {biyomon: 0}
    banlist = Banlist(date=date, number_of_copies_by_card=number_of_copies_by_card)
    deck = Deck(cards=[biyomon])
    deckset = Deckset(name="Deckset", main_deck=deck)

    assert not banlist.is_deckset_allowed(deckset)


def test_11_deckset_is_not_allowed_if_at_least_one_the_optional_decks_is_not_allowed() -> (
    None
):
    number_of_copies_by_card = {shadow_wing: 3, biyomon: 0}
    banlist = Banlist(date=date, number_of_copies_by_card=number_of_copies_by_card)
    main_deck = Deck(cards=[shadow_wing])
    biyomon_deck = Deck(cards=[biyomon])
    optional_decks = {"Biyomon-Deck": biyomon_deck}
    deckset = Deckset(
        name="Deckset", main_deck=main_deck, optional_decks=optional_decks
    )

    assert not banlist.is_deckset_allowed(deckset)


def test_12_deckset_is_allowed_if_all_decks_are_allowed() -> None:
    number_of_copies_by_card = {shadow_wing: 3, biyomon: 0}
    banlist = Banlist(date=date, number_of_copies_by_card=number_of_copies_by_card)
    main_deck = Deck(cards=[shadow_wing])
    digi_egg_deck = Deck(cards=[card_seeder.koromon()])
    optional_decks = {"Digi-Egg": digi_egg_deck}
    deckset = Deckset(
        name="Deckset", main_deck=main_deck, optional_decks=optional_decks
    )

    assert banlist.is_deckset_allowed(deckset)
