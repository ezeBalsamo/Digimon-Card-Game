from datetime import date
from digimon_card_game.banlists.banlist import Banlist
from digimon_card_game.cards import shadow_wing
from tests.assertions.dictionary.assertions import assert_dict_raises_not_minimum_length


def test_01_cannot_create_banlist_without_cards():
    assert_dict_raises_not_minimum_length('number_of_copies_by_card', 1,
                                          lambda invalid_cards: Banlist(
                                              date=date.today(),
                                              number_of_copies_by_card=invalid_cards))


def test_02_instance_creation_and_accessing():
    today = date.today()
    number_of_copies_by_card = {shadow_wing(): 1}
    banlist = Banlist(date=today, number_of_copies_by_card=number_of_copies_by_card)

    assert banlist.date == today
    assert banlist.number_of_copies_by_card == number_of_copies_by_card
