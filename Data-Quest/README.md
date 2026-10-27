*42 curriculum exercises · mhaddad*

# Data Quest

Seven exercises applying lists, tuples, sets, dictionaries, comprehensions, and generators.

## Description

| Exercise | Focus |
| --- | --- |
| `ex0`–`ex1` | CLI arguments and score calculations |
| `ex2` | Coordinate tuples and Euclidean distance |
| `ex3` | Set union, intersection, and difference |
| `ex4` | Inventory dictionaries and percentages |
| `ex5`–`ex6` | Generators and comprehensions |

## Instructions

Requirements: Python 3.13+. Run from this directory:

```sh
python3 ex0/ft_command_quest.py alpha beta
python3 ex1/ft_score_analytics.py 10 20 30
python3 ex4/ft_inventory_system.py sword:2 potion:3
python3 ex5/ft_data_stream.py
```

## Technical Notes

Python **3.13+** is needed for the generator typing used by `ex5`. `ex2` prompts for coordinates; `ex3` and `ex6` use randomized sample data.

**Known issue:** `python3 ex4/ft_inventory_system.py potion:0` raises `ZeroDivisionError` because the total quantity is zero.

## Resources

- [Data structures](https://docs.python.org/3/tutorial/datastructures.html) · [Generators](https://docs.python.org/3/howto/functional.html#generators)
- [Generator syntax and behavior](https://docs.python.org/3/tutorial/classes.html#generators)
- [Typing Generator](https://docs.python.org/3/library/typing.html#typing.Generator)

## AI Usage

AI assistance supported documentation and verification during portfolio publication. See the [collection's AI usage note](../README.md#ai-usage).
