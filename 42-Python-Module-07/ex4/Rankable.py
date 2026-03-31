from abc import ABC, abstractmethod


class Rankable(ABC):
    @abstractmethod
    def update_rating(self, opponent_rating: int, won: bool) -> None:
        pass

    @abstractmethod
    def get_rank_stats(self) -> dict:
        pass
