class GameEngine:
    def __init__(self, factory, strategy):
        self.factory = factory
        self.strategy = strategy
        self.hand = []

    def prepare_game(self):
        self.hand.append(self.factory.create_creature("Dragon"))
        self.hand.append(self.factory.create_spell("Heal"))
        return f"Game prepared with {self.factory.__class__.__name__}"

    def simulate_turn(self):
        return self.strategy.execute_turn(self.hand, [])
