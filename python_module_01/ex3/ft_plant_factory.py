#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, age: int):
        """
        Create a Plant object
        - name: Name of the plant
        - heigth: Height of the plant
        - age: Age of the plant
        """
        self.name = name
        self.height = height
        self.current_age = age
        print(f"Created: {name} ({height}cm, {age} days)")


def ft_plant_factory():
    """
    Create 5 plants in a list and print the number of plants created
    """
    print("=== Plant Factory Output ===")
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]
    n = 0
    for i in plants:
        n += 1

    print(f"\nTotal plants created: {n}")


if __name__ == "__main__":
    ft_plant_factory()
