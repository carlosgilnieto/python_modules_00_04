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
        self.age = age

    def info(self) -> str:
        """
        Print the info about the plant
        """
        return f"{self.name}: {self.height} cm, {self.age} days old"


def plant_registry():
    """
    Create 3 plants and print the info
    """
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry")
    print(plant1.info())
    print(plant2.info())
    print(plant3.info())


if __name__ == "__main__":
    plant_registry()
