from digimon_card_game.banlists.banlist import Banlist
from tests.assertions import assert_attr_raises_not_blank


def test_01_name_must_not_be_blank():
    assert_attr_raises_not_blank('name',
                                 lambda invalid_name: Banlist(name=invalid_name))
