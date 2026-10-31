*42 curriculum exercises · mhaddad*

# Garden Guardian

Garden Guardian builds a series of small failure-handling demonstrations:
parse a temperature, reject an unsuitable value, distinguish several exception
types, define domain-specific errors, and close a watering system even when a
call fails. The progression is about controlling what happens after an error,
not simply printing a list of Python exception names.

## Instructions

Use Python **3.12+** because ex0 uses newer f-string expression syntax. There are
no external dependencies. From this directory:

```sh
python3 ex0/ft_first_exception.py
python3 ex1/ft_raise_exception.py
python3 ex2/ft_different_errors.py
python3 ex3/ft_custom_errors.py
python3 ex4/ft_finally_block.py
```

These scripts deliberately trigger errors and normally catch them. An error
message inside their output is often the expected result.

## ex0 — Recovering from failed conversion

[`input_temperature` and `test_temperature`](ex0/ft_first_exception.py) first
convert `"25"` successfully, then attempt `int("abc")`. A surrounding `try`
catches the conversion exception and the final completion message still runs.

The conversion helper does not catch its own error: responsibility is left to
the calling demonstration. Both calls share one `try` block, so an exception
skips any remaining statements in that block before reaching the handler.

## ex1 — Adding a rule beyond type conversion

[`ft_raise_exception.py`](ex1/ft_raise_exception.py) keeps the conversion but
adds a permitted range of **0 through 40°C, inclusive**. Values above 40 and
below zero explicitly raise `ValueError` with a garden-specific explanation.
`"abc"` instead fails in the integer conversion itself.

The driver tries `25`, `abc`, `100`, and `-50` separately. Each iteration has
its own handler, so one bad reading does not prevent later readings from being
processed. Input `100` reports `100°C is too hot for plants (max 40°C)` rather
than accepting it merely because it is a valid integer.

## ex2 — Choosing a handler by error type

[`garden_operations(operation_number)`](ex2/ft_different_errors.py) triggers
four concrete failures: converting `"hi"`, dividing by zero, opening a missing
path, and adding a string to an integer. `test_error_types` handles value and
division errors separately, then groups missing-file and type errors in one
handler that prints the runtime exception name.

Operation 4 falls through without performing a failing action. Comparing it
with operations 0–3 makes the normal and exceptional control paths visible.
This demonstrates typed handlers; it is not an implementation of file recovery
or automatic retry.

## ex3 — Errors belonging to the application domain

[`GardenError`, `PlantError`, and `WaterError`](ex3/ft_custom_errors.py) form a
small exception hierarchy. `plant_health()` raises a wilting-plant error;
`water_level()` raises a low-water error. Each subclass forwards its message to
the base exception.

The driver first catches the exact subclasses, then catches both through
`GardenError`. This lets callers choose between specific recovery and a common
policy for all garden failures, without catching unrelated exceptions.

## ex4 — Cleanup across an exception and an early return

[`water_plant` and `test_watering_system`](ex4/ft_finally_block.py) model opening
and closing a watering system through printed messages. A name is accepted
when it equals its `.capitalize()` form: `Tomato` passes; `lettuce` raises
`PlantError`. This is a capitalization rule, not a botanical name validator.

For the invalid sequence, `Tomato` is watered, `lettuce` fails, and `carrots`
is never reached. The handler prints a message and returns early, but `finally`
still prints `Closing watering system` before control leaves the function:

```text
Watering Tomato: [OK]
Caught PlantError: Invalid plant name to water: 'lettuce'
ending tests and returning to main
Closing watering system
Cleanup always happens, even with errors!
```

This output is an excerpt from the script's invalid-input scenario. No real
valves or files are opened; the exercise isolates the control-flow guarantee.

## Design observations

The files are independent, so identically named exception classes in ex3 and
ex4 are different classes. Ex0/ex1 catch broad `Exception` values, while later
examples demonstrate narrower handlers. All five demos were run successfully;
their output shows expected error handling, not comprehensive input validation
for a production service.

## Resources

- [Errors and exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Built-in exceptions](https://docs.python.org/3/library/exceptions.html)

## AI Usage

AI assisted the README and checking demonstration output. Historical
implementation assistance is not established; see the
[collection disclosure](../README.md#ai-usage).
