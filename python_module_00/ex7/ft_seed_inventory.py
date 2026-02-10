def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type = seed_type.capitalize()
    if unit == "packets":
        print(seed_type + f" seeds: {quantity} " + unit + " available")
    elif unit == "grams":
        print(seed_type + f" seeds: {quantity} " + unit + " total")
    elif unit == "area":
        print(seed_type + f" seeds: covers {quantity} squares meters")
    else:
        print(seed_type + f" seeds: {quantity} Unknown unit type")
