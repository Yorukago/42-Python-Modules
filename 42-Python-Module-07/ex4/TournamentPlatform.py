class TournamentPlatform:
    def __init__(self):
        self.registry = []
        self.matches_played = 0

    def register_card(self, card):
        self.registry.append(card)

    def run_match(self, card1, card2):
        c1_wins = card1.atk_power >= card2.atk_power

        card1.update_rating(card2.rating, c1_wins)
        card2.update_rating(card1.rating, not c1_wins)

        self.matches_played += 1
        winner = card1 if c1_wins else card2
        loser = card2 if c1_wins else card1

        return {
            "winner": winner.name,
            "loser": loser.name,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }

    def get_platform_report(self) -> dict:
        ratings = [c.rating for c in self.registry]
        avg_rating = sum(ratings) / len(ratings) if ratings else 0
        return {
            "total_cards": len(self.registry),
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active"
        }
