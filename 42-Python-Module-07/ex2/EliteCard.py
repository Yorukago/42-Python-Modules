from ex0.Card import Card
from .Combatable import Combatable
from .Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str,
                 atk: int, mag: int):
        super().__init__(name, cost, rarity)
        self.atk_power = atk
        self.mag_power = mag
        self.mana_pool = 4

    def play(self, game_state: dict) -> dict:
        return {"card_played": self.name, "effect": "Elite Warrior enters!"}

    def attack(self, target) -> dict:
        return {"attacker": self.name, "target": target,
                "damage": self.atk_power, "combat_type": "melee"}

    def defend(self, incoming_damage: int) -> dict:
        """Implementation of Combatable.defend."""
        blocked = 3
        return {
            "defender": self.name,
            "damage_taken": incoming_damage - blocked,
            "damage_blocked": blocked,
            "still_alive": True
        }

    def get_combat_stats(self) -> dict:
        return {"attack": self.atk_power}

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return {"caster": self.name, "spell": spell_name,
                "targets": targets, "mana_used": 4}

    def channel_mana(self, amount: int) -> dict:
        self.mana_pool += amount
        return {"channeled": amount, "total_mana": self.mana_pool}

    def get_magic_stats(self) -> dict:
        return {"magic_power": self.mag_power}
