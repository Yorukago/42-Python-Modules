from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main():
    print("=== DataDeck Game Engine ===")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine(factory, strategy)

    print(f"Strategy: {strategy.get_strategy_name()}")
    print(engine.prepare_game())

    print("\nSimulating Turn:")

    result = engine.simulate_turn()
    print(f"AI Decision: {result}")

    print("\nAbstract Factory and Strategy patterns verified!")


if __name__ == "__main__":
    main()
