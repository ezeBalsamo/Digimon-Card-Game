from digimon_card_game.banlists.banlist import Banlist
from tests.assertions import assert_attr_raises_not_blank
from tests.assertions.dictionary.assertions import assert_dict_raises_not_minimum_length


def test_01_name_must_not_be_blank():
    assert_attr_raises_not_blank('name',
                                 lambda invalid_name: Banlist(
                                     name=invalid_name,
                                     number_of_copies_by_card={}))


def test_02_cannot_create_banlist_without_cards():
    assert_dict_raises_not_minimum_length('number_of_copies_by_card', 1,
                                          lambda invalid_cards: Banlist(
                                              name="Banlist",
                                              number_of_copies_by_card=invalid_cards))
