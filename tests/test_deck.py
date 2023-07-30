from src.digimon_card_game import Deck, DigiEggCard, CardColor, CardRarity, DigimonType
from pytest import raises


def test_01_cannot_create_deck_without_cards():
    invalid_cards = []
    minimum_length = 1
    with raises(ValueError) as exception_info:
        Deck(cards=invalid_cards)
    assert str(exception_info.value) == f"Length of 'cards' must be => {minimum_length}: {len(invalid_cards)}"


def test_02_instance_creation_and_accessing():
    card = DigiEggCard(name='Koromon', color=CardColor.RED, identifier='ST1-01', rarity=CardRarity.COMMON,
                       type=DigimonType.LESSER, level=2)
    cards = [card]
    deck = Deck(cards=cards)
    assert deck.cards == cards
