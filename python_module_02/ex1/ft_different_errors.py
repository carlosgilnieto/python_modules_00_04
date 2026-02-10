#!/usr/bin/env python3
def garden_operations(tmp_str):
    """Testing some types of error"""
    if tmp_str == "multi":
        try:
            int(tmp_str)
        except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
            print("Caught an error, but program continues!")
            return
    try:
        if tmp_str == "abc":
            int(tmp_str)
        elif tmp_str == 0:
            10 / tmp_str
        elif tmp_str == "missing.txt":
            raise FileNotFoundError(f"No such file '{tmp_str}'")
        elif tmp_str == "missing_plant":
            garden = {"potato": 1}
            garden[tmp_str]
    except ValueError as error:
        if tmp_str == "multi":
            raise error
        print("Caught ValueError: invalid literal for int()")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division  by zero")
    except FileNotFoundError as txt:
        print(f"Caught FileNotFoundError: {txt}")
    except KeyError:
        print("Caught KeyError: missing_plant")


def test_error_types():
    print("=== Garden Error Types Demo ===")

    print("\nTesting ValueError...")
    garden_operations("abc")

    print("\nTesting ZeroDivisionError...")
    garden_operations(0)

    print("\nTesting FileNotFoundError...")
    garden_operations("missing.txt")

    print("\nTesting KeyError...")
    garden_operations("missing_plant")

    print("\nTesting multiple errors together...")
    garden_operations("multi")

    print("\nAll error types tested succesfully!")


# if __name__ == "__main__":
#     test_error_types()
