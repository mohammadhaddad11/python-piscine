*Exercises from the 42 curriculum. Portfolio maintainer: mhaddad.*

# Python Piscine

## Description

A collection of eleven small Python projects covering procedural programming,
object-oriented design, error handling, collections, file I/O, imports,
functional programming, dependency management, and validation. Each project
keeps its own exercises and README; these are learning programs rather than a
single application or installable package.

This repository continues the history of `mohammadhaddad11/python`, renamed to
`python-piscine`. Established directory spellings are retained to preserve paths.

## Project Index

| Project | Topics |
| --- | --- |
| [Growing Code](Growing_Code/README.md) | Functions, input, branching, loops, recursion, parameters |
| [code_cultivation](code_cultivation/README.md) | Plant classes, construction, encapsulation, inheritance, nested statistics |
| [Garden Guardian](Garden_Guardian/README.md) | Exceptions, custom errors, cleanup with `finally` |
| [Data Quest](Data-Quest/README.md) | CLI arguments, lists, tuples, sets, dictionaries, generators, comprehensions |
| [Data-Archivist](Data_Archivist/README.md) | Text files, transformations, standard streams, context managers |
| [The Codex](The-codex/README.md) | Namespaces, packages, exports, relative imports, circular dependencies |
| [Code Nexus](code_Nexus/README.md) | Abstract processors, polymorphic routing, pipeline/export protocols |
| [Data Deck](Data_Deck/README.md) | Abstract factories, multiple inheritance, capability interfaces, strategies |
| [func_mage](func_mage/README.md) | Higher-order functions, closures, decorators, `functools` |
| [The Matrix](The_Matrix/README.md) | Environments, dependencies, weather analysis, dotenv configuration |
| [Cosmic Data](Cosmic_Data/README.md) | Pydantic v2 models, field constraints, nested and cross-field validation |

A-Maze-ing is maintained independently at
[mohammadhaddad11/a-maze-ing](https://github.com/mohammadhaddad11/a-maze-ing).

## Instructions

Use Python **3.13 or newer** to run the complete collection as written. Most
exercises need only the standard library; some syntax requires 3.12+, and the
Data Quest generator annotations use 3.13+ typing defaults. Publication checks
used Python 3.14.8 on Fedora.

```sh
git clone git@github.com:mohammadhaddad11/python-piscine.git
cd python-piscine
python3 -m venv .venv
. .venv/bin/activate
python3 code_cultivation/ex6/ft_garden_analytics.py
python3 code_Nexus/ex2/data_pipeline.py
python3 Data_Deck/tournament.py
```

For the dependency-based projects:

```sh
python3 -m pip install 'pydantic>=2' -r The_Matrix/ex1/requirements.txt \
  -r The_Matrix/ex2/requirements.txt
```

Individual READMEs explain execution context, required input, intentional
failures, and generated files. Growing Code modules define functions without
calling them, so executing those files alone normally prints nothing.

## Technical Organization and Design Decisions

Exercise directories deliberately repeat classes and helper names as concepts
are introduced. They are not a shared framework. Run demonstrations separately
to avoid confusing similarly named modules such as `ex0` or `elements`.
Imports inside Data Deck and The Codex rely on their retained package layouts.

Current local code-cultivation and file-I/O sources replace the corresponding
older remote files. Remote-only material remains: the old root-level garden
analytics script, established Code Nexus entry paths, and Matrix's dotenv
requirements. The local completed Code Nexus stream implementation also updates
its existing top-level path. Garden Guardian retains a valid remote-only
`WaterError` definition instead of applying a deletion-only local difference.

## Verification

On 2026-10-27, all **85 published Python source files** compiled successfully
in memory. Demonstration checks exercised all seven corrected garden exercises,
all four archive exercises through scripts/API calls, processor pipelines,
creature strategies, Pydantic examples, functional exercises, import demos,
interactive input, and basic function calls. Both deliberately failing Codex
examples produced the expected exceptions.

The live Matrix weather request succeeded, processed 72 hourly records, and
generated its chart using a headless Matplotlib backend. Configuration checks
covered valid settings, invalid mode, and missing variables. These observations
do not guarantee future availability of the external weather service.

### Known issues retained in source

- `code_cultivation/ft_garden_analytics.py` is an older remote-only variant.
  Running it raises `NameError` for undefined `Flower`. Use the current
  `code_cultivation/ex6/ft_garden_analytics.py`, which passed its demonstration.
- Data Quest inventory with `potion:0` raises `ZeroDivisionError` because total
  quantity is zero. Positive-total input passed.
- Some demonstrations are randomized or intentionally raise exceptions; exact
  output is not always deterministic.

The implementation was not silently rewritten to conceal these findings.
No official evaluation, exhaustive type check, or complete unit-test coverage
of every exercise is claimed.

## Resources

- [Python tutorial](https://docs.python.org/3/tutorial/).
- [Standard library](https://docs.python.org/3/library/).
- [Pydantic documentation](https://docs.pydantic.dev/latest/).
- [Open-Meteo forecast API](https://open-meteo.com/en/docs).
- Collection/index presentation informed by [AhmadNajiKam/42_Python_Projects](https://github.com/AhmadNajiKam/42_Python_Projects). No implementation or documentation text was copied.

## AI Usage

An AI coding assistant helped compare local/remote versions, organize this
publication, write READMEs, and execute verification checks. The available
Piscine files do not establish how AI was used during the original exercise
implementation; no claim of either AI-free development or AI authorship is made.
The source changes come from the supplied local implementations and retained
remote work, rather than replacement solutions generated for the portfolio.
