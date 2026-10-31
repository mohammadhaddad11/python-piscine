*42 curriculum exercises · mhaddad*

# Data Deck

Data Deck builds interchangeable creature families and action policies. A caller
can request a base/evolved pair from a factory, add healing or transformation
capabilities, and choose a strategy without hardcoding every concrete creature
into the driver.

Despite the name, the implementation does not model a deck of cards. It is a
small creature-based demonstration of object creation, multiple inheritance,
and behavior selection. Battles produce action descriptions, not numerical
damage or a winner.

## Instructions

Python 3.10+; standard library only. From this directory:

```sh
python3 battle.py
python3 capacitor.py
python3 tournament.py
```

Keep `ex0/`, `ex1/`, and `ex2/` with their `__init__.py` files: the root drivers
import these packages directly. The exercise files define components; the
three root scripts provide the demonstrations.

## ex0 — Create related objects through a factory

[`Creature`](ex0/creature.py) defines the shared state (`name`, `creature_type`),
a concrete `describe()` method, and an abstract `attack()`. Four concrete
creatures return their own attack strings: Charmander/Charizard and
Squirtle/Blastoise.

[`CreatureFactory`](ex0/factories.py) requires `create_base()` and
`create_evolved()`. `FlameFactory` supplies the first pair; `AquaFactory` supplies
the second. “Evolved” means creating another concrete object, not mutating an
existing creature into a new class.

[`battle.py`](battle.py) accepts these factories through their common interface.
`tester(factory)` prints both objects and attacks; `battle(f1, f2)` creates base
creatures and prints their encounter. The driver can switch families without
changing the creation logic inside those functions.

## ex1 — Add capabilities without requiring them everywhere

[`HealCapability` and `TransformCapability`](ex1/capabilities.py) describe two
additional interfaces. [`Oddish` and `Bellossom`](ex1/creatures.py) inherit
from `Creature` and the healing capability. Their `heal()` methods return
descriptions; no health total is stored or changed.

`Zorua` and `Zoroark` combine `Creature` with transformation. Their constructors
explicitly initialize `TransformCapability` to create `is_transformed`.
`transform()` and `revert()` toggle that flag, and `attack()` branches on it.
This creates an observable state transition rather than merely changing the
printed creature name.

The [new factories](ex1/factories.py) construct these families:
`HealingCreatureFactory` returns Oddish/Bellossom, and
`TransformCreatureFactory` returns Zorua/Zoroark.
[`capacitor.py`](capacitor.py) exercises both capabilities. Its Zorua sequence
includes:

```text
Zorua strikes from the shadows with Feint Attack!
Zorua slips into an illusion form!
Zorua strikes harder using its Night Daze!
Zorua drops the illusion!
```

The capability split avoids pretending that every creature can heal or
transform, while still letting each be used through `Creature` for description
and basic attacks.

## ex2 — Choose an action policy separately from construction

[`BattleStrategy`](ex2/strategies.py) requires `is_valid(entity)` and
`act(entity)`, with actions returned as a list of strings:

- `NormalStrategy` accepts a creature and performs its attack.
- `DefensiveStrategy` requires `HealCapability`, then returns attack and heal.
- `AggressiveStrategy` requires `TransformCapability`, then transforms,
  attacks in that state, and reverts.

Runtime `isinstance` checks enforce capability compatibility before the
capability-specific calls. `typing.cast` then describes that narrowed interface
to static tools; it does not perform the runtime validation itself. Unsupported
combinations raise `InvalidStrategyError`.

[`tournament.py`](tournament.py) connects factories and strategies as
`(factory, strategy)` pairs. `battle(opponents)` visits every unordered pair,
creates fresh base creatures for that encounter, and prints each strategy's
actions. Three opponents therefore create three pairings, not a bracket with
winners progressing to a final.

The script runs a basic encounter, an invalid aggressive Charmander encounter,
and a three-opponent demonstration. An invalid pairing prints a battle error
and returns from that tournament call; the outer demo can still start its next
tournament.

## Why the separation matters

Factories answer **which objects belong together**; strategies answer **what
to do with an object**. Capabilities make the conditions for those actions
explicit. Combining the three lets the driver express a new matchup by changing
its inputs instead of adding a creature-specific branch to every battle.

All three drivers were executed successfully, including the handled invalid
strategy. The project has no HP accounting, score calculation, persisted state,
or winner selection. In the aggressive strategy, reversion is a normal final
step, not protected by `finally` against an unexpected attack exception.

## Resources

- [Abstract base classes](https://docs.python.org/3/library/abc.html)
- [Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [Strategy pattern](https://en.wikipedia.org/wiki/Strategy_pattern)

## AI Usage

AI assisted this documentation and demonstration checks. Original implementation
AI use is not established; see the [collection disclosure](../README.md#ai-usage).
