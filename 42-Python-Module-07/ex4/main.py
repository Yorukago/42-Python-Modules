from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("=== DataDeck Tournament Platform ===")

    tp = TournamentPlatform()
    dragon = TournamentCard("Fire Dragon", 5, "Legendary", 10)
    wizard = TournamentCard("Ice Wizard", 4, "Rare", 6)

    tp.register_card(dragon)
    tp.register_card(wizard)

    interfaces = ["Combatable", "Rankable"]
    print(f"Tournament Card: {dragon.name}")
    print(f"- Interfaces: {interfaces}")
    print(f"- Rating: {dragon.rating}")

    print("\nCreating tournament match...")
    res = tp.run_match(dragon, wizard)
    print(f"Match result: {res}")

    print("\nTournament Leaderboard:")
    d_name = dragon.name
    d_rating = dragon.rating
    d_rec = f"{dragon.wins}-{dragon.losses}"
    d_stats = f"{d_name} - Rating: {d_rating} ({d_rec})"

    w_name = wizard.name
    w_rating = wizard.rating
    w_rec = f"{wizard.wins}-{wizard.losses}"
    w_stats = f"{w_name} - Rating: {w_rating} ({w_rec})"

    print(f"1. {d_stats}")
    print(f"2. {w_stats}")

    print("\nPlatform Report:")
    report = tp.get_platform_report()
    print(f"{report}")

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
