from digimon_card_game.decks import Deck
from digimon_card_game.cards import Card
from digimon_card_game.seeders import card_seeder
from .assertions import assert_list_raises_not_minimum_length, assert_the_only_one_in, assert_raises_not_positive
from pytest import raises

shadow_wing = card_seeder.shadow_wing()
koromon = card_seeder.koromon()


def assert_raises_no_more_cards(closure: Callable[[], Any]) -> None:
    with raises(ValueError) as exception_info:
        closure()
    assert str(exception_info.value) == 'There are no more cards.'


def test_01_cannot_create_deck_without_cards():
    assert_list_raises_not_minimum_length('cards', 1, lambda invalid_cards: Deck(cards=invalid_cards))


def test_02_instance_creation_and_accessing() -> None:
    cards: list[Card] = [koromon]
    deck = Deck(cards=cards)
    assert deck.cards == cards


def test_03_draw_one_card() -> None:
    deck = Deck(cards=[koromon, shadow_wing])
    drawn_card = deck.draw()
    assert drawn_card == koromon
    assert_the_only_one_in(deck.cards, shadow_wing)


def test_04_draw_the_last_card() -> None:
    deck = Deck(cards=[koromon])
    drawn_card = deck.draw()
    assert drawn_card == koromon
    assert deck.is_empty()


def test_05_cannot_draw_when_there_are_no_more_cards() -> None:
    deck = Deck(cards=[koromon])
    deck.draw()
    assert deck.is_empty()
    assert_raises_no_more_cards(lambda: deck.draw())


def test_06_draw_many_cards() -> None:
    biyomon = card_seeder.biyomon()
    deck = Deck(cards=[koromon, shadow_wing, biyomon])
    drawn_cards = deck.draw_many(number_of_cards=2)
    assert drawn_cards == [koromon, shadow_wing]
    assert_the_only_one_in(deck.cards, biyomon)


def test_07_draw_many_cards_and_leave_the_deck_empty() -> None:
    deck = Deck(cards=[koromon, shadow_wing])
    drawn_cards = deck.draw_many(number_of_cards=2)
    assert drawn_cards == [koromon, shadow_wing]
    assert deck.is_empty()


def test_08_cannot_draw_many_cards_when_there_are_no_more_cards() -> None:
    deck = Deck(cards=[koromon])
    deck.draw()
    assert deck.is_empty()
    assert_raises_no_more_cards(lambda: deck.draw_many(number_of_cards=2))


def test_08_cannot_draw_more_cards_than_the_number_of_remaining_cards_in_deck() -> None:
    deck = Deck(cards=[koromon])
    with raises(ValueError) as exception_info:
        deck.draw_many(number_of_cards=2)
    assert str(exception_info.value) == 'You cannot draw 2 cards. Number of remaining cards: 1.'


def test_09_cannot_draw_non_positive_number_of_cards() -> None:
    deck = Deck(cards=[koromon])
    assert_raises_not_positive(lambda invalid_number_of_cards: deck.draw_many(invalid_number_of_cards),
                               'The number of cards to draw must be positive.')
