from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    counter = 0

    def inner() -> int:
        nonlocal counter
        counter += 1
        return counter
    return (inner)


def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power

    def inner(amount: int) -> int:
        nonlocal total_power
        total_power += amount
        return total_power

    return inner


def enchantment_factory(enchantment_type: str) -> Callable:

    def inner(item: str) -> str:
        enhanced_item = enchantment_type + ' ' + item
        return (enhanced_item)
    return inner


def memory_vault() -> dict[str, Callable]:
    memory: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        memory[key] = value

    def recall(key: str) -> Any:
        return (memory.get(key, "Memory not found"))

    res: dict[str, Callable] = {"store": store, "recall": recall}
    return (res)


if __name__ == "__main__":
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()

    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("Testing spell accumulator...")
    accumulator = spell_accumulator(100)

    print(f"Base 100, add 20: {accumulator(20)}")
    print(f"Base 100, add 30: {accumulator(30)}")

    print("Testing enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")

    print(flaming("Sword"))
    print(frozen("Shield"))

    print("Testing memory vault...")
    vault = memory_vault()

    print("Store 'secret' = 42")
    vault["store"]("secret", 42)

    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")
