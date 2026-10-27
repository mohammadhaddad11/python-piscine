*42 curriculum exercises. Portfolio maintainer: mhaddad.*

# Data Deck

## Description

Creature-based design-pattern exercises covering abstract factories,
capability interfaces, multiple inheritance, and interchangeable battle
strategies. Despite the project name, the implementation is not a card-deck
engine: it demonstrates object collaboration through printed actions.

## Instructions

Python 3.10+; standard library only. Execute the drivers from this directory:

```sh
python3 battle.py
python3 capacitor.py
python3 tournament.py
```

Preserve `ex0/`, `ex1/`, and `ex2/` and their `__init__.py` files. Root drivers
import those packages directly.

## Technical Implementation

- **ex0:** abstract creature/factory interfaces and fire/water creature families.
- **ex1:** healing and transformation capabilities, richer creatures, and matching
  factories. Multiple inheritance combines creature and capability interfaces.
- **ex2:** normal, defensive, and aggressive strategies. Strategies check required
  capabilities and raise `InvalidStrategyError` for unsupported choices.
- **Drivers:** construct objects, switch behavior, and demonstrate invalid
  strategy handling.

## Design Decisions

Factories hide the concrete creation choice; strategies separate battle
behavior from creature construction. Capability checks make incompatible
combinations visible rather than assuming every creature can heal or transform.
Actions print messages; there is no implemented HP system, scoring table,
winner calculation, or persistent tournament engine.

## Verification

All twelve source files are retained unchanged from matching local/remote
implementations. Syntax checks and all three root demonstrations passed on
Python 3.14.8, including the handled invalid-strategy scenario.

## Resources

- [Python abstract base classes](https://docs.python.org/3/library/abc.html).
- [Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance).
- [Strategy pattern](https://en.wikipedia.org/wiki/Strategy_pattern).

## AI Usage

AI assisted source comparison, README writing, and demonstration checks for this
publication. Original AI assistance is not established; see the
[collection disclosure](../README.md#ai-usage).
