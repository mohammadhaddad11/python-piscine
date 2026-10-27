*42 curriculum exercises. Portfolio maintainer: mhaddad.*

# Code Nexus

## Description

A progression from abstract data processors to polymorphic stream routing and
pluggable output. The exercises use numeric, text, and log records to explore
interfaces, validation, ordered dispatch, and separation of concerns.

## Instructions

Python 3.10+; standard library only. From this directory:

```sh
python3 ex0/data_processor.py
python3 ex1/data_stream.py
python3 ex2/data_pipeline.py
```

The established top-level `data_processor.py` and `data_stream.py` paths remain
usable. The latter now contains the completed local implementation instead of
the remote version's unfinished method body.

## Technical Implementation

`DataProcessor` is an abstract base class requiring validation and ingestion.
Each concrete processor stores numbered `(counter, string)` items in a list.
Numeric validation excludes booleans; log records require `log_level` and
`log_message` string fields. `output()` removes the oldest item or raises when
empty.

`DataStream` keeps processors in registration order. Each stream element goes
to the first processor that accepts and ingests it; unmatched items produce a
message. The pipeline exercise adds an export protocol and CSV/JSON-style
plugins that print their results to stdout.

## Algorithms and Design Decisions

Ordered routing demonstrates polymorphism without a central type switch.
FIFO consumption uses `list.pop(0)`, so removal is linear in queue length.
The exporters manually build strings: they are not general-purpose escaped CSV
or JSON serializers and do not persist files. Empty-list validation can match
more than one processor; registration order determines the recipient.

## Verification

All five published entry paths passed syntax and demonstration checks on
Python 3.14.8, including stream dispatch, processor statistics, consumption,
and pipeline export. The checks do not establish serializer conformance for
arbitrary embedded punctuation or exhaustive processor contracts.

## Resources

- [Abstract base classes](https://docs.python.org/3/library/abc.html).
- [Protocols](https://docs.python.org/3/library/typing.html#typing.Protocol).
- [Collections and queues](https://docs.python.org/3/tutorial/datastructures.html).

## AI Usage

AI assisted the local/remote comparison, documentation, and execution checks.
The processor implementation came from the supplied local source. Historical
AI use is not established; see the [collection disclosure](../README.md#ai-usage).
