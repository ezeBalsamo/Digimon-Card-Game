from ..cards import DigiEggCard, OptionCard, DigimonCard, TamerCard
from ..cards.information import (
    CardColor,
    CardRarity,
    DigimonType,
    DigimonForm,
    DigimonAttribute,
)


def koromon() -> DigiEggCard:
    return DigiEggCard(
        name="Koromon",
        color=CardColor.RED,
        identifier="ST1-01",
        rarity=CardRarity.UNCOMMON,
        type=DigimonType.LESSER,
        level=2,
    )


def shadow_wing() -> OptionCard:
    return OptionCard(
        name="Shadow Wing",
        colors=frozenset([CardColor.RED]),
        identifier="ST1-13",
        rarity=CardRarity.COMMON,
        cost=1,
    )


def biyomon() -> DigimonCard:
    return DigimonCard(
        name="Biyomon",
        colors=frozenset([CardColor.RED]),
        identifier="ST1-02",
        rarity=CardRarity.COMMON,
        form=DigimonForm.ROOKIE,
        attribute=DigimonAttribute.VACCINE,
        types=frozenset([DigimonType.BIRD]),
        cost=2,
        power=3000,
        level=3,
    )


def blossomon() -> DigimonCard:
    return DigimonCard(
        name="Blossomon",
        colors=frozenset([CardColor.GREEN]),
        identifier="BT3-054",
        rarity=CardRarity.COMMON,
        form=DigimonForm.ULTIMATE,
        attribute=DigimonAttribute.DATA,
        types=frozenset([DigimonType.VEGETATION]),
        cost=7,
        power=7000,
        level=5,
    )


def impmon() -> DigimonCard:
    return DigimonCard(
        name="Impmon",
        colors=frozenset([CardColor.PURPLE]),
        identifier="EX2-039",
        rarity=CardRarity.RARE,
        form=DigimonForm.ROOKIE,
        attribute=DigimonAttribute.VIRUS,
        types=frozenset([DigimonType.EVIL]),
        cost=3,
        power=1000,
        level=3,
    )


def weregarurumon() -> DigimonCard:
    return DigimonCard(
        name="WereGarurumon",
        colors=frozenset([CardColor.BLUE]),
        identifier="P-008",
        rarity=CardRarity.PROMO,
        form=DigimonForm.ULTIMATE,
        attribute=DigimonAttribute.VACCINE,
        types=frozenset([DigimonType.BEASTKIN]),
        cost=7,
        power=6000,
        level=5,
    )


def grankuwagamon() -> DigimonCard:
    return DigimonCard(
        name="GranKuwagamon",
        colors=frozenset([CardColor.GREEN]),
        identifier="P-025",
        rarity=CardRarity.PROMO,
        form=DigimonForm.MEGA,
        attribute=DigimonAttribute.FREE,
        types=frozenset([DigimonType.INSECTOID]),
        cost=11,
        power=11000,
        level=6,
    )


def greymon_x_antibody() -> DigimonCard:
    return DigimonCard(
        name="Greymon (X Antibody)",
        colors=frozenset([CardColor.BLACK, CardColor.RED]),
        identifier="BT11-064",
        rarity=CardRarity.COMMON,
        form=DigimonForm.CHAMPION,
        attribute=DigimonAttribute.VIRUS,
        types=frozenset([DigimonType.DINOSAUR, DigimonType.X_ANTIBODY]),
        cost=5,
        power=6000,
        level=4,
    )


def calling_from_the_darkness() -> OptionCard:
    return OptionCard(
        name="Calling From The Darkness",
        colors=frozenset([CardColor.PURPLE]),
        identifier="BT7-107",
        rarity=CardRarity.UNCOMMON,
        cost=1,
    )


def sunrise_buster() -> OptionCard:
    return OptionCard(
        name="Sunrise Buster",
        colors=frozenset([CardColor.YELLOW, CardColor.RED]),
        identifier="BT9-099",
        rarity=CardRarity.RARE,
        cost=5,
    )


