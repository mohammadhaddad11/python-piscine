*42 curriculum exercises. Portfolio maintainer: mhaddad.*

# Data Quest

## Description

Seven game-themed exercises practice choosing Python data structures: lists
for scores, tuples for positions, sets for achievements, dictionaries for
inventory, generators for events, and comprehensions for transformations.

## Instructions

Use Python **3.13+** for the complete project as written: ex5 uses single-argument
`typing.Generator` annotations with default type parameters. Standard library
only. From this directory:

```sh
python3 ex0/ft_command_quest.py alpha beta
python3 ex1/ft_score_analytics.py 10 20 30
python3 ex2/ft_coordinate_system.py
python3 ex4/ft_inventory_system.py sword:2 potion:3
python3 ex5/ft_data_stream.py
```

Ex2 asks twice for three comma-separated coordinates; try `0,0,0`, then `3,4,0`.
Ex3 (`ft_achievement_tracker.py`) and ex6 (`ft_data_alchemist.py`) run without
arguments and use randomized sample data.

## Algorithms and Data Structures

| Exercise | Concepts |
| --- | --- |
| ex0 | `sys.argv`, counting and displaying arguments |
| ex1 | Integer conversion, invalid-score handling, aggregation |
| ex2 | Tuple unpacking and Euclidean distance |
| ex3 | Set union, intersection and difference |
| ex4 | Parsing `item:quantity`, dictionary totals and percentages |
| ex5 | Infinite event production and destructive list-consumption generators |
| ex6 | List/dictionary comprehensions and above-average score filtering |

## Design Decisions and Limits

The exercises emphasize direct operations over shared abstractions. Random
output is not reproducible without externally controlling the random seed.
The ex3 helper relies on state initialized in its main block, so it is primarily
a script demonstration rather than a self-contained reusable API.

**Known issue:** `python3 ex4/ft_inventory_system.py potion:0` raises
`ZeroDivisionError`; total quantity is not guarded before computing percentages.
The supplied implementation is preserved, not silently patched.

## Verification

All seven modules passed syntax checks and normal demonstrations on Python
3.14.8. Scripted coordinates included an invalid entry followed by valid values;
score parsing included invalid text. The event-stream demo completed. The
zero-total inventory failure was separately reproduced and remains documented.

## Resources

- [Python data structures](https://docs.python.org/3/tutorial/datastructures.html).
- [Generators](https://docs.python.org/3/tutorial/classes.html#generators).
- [Typing Generator](https://docs.python.org/3/library/typing.html#typing.Generator).

## AI Usage

AI assisted version comparison, documentation, and smoke/edge-case checks during
publication. Historical implementation assistance is not established; see the
[collection disclosure](../README.md#ai-usage).
