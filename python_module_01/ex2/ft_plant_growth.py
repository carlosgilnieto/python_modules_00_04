#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, grow_rate: int, age: int):
        """
        Create a Plant object
        - name: Name of the plant
        - heigth: Height of the plant
        - grow_rate: The height of the grow in a day
        - age: Age of the plant
        """
        self.name = name
        self.height = height
        self.grow_rate = grow_rate
        self.current_age = age

    def get_info(self) -> str:
        """
        print the info about the plant
        """
        return f"{self.name}: {self.height} cm, {self.current_age} days old"

    def grow(self, days: int):
        """Grow the plant"""
        self.height += self.grow_rate * days

    def age(self, days: int):
        """age the plant"""
        self.current_age += days


def ft_plant_growth():
    """
    Create a plant and see how the info change with the time
    """
    plant1 = Plant("Rose", 25, 1, 30)
    print("=== Day 1 ===")
    print(plant1.get_info())
    height = plant1.height
    print("=== Day 7 ===")
    plant1.age(6)
    plant1.grow(6)
    print(plant1.get_info())
    print(f"Growth this week: +{plant1.height - height}cm")


if __name__ == "__main__":
    ft_plant_growth()
