*42 curriculum exercises. Portfolio maintainer: mhaddad.*

# Cosmic Data

## Description

Space-themed Pydantic models demonstrate typed data validation, field bounds,
enums, optional values, assignment validation, and relationships between fields
and nested objects. The aim is to keep invalid states out of the model layer.

## Instructions

Python 3.11+ is required by the use of `typing.Self`; install Pydantic v2:

```sh
python3 -m pip install 'pydantic>=2'
python3 ex0/space_station.py
python3 ex1/alien_contact.py
python3 ex2/space_crew.py
```

The examples construct both valid and invalid data. Printed validation errors
are intentional demonstrations and do not necessarily mean a nonzero exit.

## Technical Implementation

| Exercise | Model and rules |
| --- | --- |
| ex0 | `SpaceStation`: constrained attributes, optional notes, assignment validation |
| ex1 | `AlienContact` and `ContactType`: identifier prefix, physical-contact verification, telepathic witnesses, strong-signal message rules |
| ex2 | `CrewMember`, `Rank`, `SpaceMission`: nested crew, required captain/commander, active membership and long-mission staffing constraints |

Field constraints express local bounds; model validators enforce relationships
that cannot be checked one field at a time. Enums constrain categories, while
nested models make crew validation reusable.

## Design Decisions and Verification

Pydantic performs coercion as well as validation; these models are not strict
JSON schemas that reject every convertible input. They are in-memory examples,
not a database, API server, or persistence system. Names in the crew examples
are sample data, not collaborator credits.

All three files match the previously published source. Syntax and standalone
valid/invalid demonstrations passed on Python 3.14.8 with Pydantic 2.14.1.
Every possible validator branch has not been exhaustively tested.

## Resources

- [Pydantic models](https://docs.pydantic.dev/latest/concepts/models/).
- [Pydantic validators](https://docs.pydantic.dev/latest/concepts/validators/).
- [Python enum](https://docs.python.org/3/library/enum.html).

## AI Usage

AI assisted this documentation and publication verification. Available files
do not establish original implementation AI use; see the
[collection disclosure](../README.md#ai-usage).
