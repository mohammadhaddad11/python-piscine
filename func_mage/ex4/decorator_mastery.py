from functools import wraps
from collections.abc import Callable
from time import time, sleep
from typing import Any


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time()
        print(f"Casting {func.__name__}...")
        res = func(*args, **kwargs)
        end_time = time()
        print(f"spell completed in {end_time - start_time:.3f} seconds")
        return (res)
    return wrapper


def power_validator(min_power: int) -> Callable:
    def factory(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(power: int, *args: Any, **kwargs: Any) -> Any:
            if power >= min_power:
                return (func(power, *args, **kwargs))
            else:
                return "Insufficient power for this spell"
        return wrapper
    return factory


def retry_spell(max_attempts: int) -> Callable:
    def factory(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            for attempt in range(1, max_attempts+1):
                try:
                    return (func(*args, **kwargs))
                except Exception:
                    if (attempt != max_attempts):
                        print("Spell failed, retrying..."
                              f" (attempt {attempt}/{max_attempts})")

            return (f"Spell casting failed after {max_attempts} attempts")
        return wrapper
    return factory


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        for i in (name):
            if not (i.isalpha() or i.isspace()):
                return False
        if len(name) >= 3:
            return True
        return False

    def cast_spell(self, spell_name: str, power: int) -> str:
        @power_validator(10)
        def _helper(power: int, spell_name: str) -> str:
            return f"Successfully cast {spell_name} with {power} power"
        return _helper(power, spell_name)


if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        sleep(0.1)
        return "Fireball cast!"

    print(f"Result: {fireball()}")

    print("Testing retrying spell...")

    @retry_spell(3)
    def failing_spell() -> str:
        raise RuntimeError("Spell failed")

    print(failing_spell())

    @retry_spell(3)
    def working_spell() -> str:
        return "Waaaaaaagh spelled !"

    print(working_spell())

    print("Testing MageGuild...")
    guild = MageGuild()

    print(MageGuild.validate_mage_name("Merlin"))
    print(MageGuild.validate_mage_name("Al1"))

    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))
