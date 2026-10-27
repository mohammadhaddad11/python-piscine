#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")


def create_plants() -> list[Plant]:
    plant_data: list[tuple[str, float, int]] = [
        ("Rose", 25.0, 30),
        ("Oak", 200.0, 365),
        ("Cactus", 5.0, 90),
        ("Sunflower", 80.0, 45),
        ("Fern", 15.0, 120),
    ]

    plants: list[Plant] = []

    for name, height, age in plant_data:
        plants += [(Plant(name, height, age))]

    return plants


if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    plants = create_plants()

    for plant in plants:
        print("Created: ", end="")
        plant.show()
