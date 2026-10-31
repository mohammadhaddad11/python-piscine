*42 curriculum exercises · mhaddad*

# Func Mage

Func Mage builds a small toolkit of spell-themed functions: sort and filter
records, combine operations, keep private state between calls, and wrap existing
functions with timing, validation, or retry behavior. The names are playful;
the implementation is about making behavior reusable without writing a class
for every operation.

The five exercises progress from passing a function as an argument, to returning
functions, to retaining state in closures, and finally to decorating callables.
They are independent modules with their own runnable demonstrations.

## Running the exercises

Python 3.10+ and the standard library are sufficient. Run from this directory:

```sh
python3 ex0/lambda_spells.py
python3 ex1/higher_magic.py
python3 ex2/scope_mysteries.py
python3 ex3/functools_artifacts.py
python3 ex4/decorator_mastery.py
```

The examples below use `runpy.run_path` to load a particular exercise without
running its demonstration block. This also avoids confusing functions from
different exercises with one another.

## ex0 — Transforming records with small functions

[`lambda_spells.py`](ex0/lambda_spells.py) operates on lists of dictionaries and
spell names. `artifact_sorter` returns artifacts in descending `power` order,
using a lambda as the sorting key rather than sorting by the whole dictionary.
`power_filter` keeps mages whose power meets an inclusive threshold.
`spell_transformer` maps each name to a decorated string such as `* heal *`.

`mage_stats` extracts power values once, then returns maximum, minimum, and an
average rounded to two decimals. An empty collection returns zero-valued
statistics instead of calling `min` or `max` on an empty list. These helpers
return new containers; they do not reorder the input list in place. The
dictionaries are expected to contain a suitable `power` value.

The script demonstrates the sorter and transformer; the filtering/statistics
helpers are available for direct calls:

```sh
python3 - <<'PY'
import runpy
spells = runpy.run_path("ex0/lambda_spells.py")
print(spells["spell_transformer"](["heal", "shield"]))
print(spells["mage_stats"]([{"power": 10}, {"power": 30}]))
PY
```

```text
['* heal *', '* shield *']
{'max_power': 30, 'min_power': 10, 'avg_power': 20.0}
```

## ex1 — Building new behavior from existing callables

[`higher_magic.py`](ex1/higher_magic.py) uses spells with the common calling
convention `(target, power)`. Each factory returns a new function, delaying the
actual spell execution until the returned function is called.

- `spell_combiner` calls two spells with the same arguments and returns their
  results as a tuple. This combines results; it does not feed one into the other.
- `power_amplifier` captures a multiplier and changes the power before forwarding
  the call to the original spell. The demo turns power 10 into 30.
- `conditional_caster` evaluates a predicate first. If it rejects the call,
  the spell is not executed and the result is `Spell fizzled`.
- `spell_sequence` calls a list of spells in order and collects their results in
  a list. An empty sequence produces an empty result list.

The returned functions share an interface while expressing different policies.
They assume the supplied callables accept that interface; they do not inspect
signatures or catch arbitrary errors from the spells.

## ex2 — Keeping state after a function returns

[`scope_mysteries.py`](ex2/scope_mysteries.py) makes lexical scope observable.
`mage_counter` creates a local integer and returns `inner`, which uses `nonlocal`
to update that same binding on later calls. A second factory call creates a
different binding, so the counters are independent:

```sh
python3 - <<'PY'
import runpy
scope = runpy.run_path("ex2/scope_mysteries.py")
a = scope["mage_counter"]()
b = scope["mage_counter"]()
print(a(), a(), b())
accumulate = scope["spell_accumulator"](100)
print(accumulate(20), accumulate(30))
vault = scope["memory_vault"]()
vault["store"]("answer", 42)
print(vault["recall"]("answer"), vault["recall"]("missing"))
PY
```

```text
1 2 1
120 150
42 Memory not found
```

`spell_accumulator` captures an initial total and adds to it on each call rather
than recalculating from the initial value. `enchantment_factory` captures a
fixed prefix, returning functions that can independently add `Flaming` or
`Frozen` to item names.

`memory_vault` returns a dictionary containing two functions, `store` and
`recall`. Both close over the **same private dictionary**, so a write through
one is visible through the other. No `nonlocal` is needed there because the
functions mutate the dictionary rather than rebind the variable. This is
encapsulation by closure, not encrypted storage or persistent memory.

## ex3 — Specializing, caching, and dispatching functions

[`functools_artifacts.py`](ex3/functools_artifacts.py) replaces some hand-written
function machinery with standard-library tools:

`spell_reducer` folds a list using addition, multiplication, maximum, or minimum.
Unknown operations raise `ValueError` for nonempty input; empty input returns
zero before operation selection, even for multiplication.

`partial_enchanter` creates fire, thunder, and ice variants of a supplied
enchantment function by pre-binding power `50` and an element name. The caller
still supplies the remaining arguments. This is useful when several operations
differ only in configuration.

`memoized_fibonacci` recursively computes Fibonacci numbers with `lru_cache`.
Repeated subproblems can reuse cached values instead of expanding the same
recursion repeatedly. Negative indexes raise `ValueError`; caching does not
remove Python's recursion limit or make arbitrarily large input safe.

`spell_dispatcher` returns a `singledispatch` function: integers become damage
messages, strings are returned unchanged, lists become a spell-count message,
and unsupported types use `Unknown spell type`. Dispatch is based on the first
argument's runtime type rather than an explicit chain inside the caller.

## ex4 — Wrapping a call without replacing its body

[`decorator_mastery.py`](ex4/decorator_mastery.py) implements three wrappers.

`spell_timer(func)` returns a function that prints a casting message, records
wall-clock time, forwards `*args` and `**kwargs` to `func`, and returns its result.
The completion message is printed only after a successful call; exceptions are
not swallowed or timed through a `finally` block.

`power_validator(min_power)` is a **parameterized decorator**. Its outer call
captures the threshold, its factory receives the function, and its wrapper
checks the first `power` argument on each invocation. Accepted calls forward
power and the remaining arguments; rejected calls return
`Insufficient power for this spell` without executing the body.

`retry_spell(max_attempts)` uses the same three-stage construction. Its wrapper
returns immediately when the underlying function succeeds. On an `Exception`,
it tries again, prints intermediate retry messages, and eventually returns a
failure string. It has no backoff or selective retry policy, so retrying a
function with side effects can repeat those side effects.

All three use `functools.wraps` to preserve metadata such as the original name
and docstring. This matters when introspecting decorated functions and when
the timer prints their names; it does not guarantee compatibility with every
possible signature.

`MageGuild.validate_mage_name` is a static name check. `cast_spell` uses a local
helper decorated with a minimum power of 10. In the demo, power 15 returns
`Successfully cast Lightning with 15 power`; power 5 returns the rejection
message. Name validation accepts alphabetic/whitespace strings of length at
least three, so it should not be treated as comprehensive identity validation.

## What this demonstrates

The progression shows how a stable calling convention supports composition,
how closures separate per-instance state without globals, and how decorators
add execution policy around existing functions. The script demos were run on
Python 3.14; timer values vary between runs. The helpers are deliberately small
and do not perform general runtime type validation of arbitrary callbacks.

## Resources

- [Functional programming HOWTO](https://docs.python.org/3/howto/functional.html)
- [functools](https://docs.python.org/3/library/functools.html)
- [Python scopes](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces)

## AI Usage

AI assisted the documentation and checking its examples. Historical AI use in
the exercise implementations is not established by the available files; see
the [collection disclosure](../README.md#ai-usage).
