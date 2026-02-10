#!/usr/bin/env python3
def check_temperature(temp_str):
    """
    Check if is a real number and print a msg
    """
    try:
        print(f"\nTesting temperature: {temp_str}")
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
    else:
        if temp >= 0 and temp <= 40:
            print(f"Temperature {temp}ºC is perfect for plants!")
        elif temp < 0:
            print(f"Error: {temp}ºC is too cold for plants (min 0ºC)")
        else:
            print(f"Error: {temp}ºC is too hot for plants (max 40ºC)")


def test_temperature_input():
    """Test the ex0"""
    print("=== Garden Temperature Checker ===")
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")
    print("\nAll tests completed - program didn't crash!")


# if __name__ == "__main__":
#     test_temperature_input()
