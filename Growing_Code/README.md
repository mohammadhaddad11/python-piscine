*42 curriculum exercises. Portfolio maintainer: mhaddad.*

# Growing Code

## Description

Introductory functions practice formatted output, console input, integer
conversion, arithmetic, branching, loops, recursion, and parameterized behavior.
Garden examples keep the programs small enough to inspect step by step.

## Instructions

Python 3.10+; standard library only. These modules **define functions but do not
call them**. Executing a file directly generally produces no output. Import or
load the module, then call its function:

```sh
python3 -c 'import runpy; runpy.run_path("ex0/ft_hello_garden.py")["ft_hello_garden"]()'
python3 -c 'import runpy; runpy.run_path("ex1/ft_plot_area.py")["ft_plot_area"]()'
python3 -c 'import runpy; runpy.run_path("ex7/ft_seed_inventory.py")["ft_seed_inventory"]("tomato", 5, "packets")'
```

Run from this directory. Follow the input prompts for functions that read stdin.

| Exercise | Function/input |
| --- | --- |
| ex0 | `ft_hello_garden()`; no input |
| ex1 | `ft_plot_area()`; two integer dimensions |
| ex2 | `ft_harvest_total()`; three integer harvest amounts |
| ex3 | `ft_plant_age()`; plant age |
| ex4 | `ft_water_reminder()`; elapsed days |
| ex5 | Iterative and recursive harvest-count functions; target count |
| ex6 | `ft_garden_summary()`; garden name, then plant count |
| ex7 | `ft_seed_inventory(seed_type, quantity, unit)` |

## Algorithms and Design Decisions

The loop and recursive versions illustrate two control-flow forms of counting.
Recursion consumes a call frame per step and remains subject to Python's
recursion limit. Functions print their results rather than forming a reusable
data-processing API. Input conversion is direct; invalid numeric text is not
uniformly caught by these introductory exercises.

## Verification

All nine files passed syntax checks. Every function was invoked on Python
3.14.8 with representative input, including both counting implementations and
the parameterized seed report. Exhaustive invalid-input handling is not claimed.

## Resources

- [Control flow and functions](https://docs.python.org/3/tutorial/controlflow.html).
- [Input/output](https://docs.python.org/3/tutorial/inputoutput.html).

## AI Usage

AI assisted documentation and scripted function-call verification for this
publication. Original implementation AI use is not established; see the
[collection disclosure](../README.md#ai-usage).
