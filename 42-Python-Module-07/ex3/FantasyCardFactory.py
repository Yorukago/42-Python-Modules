from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from .CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    def create_creature(self, name: str = "Goblin") -> CreatureCard:
        return CreatureCard(name, 2, "Common", 2, 2)

    def create_spell(self, name: str = "Fireball") -> SpellCard:
        return SpellCard(name, 3, "Rare", "Fire")

    def create_artifact(self, name: str = "Shield") -> ArtifactCard:
        return ArtifactCard(name, 1, "Common", 5, "Defense")

    def create_themed_deck(self, size: int) -> dict:
        return {"theme": "Fantasy", "size": size, "status": "Ready"}

    def get_supported_types(self) -> dict:
        return {"types": ["Creature", "Spell", "Artifact"]}
