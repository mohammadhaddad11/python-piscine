*42 curriculum exercises · mhaddad*

# Code Nexus

Abstract processors, input validation, polymorphic routing, and small data-export pipelines.

## Description

| Exercise | Focus |
| --- | --- |
| `ex0` | Abstract `DataProcessor` interface and concrete implementations |
| `ex1` | Ordered stream routing between registered processors |
| `ex2` | Pipeline composition and export protocols |

## Instructions

Requirements: Python 3.10+ (standard library only). Run from this directory:

```sh
python3 ex0/data_processor.py
python3 ex1/data_stream.py
python3 ex2/data_pipeline.py
```

## Technical Notes

Records are offered to processors in registration order. The first one that accepts and successfully ingests a record handles it. The processors store items in a list and remove the oldest item with `pop(0)`, which is linear in the list length.

The example CSV/JSON exporters print constructed output; they are not general-purpose serializers for arbitrary data.

## Resources

- [Abstract base classes](https://docs.python.org/3/library/abc.html) · [Protocols](https://docs.python.org/3/library/typing.html#typing.Protocol)
- [Collections and queues](https://docs.python.org/3/tutorial/datastructures.html)

## AI Usage

AI assistance supported documentation and verification during portfolio publication. See the [collection's AI usage note](../README.md#ai-usage).
