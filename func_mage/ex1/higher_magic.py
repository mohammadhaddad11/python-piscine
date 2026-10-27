from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return (combined)


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:

    def multiply(target: str, power: int) -> str:
        mul_power = power * multiplier
        return (base_spell(target, mul_power))
    return (multiply)


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def spell_checker(target, power) -> str:
        if condition(target, power):
            return (spell(target, power))
        else:
            return ("Spell fizzled")
    return (spell_checker)


def spell_sequence(spells: list[Callable]) -> Callable:
    def infinity_spells(target: str, power: int) -> list:
        res = []
        for spell in spells:
            res.append(spell(target, power))
        return (res)
    return (infinity_spells)


if __name__ == "__main__":
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target}"

    def heal(target: str, power: int) -> str:
        return f"Heals {target}"

    def power_spell(target: str, power: int) -> str:
        return str(power)

    def strong_enough(target: str, power: int) -> bool:
        return power >= 10

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    first_result, second_result = combined("Dragon", 10)
    print(f"Combined spell result: {first_result}, {second_result}")

    print("Testing power amplifier...")
    amplified = power_amplifier(power_spell, 3)
    print(f"Original: {power_spell('Dragon', 10)}, "
          f"Amplified: {amplified('Dragon', 10)}")

    print("Testing conditional caster...")
    conditional_spell = conditional_caster(strong_enough, fireball)
    print(conditional_spell("Dragon", 10))
    print(conditional_spell("Dragon", 5))

    print("Testing spell sequence...")
    sequence = spell_sequence([fireball, heal])
    print(sequence("Dragon", 10))
