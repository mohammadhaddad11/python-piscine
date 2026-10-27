*42 curriculum exercises. Portfolio maintainer: mhaddad.*

# Garden Guardian

## Description

Five garden-themed demonstrations explain exception propagation, deliberate
raising, custom exception hierarchies, and guaranteed cleanup. The purpose is
to distinguish invalid input from normal flow and keep cleanup explicit.

## Instructions

Use Python **3.12+**: ex0 uses modern f-string expression syntax. No external
dependencies are needed.

```sh
python3 ex0/ft_first_exception.py
python3 ex1/ft_raise_exception.py
python3 ex2/ft_different_errors.py
python3 ex3/ft_custom_errors.py
python3 ex4/ft_finally_block.py
```

## Technical Implementation

- **ex0:** conversion errors and `try`/`except` handling.
- **ex1:** explicitly raised temperature-range errors.
- **ex2:** value, division, missing-file, and type errors.
- **ex3:** `GardenError`, `PlantError`, and `WaterError` hierarchy.
- **ex4:** `finally` behavior through exceptional and early-return paths.

Each file is an independent exercise, so similarly named exception classes
need not be the same runtime class across modules. The examples emphasize
control flow rather than persistent garden management.

## Design Decisions and Verification

Errors printed by these demonstrations are expected learning outcomes. They
are not evidence of an installation failure. All five scripts passed syntax
and demonstration checks on Python 3.14.8. The existing remote `WaterError`
definition in ex4 was retained: its local omission introduced no functional
improvement and would unnecessarily remove a public class.

## Resources

- [Errors and exceptions](https://docs.python.org/3/tutorial/errors.html).
- [Exception hierarchy](https://docs.python.org/3/library/exceptions.html).

## AI Usage

AI assisted the source comparison, README, and smoke checks for publication.
Historical implementation assistance is not established; see the
[collection disclosure](../README.md#ai-usage).
