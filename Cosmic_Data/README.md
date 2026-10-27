*42 curriculum exercises · mhaddad*

# Cosmic Data

Space-themed data models using Pydantic for type constraints, cross-field rules, and nested validation.

## Description

| Exercise | Focus |
| --- | --- |
| `ex0` | `SpaceStation` fields and assignment validation |
| `ex1` | `AlienContact`, enums, and conditional rules |
| `ex2` | Nested crew and mission validation |

## Instructions

Requirements: Python 3.11+ and Pydantic v2. Run from this directory:

```sh
python3 -m pip install 'pydantic>=2'
python3 ex0/space_station.py
python3 ex1/alien_contact.py
python3 ex2/space_crew.py
```

## Technical Notes

Field constraints and validators check individual values; model validators check relationships between fields, such as the required crew composition. Some intentionally invalid examples print validation errors.

Pydantic may coerce compatible input types, so these examples should not be described as strict-schema validators. Names in the sample crew data are not contributor credits.

## Resources

- [Pydantic models](https://docs.pydantic.dev/latest/concepts/models/) · [Validators](https://docs.pydantic.dev/latest/concepts/validators/)
- [Python enum](https://docs.python.org/3/library/enum.html)

## AI Usage

AI assistance supported documentation and verification during portfolio publication. See the [collection's AI usage note](../README.md#ai-usage).
