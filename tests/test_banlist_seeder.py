from datetime import date

from digimon_card_game.seeders.banlist_seeder import banlist_2022_05_13, banlist_2021_04_01, banlist_2022_02_25, \
    banlist_2022_08_01, banlist_2022_11_11, banlist_2023_04_01, banlist_2023_06_01
from digimon_card_game.seeders.card_seeder import saviorhuckmon, eyesmon, argomon, hidden_potential_discovered, \
    reinforcing_memory_boost, ice_wall, jetsilphymon, tommy_himi, mega_digimon_fusion, calling_from_the_darkness, \
    sunrise_buster, dorugreymon, shoutmon_x4, greymon_x_antibody, blossomon, impmon, weregarurumon, grankuwagamon


def test_01_banlist_2022_05_13() -> None:
    banlist_date = date(2022, 5, 13)
    invalid_number_of_copies_by_card = {
        saviorhuckmon(): 1,
        eyesmon(): 1
    }

    assert banlist_2022_05_13().date == banlist_date
    assert banlist_2022_05_13().number_of_copies_by_card == invalid_number_of_copies_by_card


def test_02_banlist_2021_04_01() -> None:
    banlist_date = date(2021, 4, 1)
    invalid_number_of_copies_by_card = {
        argomon(): 1,
        hidden_potential_discovered(): 1
    }

    assert banlist_2021_04_01().date == banlist_date
    assert banlist_2021_04_01().number_of_copies_by_card == invalid_number_of_copies_by_card


def test_03_banlist_2022_02_25() -> None:
    banlist_date = date(2022, 2, 25)
    invalid_number_of_copies_by_card = {
        mega_digimon_fusion(): 0,
        reinforcing_memory_boost(): 1,
        ice_wall(): 1
    }

    assert banlist_2022_02_25().date == banlist_date
    assert banlist_2022_02_25().number_of_copies_by_card == invalid_number_of_copies_by_card


def test_04_banlist_2022_08_01() -> None:
    banlist_date = date(2022, 8, 1)
    invalid_number_of_copies_by_card = {
        jetsilphymon(): 1,
        tommy_himi(): 1
    }

    assert banlist_2022_08_01().date == banlist_date
    assert banlist_2022_08_01().number_of_copies_by_card == invalid_number_of_copies_by_card


def test_05_banlist_2022_11_11() -> None:
    banlist_date = date(2022, 11, 11)
    invalid_number_of_copies_by_card = {
        calling_from_the_darkness(): 1,
        sunrise_buster(): 1,
        dorugreymon(): 1,
        shoutmon_x4(): 1
    }

    assert banlist_2022_11_11().date == banlist_date
    assert banlist_2022_11_11().number_of_copies_by_card == invalid_number_of_copies_by_card


def test_06_banlist_2023_04_01() -> None:
    banlist_date = date(2023, 4, 1)
    invalid_number_of_copies_by_card = {
        greymon_x_antibody(): 1
    }

    assert banlist_2023_04_01().date == banlist_date
    assert banlist_2023_04_01().number_of_copies_by_card == invalid_number_of_copies_by_card


def test_07_banlist_2023_06_01() -> None:
    banlist_date = date(2023, 6, 1)
    invalid_number_of_copies_by_card = {
        blossomon(): 1,
        impmon(): 1,
        weregarurumon(): 1,
        grankuwagamon(): 1
    }

    assert banlist_2023_06_01().date == banlist_date
    assert banlist_2023_06_01().number_of_copies_by_card == invalid_number_of_copies_by_card
