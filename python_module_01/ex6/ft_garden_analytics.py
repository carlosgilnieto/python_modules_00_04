#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int):
        """
        Create a Plant object
        Args:
            name: Name of the plant
            heigth: Height of the plant
        """
        self.name = name
        self.height = height
        self.type = "regular"

    def grow(self, grow_height: int):
        """Grow the plant {grow_height}cm"""
        self.height += grow_height
        print(f"{self.name} grew {grow_height}cm")

    def get_info(self) -> str:
        """Return a string with the info about the plant"""
        return f"- {self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name, height, color: str):
        """
        Create a new flower with color of the bloom
        Args:
            name: Name of the flower
            heigth: Height of the flower
            color: Color of the flower
        """
        super().__init__(name, height)
        self.color = color
        self.type = "flowering"

    def get_info(self):
        """Return a string with the info about the FloweringPlant"""
        self.color = self.color.lower()
        return super().get_info() + f", {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize: int):
        """
        Create a new flower with a score
        Args:
            name: Name of the flower
            heigth: Height of the flower
            color: Color of the flower
            prize: The score of the flower
        """
        super().__init__(name, height, color)
        self.prize = prize
        self.type = "prize"

    def get_info(self):
        """Return a string with the info about the PrizeFlower"""
        return super().get_info() + f", Prize points: {self.prize}"


class Garden:

    def __init__(self, player: str):
        """Create a new empty garden """
        self.player = player
        self.plants: Plant = []
        self.grow_history = 0
        self.total_plants = 0

    def add_plant(self, plant: Plant, info=True):
        """Add the plant to the garden"""
        self.plants.append(plant)
        self.total_plants += 1
        if info:
            print(f"Added {plant.name} to {self.player}'s garden")

    def grow_all(self, height: int, info=True):
        """Grow all the plants in the garden"""
        if info:
            print(f"\n{self.player} is helping all plants grow...")
        for item in self.plants:
            item.grow(height)
            self.grow_history += height

    def info(self):
        """Print info about the plants in the garden"""
        print(f"\n=== {self.player}'s Garden Report ===")
        print("Plants in garden:")
        for item in self.plants:
            print(item.get_info())


class GardenManager:
    total_gardens = 0

    class GardenStats:
        @staticmethod
        def garden_report(garden: Garden):
            """Calculate the stats of the garden and print the info"""
            count_regular = 0
            count_flower = 0
            count_prize = 0
            score = 0
            for plant in garden.plants:
                score += plant.height
                if plant.type == "prize":
                    count_prize += 1
                elif plant.type == "flowering":
                    count_flower += 1
                elif plant.type == "regular":
                    count_regular += 1
            print()
            print(f"Plants added: {garden.total_plants}"
                  f", Total growth: {garden.grow_history}cm")
            print(f"Plant types: {count_regular} regular, "
                  f"{count_flower} flowering, {count_prize} prize flowers")

        @staticmethod
        def garden_score(garden: Garden) -> int:
            """Calculate the score of the garden"""
            score = 0
            for p in garden.plants:
                score += p.height
                if p.type == "flowering":
                    score += 15
                if p.type == "prize":
                    score += p.prize + 15
            return score

        @staticmethod
        def check_height(garden: Garden) -> bool:
            """Check if all the height in the gardens is positives"""
            for p in garden.plants:
                if (p.height <= 0):
                    return False
            return True

        @staticmethod
        def report(gardens: dict):
            """Print a report about all the gardens"""
            check_h = True
            first = True
            score_str = ""
            for g in gardens:
                check_h = GardenManager.GardenStats.check_height(gardens[g])
                score = GardenManager.GardenStats.garden_score(gardens[g])
                if first:
                    score_str += f"{g}: {score}, "
                    first = False
                else:
                    score_str += f"{g}: {score}"

            print()
            print(f"Height validation test: "
                  f"{check_h}")
            print(f"Garden scores - {score_str}")
            print(f"Total gardens managed: {GardenManager.total_gardens}")

    def __init__(self):
        """Create a new garden with """
        self.gardens = {}

    def get_garden(self, player: str) -> Garden:
        """Get the garden of the {player}"""
        return self.gardens[player]

    @classmethod
    def create_garden_network(cls, players: list):
        """Create a new garden network with a list of players"""
        manager = cls()
        for player in players:
            manager.gardens[player] = Garden(player)
            GardenManager.total_gardens += 1
        return manager


def ft_garden_analytics():
    print("=== Garden Management System Demo ===\n")
    players = ["Alice", "Bob"]

    garden_manager = GardenManager.create_garden_network(players)

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "Red")
    sunflower = PrizeFlower("Sunflower", 50, "Yellow", 10)

    alice_garden = garden_manager.get_garden("Alice")
    bob_garden = garden_manager.get_garden("Bob")

    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)

    bob_garden.add_plant(Plant("Spruce Tree", 92), False)

    alice_garden.grow_all(1)

    alice_garden.info()

    garden_manager.GardenStats.garden_report(alice_garden)
    garden_manager.GardenStats.report(garden_manager.gardens)


if __name__ == "__main__":
    ft_garden_analytics()
