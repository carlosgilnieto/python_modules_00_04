#!/usr/bin/env python3
class GardenError(Exception):
    """Custom error for the garden"""
    pass


class PlantError(GardenError):
    """Custom error for plants"""
    pass


class HealthError(GardenError):
    """Custom error for the health of the plants"""
    pass


class Plant():
    def __init__(self, name: str, water_lvl: int, sun_lvl: int):
        self.name = name
        self.water_lvl = water_lvl
        self.sun_lvl = sun_lvl


class GardenManager:
    """Create a garden and manages it"""
    def __init__(self):
        self.plants = []
        self.water = 2

    def add_plant(self, plant: Plant):
        """Add a plant to the garden"""
        try:
            if not plant.name:
                raise PlantError("Plant name cannot be empty!")
            else:
                print(f"Added {plant.name} successfully")
                self.plants.append(plant)
        except PlantError as error:
            print(f"Error adding plant: {error}")

    def watering_plants(self):
        """Watering all the plants in the garden"""
        if self.water < 1:
            raise GardenError("Not enough water in tank")
        print("\nWatering plants...")
        print("Opening watering system")
        try:
            for plant in self.plants:
                plant.water_lvl += 1
                self.water -= 1
                print("Watering " + plant.name + " - success")
        except Exception:
            print(f"Error: Cannot water {plant.name} - invalid plant!")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self):
        """Checking the health of all the plants in the garden"""
        print("\nChecking plant health...")
        for plant in self.plants:
            try:
                if plant.water_lvl < 1:
                    raise HealthError(f"Water level {plant.water_lvl}"
                                      f" is too low (min 1)")
                elif plant.water_lvl > 10:
                    raise HealthError(f"Water level {plant.water_lvl}"
                                      f" is too high (max 10)")
                elif plant.sun_lvl < 2:
                    raise HealthError(f"Sunlight hours {plant.sun_lvl}"
                                      f" is too low (min 2)")
                elif plant.sun_lvl > 12:
                    raise HealthError(f"Sunlight hours {plant.sun_lvl}"
                                      f" is too high (max 12)")
                print(f"{plant.name}: healthy (water: {plant.water_lvl}"
                      f", sun: {plant.sun_lvl})")
            except HealthError as error:
                print(f"Error checking {plant.name}: {error}")


def ft_garden_manager():
    manager = GardenManager()

    print("=== Garden Management System ===")

    print("\nAdding plants to garden...")
    manager.add_plant(Plant("tomato", 4, 8))
    manager.add_plant(Plant("lettuce", 14, 6))
    manager.add_plant(Plant("", 4, 8))

    manager.watering_plants()
    manager.check_plant_health()

    print("\nTesting error recovery...")
    try:
        manager.watering_plants()
    except GardenError as error:
        print(f"Caught GardenError: {error}")
        manager.water = 2
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


# if __name__ == "__main__":
#     ft_garden_manager()
