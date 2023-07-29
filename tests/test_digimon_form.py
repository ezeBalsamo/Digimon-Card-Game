from src.digimon_card_game import DigimonForm


def test_01_digimon_forms():
    enum_values = set(map(lambda enum_item: enum_item.value, list(DigimonForm)))
    assert enum_values == {'In-Training', 'Rookie', 'Champion', 'Mega', 'Ultimate'}
