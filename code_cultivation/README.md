*42 curriculum exercises. Portfolio maintainer: mhaddad.*

# code_cultivation

## Description

Seven garden-themed exercises introduce object state, constructors, validation,
inheritance, polymorphism, and class-level utilities. The current implementation
progresses from a printed plant record to nested per-instance statistics.

## Instructions

Python 3.10+ and the standard library are sufficient. From this directory:

```sh
python3 ex0/ft_garden_intro.py
python3 ex4/ft_garden_security.py
python3 ex6/ft_garden_analytics.py
```

| Exercise | Implementation |
| --- | --- |
| ex0 | A printed plant name, height, and age |
| ex1 | An annotated `Plant` class; attributes are initialized explicitly in the demo |
| ex2 | Daily growth/aging with a seven-day report |
| ex3 | Constructor-based plant creation from tuples |
| ex4 | Setter validation rejecting negative height and age |
| ex5 | `Flower`, `Tree`, and `Vegetable` subclasses with different behavior |
| ex6 | Nested `_Stats`, `Seed` inheritance, static validation and an anonymous-plant classmethod |

## Technical Implementation and Design Decisions

Early examples deliberately avoid a constructor so attribute assignment is
visible. Later exercises centralize initialization and route changes through
setters. A leading underscore marks internal state by convention; it is not
access-control enforcement. Inheritance reuses plant initialization while
subclasses add bloom state, shade reporting, or nutritional-value updates.

In ex6, each plant owns its own nested statistics object. Growth, aging, and
display calls increment counters; tree shade calls have a separate counter.
`display_statistics` accepts a plant and dispatches through its methods.
The nutrition/shade calculations are learning examples, not biological models.

## Verification and Preserved Remote File

All seven current local exercises passed syntax and standalone demonstration
checks on Python 3.14.8. The older root-level
[`ft_garden_analytics.py`](ft_garden_analytics.py) is retained from remote history
because it has no matching local path. Its demo fails with `NameError` for
undefined `Flower`; it is not the current ex6 implementation. No source was
rewritten to repair it.

## Resources

- [Python classes](https://docs.python.org/3/tutorial/classes.html).
- [Built-in classmethod and staticmethod](https://docs.python.org/3/library/functions.html).

## AI Usage

AI assisted the publication comparison, documentation, and smoke checks. The
original implementation's AI usage is not established by the available files;
see the [collection disclosure](../README.md#ai-usage).
