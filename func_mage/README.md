*42 curriculum exercises. Portfolio maintainer: mhaddad.*

# func_mage

## Description

Five functional-programming exercises use spell-themed callables to explore
composition, closures, captured state, decorators, and `functools`. Functions are
treated as values that can be passed, returned, specialized, and wrapped.

## Instructions

Python 3.10+; standard library only. Each exercise includes a main demonstration:

```sh
python3 ex0/lambda_spells.py
python3 ex1/higher_magic.py
python3 ex2/scope_mysteries.py
python3 ex3/functools_artifacts.py
python3 ex4/decorator_mastery.py
```

## Technical Implementation

| Exercise | Concepts |
| --- | --- |
| ex0 | Lambdas for sort keys, filtering, mapping, and aggregate statistics |
| ex1 | Function combiners, amplifiers, conditional execution, callable sequences |
| ex2 | `nonlocal` counters, accumulators, closure-private memory |
| ex3 | `reduce`, `partial`, cached Fibonacci, `singledispatch` |
| ex4 | Timing, minimum-power and retry decorators; `wraps`; static/instance methods |

## Algorithms and Design Decisions

Closures keep mutable state without exposing a new class interface. Partial
application binds selected arguments; dispatch selects behavior from the
argument type. Caching avoids repeatedly expanding the same Fibonacci
subproblems, trading stored results for reduced repeated work.

The timing decorator measures wall time and is illustrative rather than a
benchmark framework. Retry catches exceptions and returns a failure message
after exhaustion; it does not implement delays, backoff, or selective retry
policies. Minimum-power validation returns a message instead of raising.

## Verification

All five scripts passed syntax and demonstration checks on Python 3.14.8,
including closure state, decorated calls, repeated failure, and successful
retry-wrapper execution. This is demonstration coverage, not validation of all
possible callable signatures or unbounded recursion sizes.

## Resources

- [Functional programming HOWTO](https://docs.python.org/3/howto/functional.html).
- [functools](https://docs.python.org/3/library/functools.html).
- [Python scopes](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces).

## AI Usage

AI assisted publication documentation and execution checks. The available
source does not establish original AI usage; see the
[collection disclosure](../README.md#ai-usage).
