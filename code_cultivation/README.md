*42 curriculum exercises · mhaddad*

# Code Cultivation

Seven garden-themed exercises introducing object state, constructors, encapsulation, inheritance, and class utilities.

## Description

| Exercise | Focus |
| --- | --- |
| `ex0`–`ex2` | Plant records, state changes, and growth reports |
| `ex3`–`ex4` | Constructors and validated setters |
| `ex5` | `Flower`, `Tree`, and `Vegetable` subclasses |
| `ex6` | Nested statistics, inherited behavior, static and class methods |

## Instructions

Requirements: Python 3.10+ (standard library only). Run from this directory:

```sh
python3 ex0/ft_garden_intro.py
python3 ex4/ft_garden_security.py
python3 ex6/ft_garden_analytics.py
```

## Technical Notes

The examples start with explicit attribute assignment, then move toward constructors and setter validation. The leading `_` convention indicates internal state; it does not enforce access control. Each plant in `ex6` keeps its own statistics object.

**Known issue:** an older root-level `ft_garden_analytics.py` remains in the repository and raises `NameError` because `Flower` is undefined there. The current exercise is `ex6/ft_garden_analytics.py`.

## Resources

- [Classes](https://docs.python.org/3/tutorial/classes.html) · [Built-in class methods](https://docs.python.org/3/library/functions.html)

## AI Usage

AI assistance supported documentation and verification during portfolio publication. See the [collection's AI usage note](../README.md#ai-usage).
