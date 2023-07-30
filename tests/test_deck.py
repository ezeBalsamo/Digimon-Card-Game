from src.digimon_card_game import Deck, DigiEggCard, CardColor, CardRarity, DigimonType, OptionCard, DigimonCard, \
    DigimonForm, DigimonAttribute
from pytest import raises


def koromon():
    return DigiEggCard(name='Koromon', color=CardColor.RED, identifier='ST1-01', rarity=CardRarity.COMMON,
                       type=DigimonType.LESSER, level=2)


def shadow_wing():
    return OptionCard(name='Shadow Wing', color=CardColor.RED, identifier='ST1-13', rarity=CardRarity.COMMON, cost=1)


def biyomon():
    return DigimonCard(name='Biyomon', color=CardColor.RED, identifier='ST1-02',
                       rarity=CardRarity.COMMON, form=DigimonForm.ROOKIE, attribute=DigimonAttribute.VACCINE,
                       type=DigimonType.BIRD, cost=2, power=3000, level=3)


def test_01_cannot_create_deck_without_cards():
    invalid_cards = []
    minimum_length = 1
    with raises(ValueError) as exception_info:
        Deck(cards=invalid_cards)
    assert str(exception_info.value) == f"Length of 'cards' must be => {minimum_length}: {len(invalid_cards)}"


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
    assert len(deck.cards) == 1
    assert deck.cards[0] == second_card


def test_04_draw_the_last_card():
    card = koromon()
    deck = Deck(cards=[card])
    drawn_card = deck.draw()
    assert drawn_card == card
    assert not deck.cards


def test_05_cannot_draw_when_there_are_no_more_cards():
    deck = Deck(cards=[koromon()])
    deck.draw()
    assert not deck.cards
    with raises(ValueError) as exception_info:
        deck.draw()
    assert str(exception_info.value) == 'There are no more cards in the deck.'


def test_06_draw_many_cards():
    first_card = koromon()
    second_card = shadow_wing()
    third_card = biyomon()
    deck = Deck(cards=[first_card, second_card, third_card])
    drawn_cards = deck.draw_many(number_of_cards=2)
    assert drawn_cards == [first_card, second_card]
    assert len(deck.cards) == 1
    assert deck.cards[0] == third_card


def test_07_draw_many_cards_and_leave_the_deck_empty():
    first_card = koromon()
    second_card = shadow_wing()
    deck = Deck(cards=[first_card, second_card])
    drawn_cards = deck.draw_many(number_of_cards=2)
    assert drawn_cards == [first_card, second_card]
    assert not deck.cards
