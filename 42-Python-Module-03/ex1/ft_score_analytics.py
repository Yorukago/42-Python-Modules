import sys

"""
Continuing from the flow of ex1, now we are grabbing said
args and stuffing them through MATH to calculate shit!!
"""


def process_scores(args: list[str]) -> None:
    scores: list[int] = []

    for arg in args:
        try:
            scores.append(int(arg))
        except ValueError:
            print(
                f"Warning: '{arg}' is not a valid score "
                "and will be skipped."
            )

    if not scores:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
        return

    total_players: int = len(scores)
    total_sum: int = sum(scores)
    avg_score: float = total_sum / total_players
    high_score: int = max(scores)
    low_score: int = min(scores)
    score_range: int = high_score - low_score

    print(f"Scores processed: {scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_sum}")
    print(f"Average score: {avg_score}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}")


def main() -> None:
    print("=== Player Score Analytics ===\n")
    if len(sys.argv) < 2:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
        return

    process_scores(sys.argv[1:])


if __name__ == "__main__":
    main()
