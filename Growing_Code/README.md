*42 curriculum exercises · mhaddad*

# Growing Code

Growing Code is a set of small garden utilities: calculate a plot's area,
combine harvest totals, make simple care decisions, count toward harvest, and
print a summary or seed inventory. It introduces one control-flow idea at a
time before combining input, calculations, and formatted output.

These are functions rather than standalone applications: the modules define
their functions but do not invoke them automatically.

## Running a function

Use Python 3.10+ with no external dependencies. From this directory, load a
module and call its function:

```sh
python3 -c 'import runpy; runpy.run_path("ex0/ft_hello_garden.py")["ft_hello_garden"]()'
python3 -c 'import runpy; runpy.run_path("ex1/ft_plot_area.py")["ft_plot_area"]()'
```

The first prints `Hello, Garden Community!`. The second asks for two dimensions;
entering `3` and `4` produces `Plot area: 12`. Executing the `.py` file alone
does not call the function and therefore produces no demonstration output.

## ex0 — A named greeting

[`ft_hello_garden()`](ex0/ft_hello_garden.py) prints one fixed welcome message.
The useful step is separating a reusable action from top-level execution: a
caller decides when the greeting happens. It has no input and returns `None`.

## ex1 — Plot area from console input

[`ft_plot_area()`](ex1/ft_plot_area.py) reads length and width, converts both
strings to integers, multiplies them, and prints the result. The local `area`
variable makes the calculation distinct from input and display. Dimensions
are not checked for positivity, and invalid numeric text raises `ValueError`.

## ex2 — Combining several measurements

[`ft_harvest_total()`](ex2/ft_harvest_total.py) reads three daily harvest amounts
and prints their sum. Input `2`, `3`, `4` gives `Total harvest: 9`. Each day has
a separate local variable; this exercise uses direct addition rather than a
collection or a general aggregation loop.

## ex3 — Choosing a message from plant age

[`ft_plant_age()`](ex3/ft_plant_age.py) branches on a strict comparison:
an age **greater than 60** prints `Plant is ready to harvest!`; 60 or less prints
`Plant needs more time to grow.` The boundary matters: this implementation does
not classify a plant aged exactly 60 days as ready.

## ex4 — A watering reminder

[`ft_water_reminder()`](ex4/ft_water_reminder.py) asks for days since watering.
More than two days prints `Water the plants!`; otherwise it prints
`Plants are fine`. This is another direct decision rule, not a scheduler or a
stored watering history.

## ex5 — Counting with iteration and recursion

The [iterative version](ex5/ft_count_harvest_iterative.py) loops over
`range(1, days + 1)`. The [recursive version](ex5/ft_count_harvest_recursive.py)
defines a local `helper` that calls itself with one less day, then prints while
the calls unwind. That ordering makes both print ascending days for positive
input:

```sh
python3 -c 'import runpy; runpy.run_path("ex5/ft_count_harvest_recursive.py")["ft_count_harvest_recursive"]()'
```

After entering `3`, the report is:

```text
Day 1
Day 2
Day 3
Harvest time!
```

Both perform one print per positive day, but recursion also uses a call frame
per level. Large counts can hit the recursion limit. Nonpositive input exposes
a difference: the loop prints no day lines, whereas the helper still prints
the supplied day once. There is no validation making those cases equivalent.

## ex6 — A readable garden summary

[`ft_garden_summary()`](ex6/ft_garden_summary.py) reads a garden name and integer
plant count and produces a small report. With `Rooftop` and `5`:

```text
Garden: Rooftop
Plants: 5
Status: Growing well!
```

The status is fixed text, not an assessment calculated from plant data. This
exercise brings string input, integer input, and formatted display together.

## ex7 — Parameters instead of interactive prompts

[`ft_seed_inventory(seed_type, quantity, unit)`](ex7/ft_seed_inventory.py) receives
its data from a caller. It capitalizes the seed name and chooses wording for
`packets`, `grams`, or `area`; another unit prints `Unknown unit type`.

```sh
python3 -c 'import runpy; runpy.run_path("ex7/ft_seed_inventory.py")["ft_seed_inventory"]("tomato", 5, "packets")'
```

```text
Tomato seeds: 5 packets available
```

This separates the reporting operation from the way input is obtained, making
it usable from a larger program without emulating stdin.

## Design and limitations

All functions report through stdout and return `None`; callers do not receive
calculated result objects. Type annotations describe the intended values but
do not validate console input. Representative calls to all nine functions were
checked on Python 3.14. The exercises demonstrate function boundaries,
conversion, branching, and two ways of expressing repeated work, rather than a
complete garden-management system.

## Resources

- [Control flow and functions](https://docs.python.org/3/tutorial/controlflow.html)
- [Input and output](https://docs.python.org/3/tutorial/inputoutput.html)

## AI Usage

AI assisted documentation and example checks. The available files do not
establish original implementation AI use; see the
[collection disclosure](../README.md#ai-usage).
