#!/usr/bin/env python3
def water_plants(plant_list: list):
    """Water the plants and manage if any item is not a plant"""
    error = False
    print("Opening watering system")
    try:
        for plant in plant_list:
            print("Watering " + plant)
    except Exception:
        error = True
        print(f"Error: Cannot water {plant} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")
        if error is False:
            print("Watering completed succesfully!")


def test_watering_system():
    """Print the output of the subject"""
    print("=== Garden Watering System ===")
    print("\nTesting normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("\nTesting with error...")
    water_plants(["tomato", None])
    print("Cleanup always happens, even with errors!")


# if __name__ == "__main__":
#     test_watering_system()
