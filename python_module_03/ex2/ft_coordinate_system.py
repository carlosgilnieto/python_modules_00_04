#!/usr/bin/env python3
import math


def new_coord(x, y, z) -> tuple:
    """Validate the coordinate and return a tuple"""
    try:
        coords = (int(x), int(y), int(z))
    except Exception:
        print("Error: All arguments must be valid integers")
    else:
        return coords


def parsing_coord(args: str, info=False) -> tuple:
    """Parsing the coordinates and validate if are int"""
    values = args.split(",")
    try:
        for val in values:
            int(val)
    except ValueError as error:
        print(f"Error parsing coordinates: {error}")
        return ("ValueError", error)
    else:
        return new_coord(int(values[0]), int(values[1]), int(values[2]))


def calculate_distance(pos1: tuple, pos2: tuple) -> float:
    """Calculate the distance between 2 positions"""
    return math.sqrt((pos2[0]-pos1[0])**2 +
                     (pos2[1]-pos1[1])**2 +
                     (pos2[2]-pos1[2])**2)


def ft_coordinate_system():
    print("=== Game Coordinate System ===")
    pos = new_coord(10, 20, 5)
    zero = new_coord(0, 0, 0)
    print(f"Position created: {pos}")
    distance = calculate_distance(zero, pos)
    print(f"Distance between {zero} and {pos}: {distance:.2f}")

    parsed = "3,4,0"
    print(f"\nParsing coordinates: \"{parsed}\"")
    parsed_coords = parsing_coord(parsed, True)
    print(f"Parsed position: {parsed_coords}")
    distance = calculate_distance(zero, parsed_coords)
    print(f"Distance between {zero} and {parsed_coords}: {distance:.2f}")

    invalid_coords = "abc,def,ghi"
    print(f"\nParsing invalid coordinates: \"{invalid_coords}\"")
    (type, error,) = parsing_coord(invalid_coords)
    print(f"Error details - Type: {type}, Args: {error.args}")

    print("\nUnpacking demostration:")
    (x, y, z) = parsing_coord("3,4,0")
    print(f"Player at x={x}, y={y}, z={z}")
    coords = new_coord(3, 4, 0)
    if coords:
        (x, y, z) = coords
        print(f"Coordinates: X={x}, Y={y}, Z={z}")


# if __name__ == "__main__":
#     ft_coordinate_system()
