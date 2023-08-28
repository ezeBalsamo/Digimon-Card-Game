from digimon_card_game.cards import DigiEggCard
from digimon_card_game.cards.information import CardColor
from digimon_card_game.cards.information import CardRarity
from digimon_card_game.cards.information import DigimonForm
from digimon_card_game.cards.information import DigimonType

from .assertions import assert_attr_raises_not_blank
from .assertions import assert_attr_raises_not_within_range


def test_01_name_must_not_be_blank() -> None:
    assert_attr_raises_not_blank(
        "name",
        lambda invalid_name: DigiEggCard(
            name=invalid_name,
            color=CardColor.RED,
            identifier="ST1-01",
            rarity=CardRarity.UNCOMMON,
            type=DigimonType.LESSER,
            level=2,
        ),
    )


def test_02_identifier_must_not_be_blank() -> None:
    assert_attr_raises_not_blank(
        "identifier",
        lambda invalid_identifier: DigiEggCard(
            name="Koromon",
            color=CardColor.RED,
            identifier=invalid_identifier,
            rarity=CardRarity.UNCOMMON,
            type=DigimonType.LESSER,
            level=2,
        ),
    )


def test_03_level_must_be_between_two_and_seven() -> None:
    assert_attr_raises_not_within_range(
        "level",
        2,
        7,
        lambda invalid_level: DigiEggCard(
            name="Koromon",
            color=CardColor.RED,
            identifier="ST1-01",
            rarity=CardRarity.UNCOMMON,
            type=DigimonType.LESSER,
            level=invalid_level,
        ),
    )


def test_04_instance_creation_and_accessing() -> None:
    card = DigiEggCard(
        name="Koromon",
        color=CardColor.RED,
        identifier="ST1-01",
        rarity=CardRarity.UNCOMMON,
        type=DigimonType.LESSER,
        level=2,
    )
    assert card.name == "Koromon"
    assert card.color == CardColor.RED
    assert card.identifier == "ST1-01"
    assert card.rarity == CardRarity.UNCOMMON
    assert card.form == DigimonForm.IN_TRAINING
    assert card.type == DigimonType.LESSER
    assert card.level == 2


def test_05_instance_creation_without_level() -> None:
    card_without_level = DigiEggCard(
        name="Koromon",
        color=CardColor.RED,
        identifier="ST1-01",
        rarity=CardRarity.UNCOMMON,
        type=DigimonType.LESSER,
    )
    assert card_without_level.level is None
