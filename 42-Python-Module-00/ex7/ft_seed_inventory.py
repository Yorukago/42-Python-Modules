def ft_seed_inventory(seed_name, quantity, unit) -> None:
    seed_name = seed_name.capitalize()
    if unit == "packets":
        print(f"{seed_name} seeds: {quantity} packets available.")
    elif unit == "grams":
        print(f"{seed_name} seeds: {quantity} grams total.")
    elif unit == "area":
        print(f"{seed_name} seeds: covers {quantity} square meters.")
    else:
        print(f"{seed_name} seeds: {quantity} {unit}")
