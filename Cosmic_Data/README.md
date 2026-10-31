*42 curriculum exercises · mhaddad*

# Cosmic Data

Cosmic Data defines validated records for a space station, an alien-contact
report, and a staffed mission. Instead of scattering checks around printing
code, the exercises attach constraints to Pydantic models so a caller must
construct a valid object before using it.

The progression starts with individual field bounds, adds rules relating
several fields, and finishes with validation across nested crew objects.
The scripts demonstrate successful construction alongside rejected examples;
they do not implement a database or network API.

## Instructions

Use Python **3.11+** (`typing.Self` is used) and Pydantic v2 in an environment:

```sh
python3 -m pip install 'pydantic>=2'
python3 ex0/space_station.py
python3 ex1/alien_contact.py
python3 ex2/space_crew.py
```

Run from this directory. The demos catch `ValidationError` and print the first
error message, so a printed expected error normally does not mean the script
failed to run.

## ex0 — Keeping a station record within field bounds

[`SpaceStation`](ex0/space_station.py) combines identifiers, staffing, system
levels, a maintenance timestamp, an operational flag, and optional notes.
Pydantic constructs typed attributes and enforces these principal bounds:

- Station ID length 3–10 and name length 1–50.
- Crew size 1–20; power and oxygen between 0 and 100.
- A required `datetime` maintenance value; notes default to `None` and are
  limited to 200 characters.

`ConfigDict(validate_assignment=True)` also validates direct later assignments
to model fields, not only initial construction. This makes field validation
part of the object interface rather than a one-time check in the driver.

The demo creates a six-person station with power 95.0 and oxygen 98.0, prints
its status, then tries a crew size of 25 and reports the expected validation
error. The operational flag defaults to `True`; it is not inferred from the
power or oxygen values.

## ex1 — Rules that depend on the whole contact report

[`AlienContact` and `ContactType`](ex1/alien_contact.py) describe radio, visual,
physical, and telepathic reports. Field constraints limit signal strength to
0–10, duration to 1–1,440 minutes, and witnesses to 1–100, alongside text bounds.

An `@model_validator(mode="after")` then enforces relationships on the typed
instance:

1. The contact ID must start with `AC`.
2. Physical contact must be verified.
3. Telepathic contact needs at least three witnesses.
4. Signal strength **greater than 7.0** requires a nonempty, non-whitespace
   received message.

These checks need the combined report: a witness count valid by itself can
still be insufficient for telepathic contact. Returning `self` completes the
successful validation; raising `ValueError` becomes a Pydantic validation error.

The script's valid radio report prints signal 8.0, five witnesses, and message
`Hello`. Its rejected telepathic report has only one witness and produces:

```text
Expected validation error:
Value error, Telepathic contact requires at least 3 witnesses
```

The message requirement does not apply at exactly 7.0. If several rules fail,
the first raised model error determines the displayed message.

## ex2 — Validating a mission and its nested crew

[`CrewMember`, `Rank`, and `SpaceMission`](ex2/space_crew.py) separate an
individual's validity from whether a group is suitable for a mission.

`CrewMember` validates an ID, name, rank enum, age 18–80, specialization,
experience 0–50 years, and an active flag. `SpaceMission` contains one to twelve
members together with a destination, launch date, duration 1–3,650 days, status,
and budget 1–10,000 million.

The mission validator requires an ID beginning with `M`, at least one captain
or commander, and no inactive member. For missions **longer than 365 days**,
at least half the crew, rounded up, must have five or more years of experience.
For a three-person long mission, that means two experienced members. A one-year
mission does not enter that additional branch.

The nested list means member-level validation happens before the mission rule
can inspect ranks and experience. The demo accepts a commander-led mission and
rejects one containing only an officer. Names printed in these sample records
are example data, not author or collaborator credits.

## Design decisions and boundaries

All three models enable assignment validation, but that does not make an entire
object graph immutable. In-place list changes or edits to an already nested
member do not automatically rerun every parent-mission rule. Revalidate a
mission when its composition changes rather than assuming it is permanently
valid after construction.

Pydantic can coerce compatible input values. These models do not enable global
strict mode, and free-form fields such as `mission_status` are not constrained
to a status enum. The examples demonstrate typed boundaries and domain rules,
not comprehensive real-world mission authorization.

All three demos were run with Pydantic v2 on Python 3.14. Timestamps in
mission output change between runs; validation message formatting may vary
between Pydantic releases.

## Resources

- [Pydantic models](https://docs.pydantic.dev/latest/concepts/models/)
- [Pydantic validators](https://docs.pydantic.dev/latest/concepts/validators/)
- [Python enum](https://docs.python.org/3/library/enum.html)

## AI Usage

AI assisted documentation and example checks. Original implementation AI use
is not established; see the [collection disclosure](../README.md#ai-usage).
