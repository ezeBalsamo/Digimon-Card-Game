from datetime import date
from digimon_card_game.banlists import Banlist
from digimon_card_game.seeders.card_seeder import (
    saviorhuckmon,
    eyesmon,
    argomon,
    hidden_potential_discovered,
    reinforcing_memory_boost,
    ice_wall,
    mega_digimon_fusion,
    jetsilphymon,
    tommy_himi,
    calling_from_the_darkness,
    sunrise_buster,
    dorugreymon,
    shoutmon_x4,
    greymon_x_antibody,
    blossomon,
    impmon,
    weregarurumon,
    grankuwagamon,
)


def banlist_2022_05_13() -> Banlist:
    return Banlist(
        date=date(2022, 5, 13),
        number_of_copies_by_card={saviorhuckmon(): 1, eyesmon(): 1},
    )


def banlist_2021_04_01() -> Banlist:
    return Banlist(
        date=date(2021, 4, 1),
        number_of_copies_by_card={argomon(): 1, hidden_potential_discovered(): 1},
    )


def banlist_2022_02_25() -> Banlist:
    return Banlist(
        date=date(2022, 2, 25),
        number_of_copies_by_card={
            mega_digimon_fusion(): 0,
            reinforcing_memory_boost(): 1,
            ice_wall(): 1,
        },
    )


def banlist_2022_08_01() -> Banlist:
    return Banlist(
        date=date(2022, 8, 1),
        number_of_copies_by_card={jetsilphymon(): 1, tommy_himi(): 1},
    )


def banlist_2022_11_11() -> Banlist:
    return Banlist(
        date=date(2022, 11, 11),
        number_of_copies_by_card={
            calling_from_the_darkness(): 1,
            sunrise_buster(): 1,
            dorugreymon(): 1,
            shoutmon_x4(): 1,
        },
    )


def banlist_2023_04_01() -> Banlist:
    return Banlist(
        date=date(2023, 4, 1), number_of_copies_by_card={greymon_x_antibody(): 1}
    )


def banlist_2023_06_01() -> Banlist:
    return Banlist(
        date=date(2023, 6, 1),
        number_of_copies_by_card={
            blossomon(): 1,
            impmon(): 1,
            weregarurumon(): 1,
            grankuwagamon(): 1,
        },
    )
