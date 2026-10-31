*42 curriculum exercises · mhaddad*

# Code Cultivation

Code Cultivation gradually builds a model of plants that can grow, age, reject
invalid updates, specialize their behavior, and report how often operations
were performed. Its seven exercises show why classes become useful when data
and the operations on that data need to stay together.

The exercises are separate programs, not successive modules of one package.
Each introduces a different `Plant` definition, so use the class belonging to
the exercise being studied.

## Instructions

Python 3.10+ and the standard library are sufficient. From this directory:

```sh
python3 ex1/ft_garden_data.py
python3 ex2/ft_plant_growth.py
python3 ex4/ft_garden_security.py
python3 ex6/ft_garden_analytics.py
```

Every `ex0`–`ex6` script includes a runnable demonstration and needs no input.

## ex0 — Describing a single plant

[`ft_garden_intro.py`](ex0/ft_garden_intro.py) stores a rose's name, height, and
age as ordinary variables and prints a small record. There is no class yet.
This establishes the information the later objects will keep together.

## ex1 — Giving each plant its own state

[`Plant` in ft_garden_data.py](ex1/ft_garden_data.py) groups `name`, `height`, and
`age`, with `show()` responsible for displaying them. The driver creates three
instances, assigns each attribute explicitly, and calls the same method on all
three. Their values remain independent:

```text
Rose: 25cm, 30 days old
Sunflower: 80cm, 45 days old
Cactus: 15cm, 120 days old
```

There is intentionally no constructor here. The annotations do not create or
initialize attributes; a caller must assign them before calling `show()`.

## ex2 — Behavior that changes an object

[`ft_plant_growth.py`](ex2/ft_plant_growth.py) adds `grow()` and `age_grow()`.
Growth adds the object's `daily_growth`; aging increments its age by one.
The demo begins at 25.0 cm and 30 days, prints days 1–7, and performs six
updates between those observations. Day 7 is therefore 29.8 cm and 36 days,
with `Growth this week: 4.8cm` reported at the end.

`initial_height` is retained separately so the final change can be calculated.
Methods update the object's existing state rather than construct a new plant
for each day.

## ex3 — Centralizing initialization in a constructor

[`create_plants()`](ex3/ft_plant_factory.py) iterates over five `(name, height,
age)` tuples and creates a `Plant` from each. `__init__` replaces the repeated
attribute assignments used earlier, ensuring each constructed object begins
with all three attributes. `show()` formats height to one decimal place.

The function returns a list of objects; the driver controls printing. This is
a concrete data-to-object factory function, not a configurable factory framework.

## ex4 — Defining acceptable updates

[`ft_garden_security.py`](ex4/ft_garden_security.py) initializes `_height` and
`_age` to zero, then calls their setters. Getters expose those values and
`get_info()` returns a formatted summary.

Negative updates print an error and leave the previous value intact. In the
demo, setting height 25 and age 30 succeeds; attempts to set `-5` and `-3` do
not undo those valid values. The final summary is:

```text
Current state: Rose: 25.0cm, 30 days old
```

A leading underscore signals an internal attribute by convention; it does not
prevent direct access. Rejection is communicated through messages rather than
exceptions or a boolean return value.

## ex5 — Specializing a shared plant interface

[`ft_plant_types.py`](ex5/ft_plant_types.py) makes `Plant` the reusable base for
validated state, `grow(amount)`, `age(days)`, and `show()`.

- `Flower` adds color and `has_bloomed`. `bloom()` changes the flag; its overridden
  `show()` calls the base display, then reports color and bloom state.
- `Tree` adds trunk diameter. `produce_shade()` prints a description using its
  height and diameter; it does not simulate light or compute a physical area.
- `Vegetable` adds a harvest season and nutritional value. Its growth and aging
  overrides call the base operation and add 10 nutrition points per call.

In the demo, growing a tomato by 42 and aging it by 20 changes it from 5.0 cm,
10 days, nutrition 0 to 47.0 cm, 30 days, nutrition 20. The increments are per
operation, not proportional to days or centimeters. An inherited rejection
does not stop the vegetable override from adding nutrition, a limitation of
the simple return-with-message interface.

## ex6 — Observing operations through composition

[`ft_garden_analytics.py`](ex6/ft_garden_analytics.py) gives each plant a nested
`Plant._Stats` object. It counts calls to growth, aging, and display; it does
not infer changes by comparing heights. Even a rejected update can count as
an attempted operation because the counter is incremented before validation.

`show_stats()` delegates to that helper. `Tree` extends reporting with a shade
counter, while `display_statistics(plant)` works through the shared method
interface instead of branching on every subclass.

This exercise also adds:

- `Seed`, a `Flower` subclass whose `bloom()` calls the inherited method and sets
  `seeds` to 42.
- `age_checker`, a static method testing whether a supplied age is greater
  than 365, without needing an instance.
- `anonymous`, a classmethod using `cls` to construct an unnamed base plant.
  Subclasses with additional required constructor arguments cannot necessarily
  use it unchanged.

For the rose, one display initially reports `Stats: 0 grow, 0 age, 1 show`.
After growing and displaying again it reports `Stats: 1 grow, 0 age, 2 show`.
Each instance owns its statistics; the counters are not shared globally.

## Scope and limitations

The current seven exercises passed their standalone demonstrations. The older
root-level [`ft_garden_analytics.py`](ft_garden_analytics.py) is a separate,
incomplete variant: its driver refers to undefined `Flower` and fails with
`NameError`. Use `ex6/ft_garden_analytics.py` for the functioning analytics demo.

The progression demonstrates constructors, instance ownership, inheritance,
method overriding, and composition. It does not provide persistence, a garden
database, or realistic biological growth/nutrition models.

## Resources

- [Python classes](https://docs.python.org/3/tutorial/classes.html)
- [classmethod and staticmethod](https://docs.python.org/3/library/functions.html)

## AI Usage

AI assisted documentation and checking the examples. Original implementation
AI usage is not established; see the [collection disclosure](../README.md#ai-usage).
