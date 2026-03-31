def ft_count_harvest_recursive() -> None:
    n = int(input("Enter days until harvest: "))

    def ft_counter(days):
        if days > n:
            print("Harvest time!")
            return
        print(f"Day {days}")
        ft_counter(days + 1)
    ft_counter(1)
