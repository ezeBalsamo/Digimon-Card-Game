from datetime import date as Date

from digimon_card_game.banlists import Banlist
from digimon_card_game.cards import Card
from digimon_card_game.seeders import banlist_seeder
from digimon_card_game.seeders.card_seeder import argomon
from digimon_card_game.seeders.card_seeder import blossomon
from digimon_card_game.seeders.card_seeder import calling_from_the_darkness
from digimon_card_game.seeders.card_seeder import dorugreymon
from digimon_card_game.seeders.card_seeder import eyesmon
from digimon_card_game.seeders.card_seeder import grankuwagamon
from digimon_card_game.seeders.card_seeder import greymon_x_antibody
from digimon_card_game.seeders.card_seeder import hidden_potential_discovered
from digimon_card_game.seeders.card_seeder import ice_wall
from digimon_card_game.seeders.card_seeder import impmon
from digimon_card_game.seeders.card_seeder import jetsilphymon
from digimon_card_game.seeders.card_seeder import mega_digimon_fusion
from digimon_card_game.seeders.card_seeder import reinforcing_memory_boost
from digimon_card_game.seeders.card_seeder import saviorhuckmon
from digimon_card_game.seeders.card_seeder import shoutmon_x4
from digimon_card_game.seeders.card_seeder import sunrise_buster
from digimon_card_game.seeders.card_seeder import tommy_himi
from digimon_card_game.seeders.card_seeder import weregarurumon


def assert_banlist(banlist: Banlist, date: Date, number_of_copies_by_card: dict[Card, int]) -> None:
    assert banlist.date == date
    assert banlist.number_of_copies_by_card == number_of_copies_by_card


def test_01_banlist_2022_05_13() -> None:
    assert_banlist(banlist=banlist_seeder.banlist_2022_05_13(),
                   date=Date(2022, 5, 13),
                   number_of_copies_by_card={
                       saviorhuckmon(): 1,
                       eyesmon(): 1
                   })


def test_02_banlist_2021_04_01() -> None:
    assert_banlist(banlist=banlist_seeder.banlist_2021_04_01(),
                   date=Date(2021, 4, 1),
                   number_of_copies_by_card={
                       argomon(): 1,
                       hidden_potential_discovered(): 1
                   })


def test_03_banlist_2022_02_25() -> None:
    assert_banlist(banlist=banlist_seeder.banlist_2022_02_25(),
                   date=Date(2022, 2, 25),
                   number_of_copies_by_card={
                       mega_digimon_fusion(): 0,
                       reinforcing_memory_boost(): 1,
                       ice_wall(): 1
                   })


def test_04_banlist_2022_08_01() -> None:
    assert_banlist(banlist=banlist_seeder.banlist_2022_08_01(),
                   date=Date(2022, 8, 1),
                   number_of_copies_by_card={
                       jetsilphymon(): 1,
                       tommy_himi(): 1
                   })


def test_05_banlist_2022_11_11() -> None:
    assert_banlist(banlist=banlist_seeder.banlist_2022_11_11(),
                   date=Date(2022, 11, 11),
                   number_of_copies_by_card={
                       calling_from_the_darkness(): 1,
                       sunrise_buster(): 1,
                       dorugreymon(): 1,
                       shoutmon_x4(): 1
                   })


def test_06_banlist_2023_04_01() -> None:
    assert_banlist(banlist=banlist_seeder.banlist_2023_04_01(),
                   date=Date(2023, 4, 1),
                   number_of_copies_by_card={
                       greymon_x_antibody(): 1
                   })


def test_07_banlist_2023_06_01() -> None:
    assert_banlist(banlist=banlist_seeder.banlist_2023_06_01(),
                   date=Date(2023, 6, 1),
                   number_of_copies_by_card={
                       blossomon(): 1,
                       impmon(): 1,
                       weregarurumon(): 1,
                       grankuwagamon(): 1
                   })
