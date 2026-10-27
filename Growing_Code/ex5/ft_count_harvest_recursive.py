def ft_count_harvest_recursive() -> None:
    days: int = int(input("Days until harvest:"))

    def helper(days):
        if (days > 1):
            helper(days-1)
        print(f"Day {days}")
    helper(days)
    print("Harvest time!")
