*42 curriculum exercises · mhaddad*

# Data Deck

Creature-themed examples of abstract factories, multiple inheritance, capabilities, and interchangeable strategies.

## Description

| Exercise | Focus |
| --- | --- |
| `ex0` | Abstract creature and factory interfaces |
| `ex1` | Healing and transformation capabilities |
| `ex2` | Normal, defensive, and aggressive strategies |

## Instructions

Requirements: Python 3.10+ (standard library only). Run from this directory:

```sh
python3 battle.py
python3 capacitor.py
python3 tournament.py
```

## Technical Notes

Factories isolate object creation, while strategies determine how an existing creature acts. Unsupported combinations raise `InvalidStrategyError`.

Actions are demonstrated through printed output; this is not a complete battle engine with health, scoring, or persistent game state. Keep the existing package directories and `__init__.py` files for imports.

## Resources

- [Abstract base classes](https://docs.python.org/3/library/abc.html) · [Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [Strategy pattern](https://en.wikipedia.org/wiki/Strategy_pattern)

## AI Usage

AI assistance supported documentation and verification during portfolio publication. See the [collection's AI usage note](../README.md#ai-usage).
