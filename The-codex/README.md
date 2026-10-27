*42 curriculum exercises · mhaddad*

# The Codex

Small import experiments demonstrating namespaces, packages, explicit exports, relative imports, and circular dependencies.

## Description

| Exercise | Focus |
| --- | --- |
| `ft_alembic_*` | Module and package access |
| `ft_distillation_*` | Imports and aliases |
| `ft_transmutation_*` | Relative imports and subpackages |
| `ft_kaboom_*` | Import timing and circular dependencies |

## Instructions

Requirements: Python 3.10+ (standard library only). Run from this directory:

```sh
python3 ft_alembic_0.py
python3 ft_distillation_0.py
python3 ft_transmutation_0.py
python3 ft_kaboom_0.py
```

## Technical Notes

Run scripts from this directory so their imports resolve as expected. `elements.py` and `alchemy/elements.py` are intentionally different modules, not duplicates.

`ft_alembic_4.py` and `ft_kaboom_1.py` intentionally raise exceptions; the latter demonstrates a circular dependency.

## Resources

- [Modules](https://docs.python.org/3/tutorial/modules.html) · [Import system](https://docs.python.org/3/reference/import.html)

## AI Usage

AI assistance supported documentation and verification during portfolio publication. See the [collection's AI usage note](../README.md#ai-usage).
