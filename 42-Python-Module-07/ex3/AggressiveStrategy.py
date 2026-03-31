from .GameStrategy import GameStrategy


def get_card_cost(card):
    """Helper function to extract cost for sorting."""
    return card.cost


class AggressiveStrategy(GameStrategy):
    def get_strategy_name(self) -> str:
        return "Aggressive AI"

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """Play the most expensive card possible without using lambdas."""
        if not hand:
            return {"action": "none", "played": None}

        playable = sorted(hand, key=get_card_cost, reverse=True)
        chosen = playable[0]

        return {
            "action": "play_card",
            "card": chosen.name,
            "strategy": self.get_strategy_name()
        }

    def prioritize_targets(self, available_targets: list) -> list:

        return sorted(available_targets, reverse=True)
