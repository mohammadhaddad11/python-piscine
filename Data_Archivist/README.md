*42 curriculum exercises. Portfolio maintainer: mhaddad.*

# Data-Archivist

## Description

Four text-file exercises explore descriptor-backed Python streams, explicit
cleanup, transformations, standard input/output/error, and context managers.
The current local implementations are preserved as the primary source.

## Instructions

Python 3.10+; standard library only. Supply a small UTF-8 text file as the
argument to exercises 0–2:

```sh
python3 ex0/ft_ancient_text.py README.md
python3 ex1/ft_archive_creation.py README.md
python3 ex2/ft_stream_management.py README.md
```

Exercises 1 and 2 ask for an output filename. Enter an empty line to skip
saving. A supplied filename is opened in write mode and can overwrite an
existing file, so use a disposable path when experimenting.

The reusable context-manager helper can be called without its fixed demo paths:

```sh
python3 -c 'import runpy; f = runpy.run_path("ex3/ft_vault_security.py")["secure_archive"]; print(f("README.md"))'
```

## Technical Implementation

| Exercise | Behavior |
| --- | --- |
| ex0 | Read and display a named file; initialize the handle before `try` and close it in `finally` |
| ex1 | Read once, append `#` to each split text line, optionally save with `input()` |
| ex2 | Similar transformation, using `sys.stdin.readline()` and stderr for errors |
| ex3 | `secure_archive(file, action, content)` returns `(success, text)` while `with` closes the file |

## Design Decisions and Limits

The scripts read the complete file into memory. Transformation uses repeated
string concatenation and is not a streaming archive format or compression
algorithm. Splitting on `"\n"` retains a trailing empty component: input ending
with newline therefore gains a final `#` line. Exercise 3 treats `"w"` specially;
other modes attempt a read. Broad exception handlers convert errors into
messages, but do not validate every file-mode contract.

The updated local sources initialize handles safely before cleanup, avoid the
second read in transformation exercises, and expand error reporting. Their
behavior is documented without changing it.

## Verification

Syntax checks passed. Runtime checks covered successful and missing-file reads,
both save paths with disposable files, exact transformed content including the
trailing empty line, and context-managed write/read/failure results. All passed
on Python 3.14.8. Permission-denial behavior was not comprehensively simulated.
The standalone ex3 demo references `why.txt`, `/etc/master.passwd`, and `m.txt`;
these are illustrative paths, not bundled assets or required real credentials.

## Resources

- [Reading and writing files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files).
- [Exception cleanup](https://docs.python.org/3/tutorial/errors.html#defining-clean-up-actions).
- [Standard streams](https://docs.python.org/3/library/sys.html#sys.stdin).

## AI Usage

AI assisted source comparison, README preparation, and isolated file-I/O checks
for publication. Historical implementation assistance is not established; see
the [collection disclosure](../README.md#ai-usage).
