#!/usr/bin/env python3
class GardenError(Exception):
    """Custom error for garden"""
    pass


class PlantError(GardenError):
    """Custom error for the plants"""
    pass


class WaterError(GardenError):
    """Custom error for the water"""
    pass


def ft_test_water():
    """Throw an error for WaterError"""
    print("\nTesting WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as error:
        print(f"Caught WaterError: {error}")


def ft_test_tomato():
    """Throw an error for PlantError"""
    print("\nTesting PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as error:
        print(f"Caught PlantError: {error}")


def ft_test_garden():
    """Throw an errors for GardenError"""
    errors = [PlantError("The tomato plant is wilting!"),
              WaterError("Not enought water in the tank!")]
    print("\nTesting catching all garden errors...")
    for e in errors:
        try:
            raise e
        except GardenError as txt:
            print(f"Caught a garden error: {txt}")


def ft_custom_error():
    print("=== Custom Garden Errors Demo ===")
    ft_test_tomato()
    ft_test_water()
    ft_test_garden()
    print("\nAll custom error types work correctly!")


# if __name__ == "__main__":
#     ft_custom_error()
