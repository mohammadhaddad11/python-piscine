*42 curriculum exercises · mhaddad*

# Data Archivist

Four exercises using Python file streams, explicit cleanup, standard I/O, and context managers.

## Description

| Exercise | Focus |
| --- | --- |
| `ex0` | Reading and closing a file safely |
| `ex1` | Text transformation and optional output file |
| `ex2` | `stdin`, `stdout`, and `stderr` |
| `ex3` | Context-managed archive helper |

## Instructions

Requirements: Python 3.10+ (standard library only). Run from this directory:

```sh
python3 ex0/ft_ancient_text.py README.md
python3 ex1/ft_archive_creation.py README.md
python3 ex2/ft_stream_management.py README.md
python3 -c 'import runpy; f = runpy.run_path("ex3/ft_vault_security.py")["secure_archive"]; print(f("README.md"))'
```

## Technical Notes

Exercises 1 and 2 ask for an output filename and open it in write mode; use a disposable path because an existing file can be overwritten. Enter an empty line to skip saving. The examples read the complete input and transform it in memory, not as a compressed or streaming archive.

The transformation appends `#` to each component of `content.split("\n")`; input ending with a newline therefore adds a final `#` line.

The `ex3/ft_vault_security.py` helper illustrates file cleanup with `with`; its standalone sample paths are demonstrations, not bundled files.

## Resources

- [File I/O](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) · [Cleanup](https://docs.python.org/3/tutorial/errors.html#defining-clean-up-actions)
- [Standard streams](https://docs.python.org/3/library/sys.html#sys.stdin)

## AI Usage

AI assistance supported documentation and verification during portfolio publication. See the [collection's AI usage note](../README.md#ai-usage).
