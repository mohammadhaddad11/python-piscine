*42 curriculum exercises · mhaddad*

# Python Piscine

Eleven small projects explore how to structure Python programs, from functions
that read console input to objects with validated state, processing pipelines,
and a script that analyzes live weather data. Each project has a detailed README
explaining its exercises, main functions/classes, examples, and limitations.

This is a collection of independent learning programs, not one application or
installable framework. The larger maze project is maintained separately in
[A-Maze-ing](https://github.com/mohammadhaddad11/a-maze-ing).

## Project guide

| Project | What it builds |
| --- | --- |
| [Growing Code](Growing_Code/README.md) | Small garden utilities for area, harvest totals, care reminders, counting, and reports |
| [Code Cultivation](code_cultivation/README.md) | Plant objects that grow, validate updates, specialize behavior, and count operations |
| [Garden Guardian](Garden_Guardian/README.md) | Concrete error-handling scenarios, custom exceptions, and cleanup paths |
| [Data Quest](Data-Quest/README.md) | Score, coordinate, achievement, inventory, and event-stream reports |
| [Data Archivist](Data_Archivist/README.md) | A text-file read/transform/save workflow with explicit cleanup and stream handling |
| [The Codex](The-codex/README.md) | Import experiments showing package APIs, module resolution, and circular dependencies |
| [Code Nexus](code_Nexus/README.md) | Mixed-data processors, ordered routing, and consuming export plugins |
| [Data Deck](Data_Deck/README.md) | Creature factories and capability-dependent action strategies |
| [Func Mage](func_mage/README.md) | Function combiners, stateful closures, cached/typed dispatch, and decorators |
| [The Matrix](The_Matrix/README.md) | Environment inspection, weather analysis/charting, and dotenv configuration |
| [Cosmic Data](Cosmic_Data/README.md) | Validated station/contact records and crew-composition rules using Pydantic |

The order above is a useful reading path: simple functions lead into state and
exceptions, data structures lead into I/O and modules, and the later projects
combine these ideas through reusable interfaces and validation boundaries.

## Getting started

Use **Python 3.13+** to run the entire collection unchanged. Some projects have
lower requirements; the Data Quest generator annotations need 3.13 defaults,
Garden Guardian uses 3.12 f-string syntax, and Cosmic Data uses `typing.Self`.

```sh
git clone git@github.com:mohammadhaddad11/python-piscine.git
cd python-piscine
python3 -m venv .venv
. .venv/bin/activate
python3 code_cultivation/ex6/ft_garden_analytics.py
python3 code_Nexus/ex2/data_pipeline.py
python3 Data_Deck/tournament.py
```

Most projects use only the standard library. For Cosmic Data and The Matrix:

```sh
python3 -m pip install 'pydantic>=2' \
  -r The_Matrix/ex1/requirements.txt -r The_Matrix/ex2/requirements.txt
```

Growing Code files need their functions called explicitly. Some programs ask
for input; The Matrix needs network access for its forecast. Each project README
states the working directory and expected behavior of its commands.

## How to navigate the code

Exercise files intentionally repeat class/function names as ideas develop.
Run them independently instead of importing all `ex0` packages into one process.
The Data Deck and Codex package layouts are part of their import examples and
should stay intact.

Demonstrations were exercised on Python 3.14, including handled errors, the
intentional Codex failures, and live weather/chart output. Notable limitations
are documented where they occur: the old root-level garden analytics script
raises `NameError`, and a nonempty zero-total inventory raises
`ZeroDivisionError`. Neither is presented as a completed feature.

## Resources

- [Python documentation](https://docs.python.org/3/)
- [Python tutorial](https://docs.python.org/3/tutorial/)
- [Standard library](https://docs.python.org/3/library/)
- [Pydantic](https://docs.pydantic.dev/latest/)
- [Open-Meteo](https://open-meteo.com/en/docs)

## AI Usage

AI assisted documentation, source review, and checking representative examples.
The available Piscine files do not establish how AI was used during the
original implementation of each exercise; no broader authorship claim is made.
