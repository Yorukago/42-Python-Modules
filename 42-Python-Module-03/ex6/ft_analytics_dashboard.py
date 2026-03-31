def main() -> None:
    """
    Processes and displays game analytics using
    various comprehension techniques
    This function demonstrates how to transform raw list
    data into filtered lists,mappable dictionaries, and unique sets—all
    without using traditional for-loops
    """
    raw_data: list[dict[str, any]] = [
        {"name": "alice", "score": 2300, "ach": 5, "reg": "north"},
        {"name": "bob", "score": 1800, "ach": 3, "reg": "central"},
        {"name": "charlie", "score": 2150, "ach": 7, "reg": "north"},
        {"name": "diana", "score": 2050, "ach": 4, "reg": "east"}
    ]

    print("=== Game Analytics Dashboard ===")

    print("\n=== List Comprehension Examples ===")
    # these create new lists by filtering or transforming the raw_data
    high_scorers: list[str] = [
        p["name"] for p in raw_data if p["score"] > 2000
    ]
    scores_doubled: list[int] = [p["score"] * 2 for p in raw_data]
    active_players: list[str] = [p["name"] for p in raw_data[:3]]

    # we also show the scores and active players
    print(f"High scorers (>2000): {high_scorers}")
    print(f"Scores doubled: {scores_doubled}")
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")
    """
    dict comprehensions allow us to reshape data into a searchable format
    instead of looping to find a score, we create a name -> score map
    """
    # so here we just..yeah grab the raw_data and put it on the dict
    player_scores: dict[str, int] = {
        p["name"]: p["score"] for p in raw_data
    }

    # then we categorize it by score
    categories: dict[str, int] = {
        "high": len([p for p in raw_data if p["score"] >= 2000]),
        "medium": len([p for p in raw_data if 1500 <= p["score"] < 2000]),
        "low": len([p for p in raw_data if p["score"] < 1500])
    }

    # then we also see their achievemnts...but not diana, she sucks
    ach_counts: dict[str, int] = {
        p["name"]: p["ach"] for p in raw_data if p["name"] != "diana"
    }

    # and then we print it all nice and prettyyy
    print(f"Player scores: {player_scores}")
    print(f"Score categories: {categories}")
    print(f"Achievement counts: {ach_counts}")

    print("\n=== Set Comprehension Examples ===")
    """
    set comprehensions look like dicts but without the 'key: value' colon
    they are perfect for finding unique values in a dataset
    """
    unique_players: set[str] = {p["name"] for p in raw_data}
    unique_regions: set[str] = {p["reg"] for p in raw_data}

    raw_ach = ["level_10", "first_kill", "level_10", "boss_slayer"]
    unique_ach: set[str] = {a for a in raw_ach}

    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_ach}")
    print(f"Active regions: {unique_regions}")

    print("\n=== Combined Analysis ===")
    total_players: int = len(unique_players)
    avg_score: float = sum(player_scores.values()) / total_players
    # This uses the .get method as a key to find the name with
    # the highest score
    top_name: str = max(player_scores, key=player_scores.get)

    print(f"Total players: {total_players}")
    print(f"Average score: {avg_score}")
    print(f"Top performer: {top_name} ({player_scores[top_name]} points)")


if __name__ == "__main__":
    main()


"""
so comprehensions allow for easier understanding of what im doing to
someone else, since i describe the transformation, this is good! cuz it
reduces the chance for having bugs and problems down the line, and makes
the reading much easier, and the also added plus is that since this is
really easy to understand, maintencance for dbs is a breeze too
"""
