*42 curriculum exercises · mhaddad*

# Growing Code

Short exercises introducing Python functions, console input, arithmetic, branches, loops, and recursion.

## Description

| Exercise | Focus |
| --- | --- |
| `ex0`–`ex1` | Output and area calculation |
| `ex2`–`ex4` | Arithmetic, branching, and reminders |
| `ex5` | Iterative and recursive counting |
| `ex6`–`ex7` | Input-based summary and parameterized inventory report |

## Instructions

Requirements: Python 3.10+ (standard library only). Run from this directory:

```sh
python3 -c 'import runpy; runpy.run_path("ex0/ft_hello_garden.py")["ft_hello_garden"]()'
python3 -c 'import runpy; runpy.run_path("ex7/ft_seed_inventory.py")["ft_seed_inventory"]("tomato", 5, "packets")'
```

## Technical Notes

These modules **define functions without calling them**, so running their files directly produces no demonstration output. Import or load the desired module and invoke its function, supplying interactive input where needed.

Recursive counting consumes a stack frame per step and remains bounded by Python's recursion limit.

## Resources

- [Control flow](https://docs.python.org/3/tutorial/controlflow.html) · [Input and output](https://docs.python.org/3/tutorial/inputoutput.html)

## AI Usage

AI assistance supported documentation and verification during portfolio publication. See the [collection's AI usage note](../README.md#ai-usage).
