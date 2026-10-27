import operator
from functools import reduce, partial, lru_cache, singledispatch
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    if operation == "add":
        return (reduce(operator.add, spells))
    elif operation == "multiply":
        return (reduce(operator.mul, spells))
    elif operation == "max":
        return reduce(lambda x, y: x if operator.gt(x, y) else y, spells)
    elif operation == "min":
        return reduce(lambda x, y: x if operator.lt(x, y) else y, spells)
    else:
        raise ValueError("Unknown operation")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:

    fire_enhancement = partial(base_enchantment, 50, "Fire")
    thunder_enhancement = partial(base_enchantment, 50, "Thunder")
    ice_enhancement = partial(base_enchantment, 50, "Ice")

    res: dict[str, Callable] = {"fire": fire_enhancement,
                                "thunder": thunder_enhancement,
                                "ice": ice_enhancement}

    return res


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n < 0:
        raise ValueError("index 'n' cant be negative number")
    elif n == 1:
        return 1
    else:
        return (memoized_fibonacci(n-1) + memoized_fibonacci(n-2))


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatcher(data: Any) -> str:
        return ("Unknown spell type")

    @dispatcher.register
    def int_handler(data: int) -> str:
        return (f"{data} damage")

    @dispatcher.register(str)
    def str_handler(data: str) -> str:
        return (data)

    @dispatcher.register(list)
    def _(data: list[Any]) -> str:
        return (f"{len(data)} spells")

    return dispatcher


if __name__ == "__main__":
    spells = [10, 20, 30, 40]

    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("Testing spell dispatcher...")
    dispatcher = spell_dispatcher()

    print(f"Damage spell: {dispatcher(42)}")
    print(f"Enchantment: {dispatcher('fireball')}")
    print(f"Multi-cast: {dispatcher(['fireball', 'heal', 'shield'])}")
    print(dispatcher(3.14))
