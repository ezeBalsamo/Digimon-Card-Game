from src.digimon_card_game import CardColor


def test_01_colors():
    enum_values = set(map(lambda enum_item: enum_item.value, list(CardColor)))
    assert enum_values == {'Red', 'Blue', 'Yellow', 'Green', 'Black', 'Purple', 'White'}
