from dataclasses import dataclass
from charactertype import CharacterType

class Character:
    name: str
    character_type: CharacterType
    health: int
    attack_power: int
    