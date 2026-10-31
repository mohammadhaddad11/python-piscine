*42 curriculum exercises · mhaddad*

# Code Nexus

Code Nexus builds an in-memory processing pipeline for mixed numeric, text,
and log records. It validates inputs, stores normalized outputs, routes a
stream to suitable processors, and finally hands batches to interchangeable
export plugins.

The three exercises expose a growing interface: first “process this value,”
then “route these mixed values,” and finally “consume processed output through
a chosen exporter.” They print demonstrations rather than run a server or
write an external data store.

## Instructions

Python 3.10+; standard library only. From this directory:

```sh
python3 ex0/data_processor.py
python3 ex1/data_stream.py
python3 ex2/data_pipeline.py
```

The root-level `data_processor.py` and `data_stream.py` also provide the first
two demonstrations. The exercise directories keep each stage self-contained;
similarly named classes in different files are separate Python classes.

## ex0 — A common contract for three kinds of input

[`DataProcessor`](ex0/data_processor.py) is an abstract base requiring
`validate(data)` and `ingest(data)`. The base stores `data`, a list of
`(sequence_number, string_value)` pairs, and a counter for total items ingested.
`output()` removes the oldest pair, raising `ValueError` if no output remains.

The concrete processors give that interface practical behavior:

- `NumericProcessor` accepts integers/floats or homogeneous lists of them.
  Booleans are explicitly excluded even though `bool` is a subclass of `int`.
  Accepted numbers are converted to strings.
- `TextProcessor` accepts a string or a list containing only strings.
- `LogProcessor` accepts a dictionary, or a list of dictionaries, whose keys
  are **exactly** `log_level` and `log_message`, both strings. It combines each
  into a value such as `ERROR: Unauthorized access!!`.

Ingestion validates again, so a caller cannot bypass checks merely by omitting
a prior `validate()` call. A list is checked as a whole before records are
appended. Each element receives its own increasing ID, starting at zero.

```sh
python3 - <<'PY'
import runpy
NumericProcessor = runpy.run_path("ex0/data_processor.py")["NumericProcessor"]
processor = NumericProcessor()
processor.ingest([10, 20])
print(processor.output())
print(processor.counter, len(processor.data))
PY
```

```text
(0, '10')
2 1
```

The total counter stays at two after one record is consumed. “Processed” and
“still queued” are different measurements.

## ex1 — Ordered routing of mixed records

[`DataStream`](ex1/data_stream.py) owns a list of processors registered with
`register_processor`. For every stream element, `process_stream` checks them
in registration order. The first one that validates and successfully ingests
the element handles it; a caught `ValueError` permits trying another processor.
Unmatched elements produce a diagnostic message.

```text
mixed input → first accepting processor → numbered string records → FIFO output
```

A list inside the stream is one candidate input for routing, then expands into
multiple records inside its accepting processor. For example, `[3.14, -1, 2.71]`
is one stream element but adds three numeric output records.

The demo initially registers only the numeric processor and shows unhandled
text/log data. After registering all three, the same batch is routed completely.
Statistics report cumulative counters alongside remaining queue lengths.

Registration order is part of the policy: empty lists satisfy all three
processors' `all(...)` checks, so the first receives them. This is not a
type-inference system that guarantees one uniquely matching handler.

## ex2 — Consuming queues through an export interface

[`data_pipeline.py`](ex2/data_pipeline.py) extends the stream with
`output_pipeline(nb, plugin)`. For **each processor**, it takes up to `nb`
available records using `output()`, then calls `plugin.process_output(batch)`
if the batch is nonempty. `nb` is not a single limit shared across the stream.

`ExportPlugin` is a typing `Protocol`: an exporter supplies the expected method
without inheriting a common implementation. `CSVExportPlugin` joins record
values with commas. `JSONExportPlugin` creates `item_<sequence_number>` keys
and string values, retaining the processor's local IDs.

The first pipeline demonstration prints, among its output:

```text
CSV Output:
3.14,-1,2.71
CSV Output:
Hello world,Hi,five
```

Export **removes** records. After those batches, the numeric queue still has
one item but the text queue is empty. Sending a second batch then exporting
JSON demonstrates that counters continue increasing rather than restarting.

The plugins print to stdout; they do not create CSV/JSON files. Their formatting
is hand-built and does not escape embedded commas, quotes, or line breaks, so
they are demonstrations of an output interface, not general serializers.

## Technical decisions and limitations

Processor lists and a stable interface separate routing from data-specific
validation. Numbered outputs make order visible without keeping original
numeric types. However, `list.pop(0)` shifts the remaining queue and is linear
in its size. There is no asynchronous stream, persistence, backpressure, or
automatic rollback if a later plugin fails after records have been removed.

The processor, stream, and pipeline demos were run successfully. The project
demonstrates abstract contracts, subtype polymorphism, ordered dispatch, FIFO
state, and structural output interfaces through one connected workflow.

## Resources

- [Abstract base classes](https://docs.python.org/3/library/abc.html)
- [Protocols](https://docs.python.org/3/library/typing.html#typing.Protocol)
- [Collections and queues](https://docs.python.org/3/tutorial/datastructures.html)

## AI Usage

AI assisted documentation and checking examples. Historical implementation
AI usage is not established; see the [collection disclosure](../README.md#ai-usage).
