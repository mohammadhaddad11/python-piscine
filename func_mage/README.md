*42 curriculum exercises · mhaddad*

# Func Mage

Five functional-programming exercises built around callables, closures, decorators, and `functools`.

## Description

| Exercise | Focus |
| --- | --- |
| `ex0` | Lambdas, mapping, filtering, and sorting |
| `ex1` | Higher-order functions and composition |
| `ex2` | `nonlocal` state and closures |
| `ex3` | `reduce`, `partial`, caching, and single dispatch |
| `ex4` | Decorators, timing, retries, and `wraps` |

## Instructions

Requirements: Python 3.10+ (standard library only). Run from this directory:

```sh
python3 ex0/lambda_spells.py
python3 ex1/higher_magic.py
python3 ex2/scope_mysteries.py
python3 ex3/functools_artifacts.py
python3 ex4/decorator_mastery.py
```

## Technical Notes

The decorators illustrate how functions can wrap other functions while preserving metadata. Cached Fibonacci avoids recomputing overlapping calls, trading memory for speed.

The retry example does not implement backoff or selective exception handling, and the timing wrapper is a demonstration rather than a benchmarking framework.

## Resources

- [Functional programming](https://docs.python.org/3/howto/functional.html) · [functools](https://docs.python.org/3/library/functools.html)
- [Python scopes](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces)

## AI Usage

AI assistance supported documentation and verification during portfolio publication. See the [collection's AI usage note](../README.md#ai-usage).
