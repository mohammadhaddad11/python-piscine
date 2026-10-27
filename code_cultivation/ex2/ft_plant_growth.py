#!/usr/bin/env python3


class Plant():
    name: str
    height: float
    age: int
    initial_height: float
    daily_growth: float

    def grow(self) -> None:
        self.height += self.daily_growth

    def age_grow(self) -> None:
        self.age += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    rose = Plant()

    rose.name = "Rose"
    rose.height = 25.0
    rose.initial_height = 25.0
    rose.age = 30
    rose.daily_growth = 0.8

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.show()
        if day < 7:
            rose.grow()
            rose.age_grow()
    print(f"Growth this week: {rose.height - rose.initial_height:.1f}cm")
