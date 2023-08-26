from typing import TypeAlias

from .digi_egg_card import DigiEggCard
from .digimon_card import DigimonCard
from .option_card import OptionCard
from .tamer_card import TamerCard

Card: TypeAlias = DigiEggCard | DigimonCard | TamerCard | OptionCard
