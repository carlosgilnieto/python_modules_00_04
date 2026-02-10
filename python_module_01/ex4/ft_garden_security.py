#!/usr/bin/env python3
class SecurePlant:
    def __init__(self, name: str, height: int, age: int):
        """
        Create a SecurePlant object
        - name: Name of the plant
        - heigth: Height of the plant (Only + numbers)
        - age: Age of the plant (Only + numbers)
        """
        self.name = name
        self.set_height(height)
        self.set_age(age)
        print(f"Plant created: {name}")

    def get_height(self) -> int:
        """ get the height of the plant"""
        return self._height

    def get_age(self) -> int:
        """ get the age of the plant"""
        return self._current_age

    def set_height(self, height: int):
        """
        Check if the height input is a correct value and
        then update the height of the plant
        """
        if height < 0:
            print(f"\nInvalid operation attempted: "
                  f"height {height}cm [REJECTED]")
            print("Security: Negative height rejected\n")
        elif height > 0:
            print(f"Height update: {height} [OK]")
            self._height = height
        else:
            pass

    def set_age(self, days: int):
        """
        Check if the age input is a correct value and
        then update the age of the plant
        """
        if days < 0:
            print(f"Invalid operation attempted: "
                  f"age {days} days [REJECTED]")
            print("Security: Negative days rejected\n")
        elif days > 0:
            print(f"Age update: {days} [OK]")
            self._current_age = days
        else:
            pass


def ft_garden_security():
    """Create a Plant with secure values and print the info"""
    print("=== Garden Security System ===")
    plant1 = SecurePlant("Rose", 0, 0)
    plant1.set_height(25)
    plant1.set_age(30)

    plant1.set_height(-5)

    print(f"Current plant: {plant1.name} "
          f"({plant1.get_height()}cm, {plant1.get_age()} days)")


if __name__ == "__main__":
    ft_garden_security()
