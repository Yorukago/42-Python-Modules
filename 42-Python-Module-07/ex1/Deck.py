import random
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard


class Deck:
    def __init__(self) -> None:
        self.cards = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for i, card in enumerate(self.cards):
            if card.name == card_name:
                self.cards.pop(i)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        return self.cards.pop() if self.cards else None

    def get_deck_stats(self) -> dict:

        if not self.cards:
            return {"total_cards": 0}
        costs = [c.cost for c in self.cards]
        stats = {
            "total_cards": len(self.cards),
            "creatures": sum(1 for c in self.cards
                             if isinstance(c, CreatureCard)),
            "spells": sum(1 for c in self.cards
                          if isinstance(c, SpellCard)),
            "artifacts": sum(1 for c in self.cards
                             if isinstance(c, ArtifactCard)),
            "avg_cost": sum(costs) / len(costs)
        }
        return stats
