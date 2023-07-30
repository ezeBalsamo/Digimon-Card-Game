from src.digimon_card_game import Deck
from src.cards import koromon, shadow_wing, biyomon
from tests.assertions.list import assert_list_raises_not_minimum_length, assert_the_only_one_in
from tests.assertions.number import assert_raises_not_positive

from pytest import raises


def assert_raises_no_more_cards(closure):
    with raises(ValueError) as exception_info:
        closure()
    assert str(exception_info.value) == 'There are no more cards.'


def test_01_cannot_create_deck_without_cards():
    assert_list_raises_not_minimum_length('cards', 1, lambda invalid_cards: Deck(cards=invalid_cards))


def test_02_instance_creation_and_accessing():
    cards = [koromon()]
    deck = Deck(cards=cards)
    assert deck.cards == cards


def test_03_draw_one_card():
    first_card = koromon()
    second_card = shadow_wing()
    deck = Deck(cards=[first_card, second_card])
    drawn_card = deck.draw()
    assert drawn_card == first_card
    assert_the_only_one_in(deck.cards, second_card)


def test_04_draw_the_last_card():
    card = koromon()
    deck = Deck(cards=[card])
    drawn_card = deck.draw()
    assert drawn_card == card
    assert deck.is_empty()


def test_05_cannot_draw_when_there_are_no_more_cards():
    deck = Deck(cards=[koromon()])
    deck.draw()
    assert deck.is_empty()
    assert_raises_no_more_cards(lambda: deck.draw())


def test_06_draw_many_cards():
    first_card = koromon()
    second_card = shadow_wing()
    third_card = biyomon()
    deck = Deck(cards=[first_card, second_card, third_card])
    drawn_cards = deck.draw_many(number_of_cards=2)
    assert drawn_cards == [first_card, second_card]
    assert_the_only_one_in(deck.cards, third_card)


def test_07_draw_many_cards_and_leave_the_deck_empty():
    first_card = koromon()
    second_card = shadow_wing()
    deck = Deck(cards=[first_card, second_card])
    drawn_cards = deck.draw_many(number_of_cards=2)
    assert drawn_cards == [first_card, second_card]
    assert deck.is_empty()


def test_08_cannot_draw_many_cards_when_there_are_no_more_cards():
    first_card = koromon()
    deck = Deck(cards=[first_card])
    deck.draw()
    assert deck.is_empty()
    assert_raises_no_more_cards(lambda: deck.draw_many(number_of_cards=2))


def test_08_cannot_draw_more_cards_than_the_number_of_remaining_cards_in_deck():
    first_card = koromon()
    deck = Deck(cards=[first_card])
    with raises(ValueError) as exception_info:
        deck.draw_many(number_of_cards=2)
    assert str(exception_info.value) == 'You cannot draw 2 cards. Number of remaining cards: 1.'


def test_09_cannot_draw_non_positive_number_of_cards():
    deck = Deck(cards=[koromon()])
    assert_raises_not_positive(lambda invalid_number_of_cards: deck.draw_many(invalid_number_of_cards),
                               'The number of cards to draw must be positive.')
