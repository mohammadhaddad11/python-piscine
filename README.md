*42 curriculum exercises · mhaddad*

# Python Piscine

Eleven projects exploring Python from fundamental functions to object-oriented design, data validation, and reusable modules. Each project is self-contained and documented separately.

## Projects

| Project | Main concepts |
| --- | --- |
| [Growing Code](Growing_Code/) | Functions, loops, recursion, console input |
| [Code Cultivation](code_cultivation/) | Classes, encapsulation, inheritance |
| [Garden Guardian](Garden_Guardian/) | Exceptions and cleanup |
| [Data Quest](Data-Quest/) | Collections, comprehensions, generators |
| [Data Archivist](Data_Archivist/) | File I/O, streams, context managers |
| [The Codex](The-codex/) | Modules, packages, imports |
| [Code Nexus](code_Nexus/) | Abstract classes, processors, pipelines |
| [Data Deck](Data_Deck/) | Factories, interfaces, strategy pattern |
| [Func Mage](func_mage/) | Closures, decorators, higher-order functions |
| [The Matrix](The_Matrix/) | Virtual environments, APIs, configuration |
| [Cosmic Data](Cosmic_Data/) | Pydantic models and validation |

My larger Python project, [A-Maze-ing](https://github.com/mohammadhaddad11/a-maze-ing), lives in its own repository.

## Instructions

Python **3.13+** is required to run the entire collection unchanged because of the generator annotations in Data Quest. Most exercises use only the standard library. Run examples individually from the repository root:

```sh
git clone git@github.com:mohammadhaddad11/python-piscine.git
cd python-piscine
python3 code_cultivation/ex6/ft_garden_analytics.py
python3 code_Nexus/ex2/data_pipeline.py
python3 Data_Deck/tournament.py
```

For exercises with third-party dependencies, use a virtual environment:

```sh
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install 'pydantic>=2' -r The_Matrix/ex1/requirements.txt -r The_Matrix/ex2/requirements.txt
```

The README in each project lists its entry points, required input, and any intentional error examples. The folders are independent exercises, not one shared installable application.

## Notes

- Some examples deliberately raise exceptions to demonstrate Python error handling or import behavior.
- The root-level `code_cultivation/ft_garden_analytics.py` is an older script that currently raises `NameError`; use `code_cultivation/ex6/ft_garden_analytics.py` instead.
- Data Quest's inventory example divides by the item total and raises `ZeroDivisionError` when all quantities are zero.
- Some examples depend on live network services or generate randomized output.

## Resources

- [Python documentation](https://docs.python.org/3/)
- [Python tutorial](https://docs.python.org/3/tutorial/)
- [Python standard library](https://docs.python.org/3/library/)
- [Pydantic documentation](https://docs.pydantic.dev/latest/)
- [Open-Meteo API](https://open-meteo.com/en/docs)

## AI Usage

AI tools assisted with comparing repository versions, preparing documentation, and running checks during the earlier portfolio publication. This refresh uses AI-assisted documentation review. These activities do not establish how AI was used during the original implementation of each exercise.
