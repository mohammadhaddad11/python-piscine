*42 curriculum exercises · mhaddad*

# Data Quest

Data Quest turns small game-related inputs into reports: inspect command-line
arguments, summarize player scores, measure distances, compare achievements,
analyze inventory, and consume event streams. Each exercise chooses a different
data structure to match the operation being performed.

The progression moves from an ordered list of values to tuples, sets, keyed
records, lazy production, and compact transformations. These are standalone
scripts rather than a game engine or shared analytics service.

## Instructions

Use **Python 3.13+** for the complete project as written. Ex5 uses
`typing.Generator` with a single type argument, relying on the default type
parameters introduced in 3.13. No third-party packages are needed.

Run commands below from this directory. Only the coordinate exercise reads
interactive input; other examples take arguments or use built-in sample data.

## ex0 — Understanding the command line

[`ft_command_quest.py`](ex0/ft_command_quest.py) reports the program name,
enumerates user arguments, and distinguishes their count from `len(sys.argv)`,
which includes the program name itself.

```sh
python3 ex0/ft_command_quest.py alpha beta
```

The report includes `Arguments received: 2`, arguments numbered 1 and 2, and
`Total arguments: 3`. With no user arguments, it prints a separate message
instead of trying to process a missing item.

## ex1 — Summarizing valid scores while rejecting bad entries

[`ft_score_analytics.py`](ex1/ft_score_analytics.py) converts each argument
independently. Invalid text is reported and skipped; valid integers are kept in
a list for count, sum, average, extremes, and range calculations.

```sh
python3 ex1/ft_score_analytics.py 10 bad 30
```

```text
=== Player Score Analytics ===
Invalid parameter: 'bad'
Scores processed: [10, 30]
Total players: 2
Total score: 40
Average score: 20.0
High score: 30
Low score: 10
Score range: 20
```

The nonempty-list check prevents division by zero and empty `min`/`max` calls
when all arguments are rejected. Negative scores are accepted integers; the
script does not impose a game-specific scoring range.

## ex2 — Coordinates as one structured value

[`get_player_pos()`](ex2/ft_coordinate_system.py) repeatedly asks for `x,y,z`,
checks that there are three components, and converts them to floats. On invalid
syntax or conversion it explains the problem and asks again.

```sh
python3 ex2/ft_coordinate_system.py
```

The driver requests two tuples, unpacks their components, computes distance
from the origin for the first, and Euclidean distance between the pair. Enter
`0,0,0` followed by `3,4,0`: the final distance is `5.0`. Calculations are rounded
to four decimal places. EOF and special float values are not separately handled.

## ex3 — Comparing ownership with set operations

[`ft_achievement_tracker.py`](ex3/ft_achievement_tracker.py) gives four players
random subsets of a catalog. `gen_player_achievements()` samples without
replacement and returns a set. Union finds achievements held by anyone;
intersection finds those held by everyone; differences identify a player's
exclusive achievements and the catalog entries they are missing.

```sh
python3 ex3/ft_achievement_tracker.py
```

Sets make membership comparisons direct and eliminate duplicate ownership
entries. The random samples and printed set order vary. The helper uses a
catalog initialized in the script's main block, so importing and calling it
without supplying that module state is not a self-contained API.

## ex4 — Inventory as a mapping from item to quantity

[`ft_inventory_system.py`](ex4/ft_inventory_system.py) parses `item:quantity`
tokens. It rejects malformed separators, discards repeated item names, and
skips quantities that cannot be converted to integers. The dictionary retains
the first accepted quantity rather than combining duplicates.

```sh
python3 ex4/ft_inventory_system.py sword:2 potion:3
```

The total is 5, with sword at `40.0%` and potion at `60.0%`. The script scans the
keys to find most/least abundant items, then inserts `magic_item: 1` and prints
the updated inventory. Percentages and extrema describe the inventory before
that final insertion.

The empty-inventory path avoids percentages. A **nonempty inventory whose
total is zero**, such as `potion:0`, raises `ZeroDivisionError`. Negative
quantities are not rejected and can also create meaningless proportions or a
zero total. This is a known input limitation, not a completed stock validator.

## ex5 — Producing events only when requested

[`ft_data_stream.py`](ex5/ft_data_stream.py) contains two generators with
different lifetimes. `gen_event()` has an infinite loop that yields random
`(player, action)` tuples. `next()` resumes it for one event, so the demo can
print 1,000 events without first allocating a 1,000-element collection.

`consume_event(events)` is finite: it selects an item from a caller-supplied
list, removes it, then yields it. The demo creates ten events and shows the
list shrinking after every yield. Consumption deliberately mutates the input;
it is random removal rather than a FIFO queue. List search/removal still costs
work proportional to list size.

```sh
python3 ex5/ft_data_stream.py
```

Expect substantial output and different player/action combinations on each run.

## ex6 — Expressing transformations and filters directly

[`ft_data_alchemist.py`](ex6/ft_data_alchemist.py) capitalizes sample names with
a list comprehension, separately selects names already starting uppercase,
and builds a dictionary of random scores. A second dictionary comprehension
retains scores strictly above the computed average.

```sh
python3 ex6/ft_data_alchemist.py
```

The two name lists answer different questions: transforming all names is not
the same as filtering the originals. Scores vary, so exact averages and
high-score membership are not fixed output examples.

## Design and checks

The scripts demonstrate ordered aggregation, structured values, set algebra,
keyed lookup, lazy state, and transformation pipelines. Normal examples were
run, including invalid-score and coordinate-retry paths. The zero-total
inventory failure was reproduced. There is no persistent game state or common
validation layer across exercises.

## Resources

- [Python data structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Generator HOWTO](https://docs.python.org/3/howto/functional.html#generators)
- [Generator behavior](https://docs.python.org/3/tutorial/classes.html#generators)
- [Typing Generator](https://docs.python.org/3/library/typing.html#typing.Generator)

## AI Usage

AI assisted the documentation and representative checks. The available files
do not establish original implementation AI use; see the
[collection disclosure](../README.md#ai-usage).
