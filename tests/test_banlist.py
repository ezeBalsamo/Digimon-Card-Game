from digimon_card_game.banlists.banlist import Banlist
from tests.assertions.dictionary.assertions import assert_dict_raises_not_minimum_length


def test_01_cannot_create_banlist_without_cards():
    assert_dict_raises_not_minimum_length('number_of_copies_by_card', 1,
                                          lambda invalid_cards: Banlist(number_of_copies_by_card=invalid_cards))
