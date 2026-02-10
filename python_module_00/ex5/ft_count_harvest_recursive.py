def ft_count_harvest_recursive():
    total_day = int(input("Days until harves: "))

    def recursive(day):
        if day < total_day:
            print(f"Day {day}")
            recursive(day + 1)
        else:
            return

    recursive(1)
    print("Harvest time!")
