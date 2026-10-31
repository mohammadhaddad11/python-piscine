*42 curriculum exercises · mhaddad*

# The Codex

The Codex is a set of runnable experiments in organizing Python code across
modules and packages. Its alchemy functions return short messages, allowing
each demonstration to focus on **which function an import resolves to**,
**which names a package exposes**, and **when a dependency is loaded**.

The sequence starts with one module, introduces a package facade, composes
functions across subpackages, and ends by contrasting a working deferred import
with a circular import that fails during initialization.

## Instructions

Python 3.10+; standard library only. Run from this directory, keeping the
`alchemy/` tree and the root `elements.py` together:

```sh
python3 ft_alembic_0.py
python3 ft_distillation_0.py
python3 ft_transmutation_0.py
python3 ft_kaboom_0.py
```

The scripts print at module level, so importing a demonstration can also run
its prints. Two intentional failures are described below; a nonzero exit from
those examples is expected.

## Module layout: two distinct meanings of “elements”

```text
elements.py                  fire and water functions
alchemy/
  __init__.py                package-facing names and heal alias
  elements.py                earth and air functions
  potions.py                 combines the two element modules
  transmutation/
    __init__.py
    recipes.py               combines an element and a potion
  grimoire/
    __init__.py              exposes the light spell recorder
    light_spellbook.py       defers importing its validator
    light_validator.py
    dark_spellbook.py        imports its validator immediately
    dark_validator.py
```

The root [`elements.py`](elements.py) is intentionally different from
[`alchemy/elements.py`](alchemy/elements.py). In `potions.py`, `import elements`
loads the former while `from . import elements as alch_elements` selects the
latter. Retaining both makes absolute and relative resolution observable.

## Alembic exercises — module access and the package facade

### Alembic 0 — Access through a module object

[`ft_alembic_0.py`](ft_alembic_0.py) uses `import elements`, then calls
`elements.create_fire()`. The module name remains the explicit namespace;
the returned value is `Fire element created`.

### Alembic 1 — Bind one function directly

[`ft_alembic_1.py`](ft_alembic_1.py) imports `create_water` from the root module
and calls it without a module prefix. The behavior is still defined in
`elements.py`; only the name bound in the caller has changed.

### Alembic 2 — Address a module inside a package

[`ft_alembic_2.py`](ft_alembic_2.py) imports `alchemy.elements` and calls its
`create_earth()`. The qualified path distinguishes it from the root module
with the same basename.

### Alembic 3 — Import from the qualified module

[`ft_alembic_3.py`](ft_alembic_3.py) binds `create_air` directly from
`alchemy.elements`. Comparing it with Alembic 1 shows how the source module
path, not the function-call syntax, determines the selected implementation.

### Alembic 4 — A package exposes selected names

[`ft_alembic_4.py`](ft_alembic_4.py) imports `alchemy`. Its `__init__.py` binds
`create_air`, so that call works. It does not bind `create_earth` at the package
root, so `alchemy.create_earth()` raises `AttributeError` after the script's
warning message. The function remains reachable through `alchemy.elements`;
this is namespace organization, not a privacy/security boundary.

### Alembic 5 — Use the facade's exported function

[`ft_alembic_5.py`](ft_alembic_5.py) uses `from alchemy import create_air` to
request the convenient package-level name. [`__all__`](alchemy/__init__.py)
also describes the names used by wildcard import; it does not itself prevent
explicit access to other available module attributes.

## Distillation exercises — composing modules and aliases

### Distillation 0 — Call the potion functions directly

[`ft_distillation_0.py`](ft_distillation_0.py) imports both functions from
[`potions.py`](alchemy/potions.py). `healing_potion()` combines earth and air
from the package-relative element module. `strength_potion()` combines fire
and water from the root module. Each constructs its return string from the
results of those function calls.

For example, the strength result is:

```text
Strength potion brewed with 'Fire element created' and 'Water element created'
```

### Distillation 1 — Provide a shorter package API

[`ft_distillation_1.py`](ft_distillation_1.py) accesses the same behavior through
`alchemy.potions.strength_potion()` and `alchemy.heal()`. The `heal` name is an
alias bound to `healing_potion`, not another potion implementation. The package
initializer therefore controls a convenient entry point without duplicating
the underlying work.

## Transmutation exercises — traversing nested packages

### Transmutation 0 — Import the recipe module explicitly

[`ft_transmutation_0.py`](ft_transmutation_0.py) imports the full
`alchemy.transmutation.recipes` path and invokes `lead_to_gold()`. The
[recipe](alchemy/transmutation/recipes.py) calls `create_air`, `strength_potion`,
and root `elements.create_fire()`, then combines their descriptions. Its imports
deliberately mix `..elements`, an absolute package path, and a top-level module.

### Transmutation 1 — Let the subpackage initialize its contents

[`ft_transmutation_1.py`](ft_transmutation_1.py) imports `alchemy.transmutation`.
That subpackage's [`__init__.py`](alchemy/transmutation/__init__.py) imports
`recipes`, so the driver can reach the recipe without spelling its module in
the import statement.

### Transmutation 2 — Reach the same recipe from the top-level facade

[`ft_transmutation_2.py`](ft_transmutation_2.py) imports only `alchemy`. Its
initializer imports `transmutation`, which imports `recipes`, making the same
call path available through chained package attributes. All three drivers
resolve to the same recipe; they demonstrate different initialization routes,
not three transmutation algorithms.

## Kaboom exercises — why import timing matters

### Kaboom 0 — Defer a dependency until a call needs it

[`ft_kaboom_0.py`](ft_kaboom_0.py) calls the package-exposed light recorder.
[`light_spell_record`](alchemy/grimoire/light_spellbook.py) imports its
validator **inside the function**. By then the spellbook's
`light_spell_allowed_ingredients` function has been defined, so the validator
can import it back without requesting a missing name from a half-built module.

The validator lowercases the input and checks whether any allowed element name
occurs as a substring. It returns a status string, which the recorder embeds:

```text
Spell recorded: Fantasy (Earth, wind and fire - VALID)
```

This is not token-level ingredient parsing: a substring match is sufficient.

### Kaboom 1 — Fail while two modules initialize each other

[`ft_kaboom_1.py`](ft_kaboom_1.py) imports
[`dark_spellbook.py`](alchemy/grimoire/dark_spellbook.py), which immediately
imports [`dark_validator.py`](alchemy/grimoire/dark_validator.py). The validator
then requests `dark_spell_allowed_ingredients` before the spellbook has reached
its definition. Python raises an import error for the partially initialized
module. No spell recording occurs.

```sh
python3 ft_alembic_4.py
python3 ft_kaboom_1.py
```

Both commands intentionally exit with an exception. The contrast with the light
version demonstrates a dependency-order problem, not an arbitrary limitation
that all circular references always fail.

## What the project demonstrates

All thirteen drivers were exercised, including the two expected failures.
The project makes namespace binding, package initialization, relative paths,
aliasing, and deferred imports concrete. It has no installation metadata or
database; keeping execution rooted in this directory is important because
the top-level `elements` dependency must remain importable.

## Resources

- [Modules and packages](https://docs.python.org/3/tutorial/modules.html)
- [Import system](https://docs.python.org/3/reference/import.html)

## AI Usage

AI assisted documentation and checking the working/failing demonstrations.
Original implementation AI use is not established; see the
[collection disclosure](../README.md#ai-usage).
