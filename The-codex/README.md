*42 curriculum exercises. Portfolio maintainer: mhaddad.*

# The Codex

## Description

A set of import experiments explains modules, package initialization,
namespaces, explicit exports, aliases, relative imports, and circular
dependencies. Several examples deliberately contrast a working import with a
failure, so not every script is expected to exit successfully.

## Instructions

Python 3.10+; standard library only. Run from this directory:

```sh
python3 ft_alembic_0.py
python3 ft_distillation_0.py
python3 ft_transmutation_0.py
python3 ft_kaboom_0.py
```

The alembic series has six numbered scripts, distillation two, transmutation
three, and kaboom two. The following are intentional failing demonstrations:

```sh
python3 ft_alembic_4.py
python3 ft_kaboom_1.py
```

The first accesses an attribute not exposed by the package; the second triggers
the dark spellbook/validator circular dependency. Expect exceptions and a
nonzero exit from both.

## Technical Implementation

```text
elements.py                   independent root module
alchemy/
  __init__.py                 package exports and aliases
  elements.py                 a different element module
  potions.py
  transmutation/
    __init__.py
    recipes.py
  grimoire/
    light_spellbook.py        delayed relative import
    light_validator.py
    dark_spellbook.py         circular-import example
    dark_validator.py
```

The root `elements.py` provides fire/water while `alchemy.elements` provides
earth/air. Both are necessary; they are not accidental duplicates. The light
spellbook's function-local import delays dependency resolution until the
function is called. The current local relative import keeps resolution inside
the package.

## Design Decisions and Verification

Small isolated demonstrations make import timing and namespace choices visible.
There is no package-installation step or console entry point. All 24 files
passed syntax checks. Root demonstrations passed on Python 3.14.8 with the two
documented failures observed as expected. Package layout was preserved.

## Resources

- [Modules and packages](https://docs.python.org/3/tutorial/modules.html).
- [Import system](https://docs.python.org/3/reference/import.html).

## AI Usage

AI assisted source comparison, this README, and expected-failure checks during
publication. Historical implementation use is not established; see the
[collection disclosure](../README.md#ai-usage).
