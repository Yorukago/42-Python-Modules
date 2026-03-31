from ex0.Card import Card
from ex2.Combatable import Combatable
from .Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str, atk: int):
        super().__init__(name, cost, rarity)
        self.atk_power = atk
        self.rating = 1200
        self.wins = 0
        self.losses = 0

    def play(self, game_state: dict) -> dict:
        return {"action": "tournament_play", "card": self.name}

    def attack(self, target) -> dict:
        return {"attacker": self.name, "damage": self.atk_power}

    def defend(self, incoming_damage: int) -> dict:
        return {"defender": self.name, "status": "blocking"}

    def get_combat_stats(self) -> dict:
        return {"attack": self.atk_power}

    def update_rating(self, opponent_rating: int, won: bool) -> None:
        # Simple Elo-like logic
        adjustment = 16 if won else -16
        self.rating += adjustment
        if won:
            self.wins += 1
        else:
            self.losses += 1

    def get_rank_stats(self) -> dict:
        return {
            "rating": self.rating,
            "record": f"{self.wins}-{self.losses}"
        }
