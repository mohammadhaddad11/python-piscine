#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self._height: float = 0.0
        self._age: int = 0
        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> float:
        return (self._height)

    def get_age(self) -> int:
        return (self._age)

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self.name}: Error, height can’t be negative")
            print("Height update rejected")
            return
        self._height = new_height
        print(f"Height updated: {self._height}cm ")

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self.name}: Error, age can’t be negative")
            print("Age update rejected")
            return
        self._age = new_age
        print(f"Age updated: {self._age} days \n")

    def get_info(self) -> str:
        return f"{self.name}: {self._height:.1f}cm, {self._age} days old"


if __name__ == "__main__":
    print("=== Garden Security System ===")

    plant = Plant("Rose", 15, 10)
    print(f"Plant created:  {plant.get_info()}")
    print()
    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-5)
    plant.set_age(-3)
    print(f"\nCurrent state: {plant.get_info()}")
