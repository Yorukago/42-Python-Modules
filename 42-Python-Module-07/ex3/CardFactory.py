from abc import ABC, abstractmethod
from ex0.Card import Card


class CardFactory(ABC):
    @abstractmethod
    def create_creature(self, name: str = None) -> Card:
        pass

    @abstractmethod
    def create_spell(self, name: str = None) -> Card:
        pass

    @abstractmethod
    def create_artifact(self, name: str = None) -> Card:
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        pass

    @abstractmethod
    def get_supported_types(self) -> dict:
        pass
