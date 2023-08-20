from typing import TypeAlias

from . import DigiEggCard, DigimonCard, TamerCard, OptionCard

Card: TypeAlias = DigiEggCard | DigimonCard | TamerCard | OptionCard
