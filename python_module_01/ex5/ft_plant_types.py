#!/usr/bin/env python3
class Plant():
    """Plant Class"""
    def __init__(self, name: str, height: int, age: int):
        """Setup the plant"""
        self.name = name.capitalize()
        self.height = height
        self.age = age


class Flower(Plant):
    """Flower Class inherits from Plant class"""
    def __init__(self, name: str, height: int, age: int,
                 color: str,
                 bloom_time: int):
        """Create a flower that inherits from a plant"""
        super().__init__(name, height, age)
        self.color = color
        self.bloom_time = bloom_time

    def get_info(self):
        """print info about the Flower"""
        print(f"\n{self.name} (Flower): {self.height}cm, {self.age} days, "
              f"{self.color} color")
        self.bloom()

    def bloom(self):
        """Check how if the flower is bloom or not"""
        if self.bloom_time > 0:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not yet bloomed")


class Tree(Plant):
    """Tree Class inherits from Plant class"""
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int,
                 shade: bool):
        """Create a tree that inherits from a plant"""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade = shade

    def get_info(self):
        """print info about the Flower"""
        print(f"\n{self.name} (Tree): {self.height}cm, {self.age} days, "
              f"{self.trunk_diameter}cm diameter")
        if self.shade:
            print(f"{self.name} provides {self.produce_shade():.0f}"
                  f" square meters of shade")

    def produce_shade(self) -> int:
        """calculate the are of the shadow"""
        square = (self.trunk_diameter/10) ** 2
        return 3.14 * square


class Vegetable(Plant):
    """Vegetable Class inherits from Plant class"""
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str,
                 vitamin: str):
        """Create a vegetable that inherits from a plant"""
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.vitamin = vitamin.capitalize()

    def get_info(self):
        """print info about the Vegetable"""
        print(f"\n{self.name} (Flower): {self.height}cm, {self.age} days, "
              f"{self.harvest_season} harvest")
        print(f"{self.name} is rich in vitamin {self.vitamin}")


def ft_plant_types():
    """Create 3 types of Plants and print the info about each one"""
    print("=== Garden Plant Types ===")
    plant1 = Flower("rose", 25, 30, "red", 20)
    plant1.get_info()

    plant2 = Tree("oak", 500, 1825, 50, True)
    plant2.get_info()

    plant3 = Vegetable("Tomato", 80, 90, "summer", "c")
    plant3.get_info()


if __name__ == "__main__":
    ft_plant_types()