def dorugreymon() -> DigimonCard:
    return DigimonCard(
        name="DoruGreymon",
        colors=frozenset([CardColor.BLACK]),
        identifier="BT7-064",
        rarity=CardRarity.UNCOMMON,
        form=DigimonForm.ULTIMATE,
        attribute=DigimonAttribute.DATA,
        types=frozenset([DigimonType.DRAGON, DigimonType.X_ANTIBODY]),
        cost=8,
        power=7000,
        level=5,
    )


def shoutmon_x4() -> DigimonCard:
    return DigimonCard(
        name="Shoutmon X4",
        colors=frozenset([CardColor.RED, CardColor.YELLOW]),
        identifier="BT10-009",
        rarity=CardRarity.RARE,
        form=DigimonForm.CHAMPION,
        attribute=DigimonAttribute.DATA,
        types=frozenset([DigimonType.COMPOSITE, DigimonType.XROS_HEART]),
        cost=9,
        power=8000,
        level=4,
    )


def jetsilphymon() -> DigimonCard:
    return DigimonCard(
        name="JetSilphymon",
        colors=frozenset([CardColor.YELLOW]),
        identifier="BT7-038",
        rarity=CardRarity.UNCOMMON,
        form=DigimonForm.HYBRID,
        attribute=DigimonAttribute.VARIABLE,
        types=frozenset([DigimonType.CYBORG]),
        cost=7,
        power=7000,
        level=5,
    )


def tommy_himi() -> TamerCard:
    return TamerCard(
        name="Tommy Himi",
        colors=frozenset([CardColor.BLUE]),
        identifier="BT7-086",
        rarity=CardRarity.RARE,
        cost=3,
    )


def mega_digimon_fusion() -> OptionCard:
    return OptionCard(
        name="Mega Digimon Fusion!",
        colors=frozenset([CardColor.WHITE]),
        identifier="BT5-109",
        rarity=CardRarity.RARE,
        cost=0,
    )


def reinforcing_memory_boost() -> OptionCard:
    return OptionCard(
        name="Reinforcing Memory Boost!",
        colors=frozenset([CardColor.YELLOW]),
        identifier="BT6-100",
        rarity=CardRarity.COMMON,
        cost=6,
    )


def ice_wall() -> OptionCard:
    return OptionCard(
        name="Ice Wall!",
        colors=frozenset([CardColor.BLUE]),
        identifier="EX1-068",
        rarity=CardRarity.RARE,
        cost=1,
    )


def argomon() -> DigimonCard:
    return DigimonCard(
        name="Argomon",
        colors=frozenset([CardColor.GREEN]),
        identifier="BT2-047",
        rarity=CardRarity.COMMON,
        form=DigimonForm.ULTIMATE,
        attribute=DigimonAttribute.VIRUS,
        types=frozenset([DigimonType.MUTANT]),
        cost=8,
        power=6000,
        level=5,
    )


def hidden_potential_discovered() -> OptionCard:
    return OptionCard(
        name="Hidden Potential Discovered!",
        colors=frozenset([CardColor.GREEN]),
        identifier="BT3-103",
        rarity=CardRarity.UNCOMMON,
        cost=0,
    )


def saviorhuckmon() -> DigimonCard:
    return DigimonCard(
        name="SaviorHuckmon",
        colors=frozenset([CardColor.RED]),
        identifier="BT6-015",
        rarity=CardRarity.UNCOMMON,
        form=DigimonForm.ULTIMATE,
        attribute=DigimonAttribute.DATA,
        types=frozenset([DigimonType.DRAGONKIN]),
        cost=7,
        power=7000,
        level=5,
    )


def eyesmon() -> DigimonCard:
    return DigimonCard(
        name="Eyesmon",
        colors=frozenset([CardColor.PURPLE]),
        identifier="BT7-072",
        rarity=CardRarity.COMMON,
        form=DigimonForm.CHAMPION,
        attribute=DigimonAttribute.VIRUS,
        types=frozenset([DigimonType.DARK_DRAGON]),
        cost=6,
        power=5000,
        level=4,
    )
