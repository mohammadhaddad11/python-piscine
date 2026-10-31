*42 curriculum exercises · mhaddad*

# Data Archivist

Data Archivist implements a small text-file workflow: open and inspect a file,
transform its contents, optionally save a new copy, and report failures without
leaving the read handle open. Four exercises develop that workflow from manual
cleanup to a reusable context-managed helper.

Despite the archive theme, this is text processing, not compression, encryption,
or a binary archive format.

## Instructions

Use Python 3.10+ and the standard library. Run from this directory:

```sh
python3 ex0/ft_ancient_text.py README.md
python3 ex1/ft_archive_creation.py README.md
python3 ex2/ft_stream_management.py README.md
```

Exercises 0–2 require exactly one filename argument. Exercises 1–2 then ask for
an output filename; enter an empty line to skip writing. A supplied output path
is opened with `"w"` and can replace an existing file.

## ex0 — Read a file and clean up after failure

[`ft_ancient_text()`](ex0/ft_ancient_text.py) opens the given file in text mode,
reads all its content, and prints it between separators. Missing files and
permission errors have explicit messages.

The handle starts as `None` before entering `try`. This matters because opening
can fail before any file object exists: the `finally` block closes only a handle
that was actually created. Both successful reading and exceptions after open
reach cleanup. The printed “closed” message precedes the actual `close()` call.

## ex1 — Transform once, then optionally preserve the result

[`ft_archive_creation()`](ex1/ft_archive_creation.py) first completes the read
and closes its input. It then splits the saved content on `"\n"`, appends `#`
and a newline to every component, prints the transformed text, and asks whether
to save it. It does not reopen the source for the transformation.

For an input containing `alpha\nbeta\n`, the generated file contains:

```text
alpha#
beta#
#
```

The final `#` line is intentional behavior of the current implementation:
splitting a trailing newline produces an empty final component. The function
is not simply copying physical lines unchanged.

The write uses a separate handle and catches filesystem-related errors. Unlike
the later context-manager helper, this save path uses an explicit `close()`
after writing rather than a `with` block.

## ex2 — Separate data, user input, and diagnostics

[`ft_stream_management()`](ex2/ft_stream_management.py) repeats the same read
and transformation but makes stream handling explicit. It obtains the save
name using `sys.stdin.readline().rstrip()` and sends file-access/save errors
to `sys.stderr`, leaving normal reports on stdout.

```sh
python3 ex2/ft_stream_management.py README.md 2> archive-errors.log
```

This lets a shell redirect diagnostics separately from normal output. The
prompt uses `flush=True` so it is visible before waiting for input. Save errors
are caught broadly; an empty stdin line means “do not save.”

## ex3 — A reusable helper with an explicit result contract

[`secure_archive(file, action="r", content="")`](ex3/ft_vault_security.py)
returns `(success, text)` instead of printing from inside the helper. For read
mode, text is the file content; for `"w"`, it writes the supplied content and
returns a confirmation. Exceptions become `(False, error_message)`.

```sh
python3 - <<'PY'
import runpy
secure_archive = runpy.run_path("ex3/ft_vault_security.py")["secure_archive"]
print(secure_archive("archivist-example.txt", "w", "hello"))
print(secure_archive("archivist-example.txt"))
PY
```

```text
(True, 'Content successfully written to file')
(True, 'hello')
```

The `with open(...)` block releases the handle before returning, including on
an error. Only the exact `"w"` action is treated as writing; other modes attempt
`read()`, so this is not a general adapter for every Python file mode.

Its standalone demo uses fixed example paths such as `why.txt` and `m.txt`.
Those are not bundled assets. Direct helper calls make behavior easier to
explore with controlled files.

## Technical decisions and limits

All exercises load whole files into memory. Repeated concatenation builds the
transformed result; there is no streaming or large-file optimization. Text
encoding is the platform default because the `open` calls do not specify one.
Read errors outside the explicitly caught types can still propagate in ex0–2.

Representative checks covered reads, missing input, both transformed save paths,
and helper write/read results. The project demonstrates resource lifetime,
error channels, and a transition from interactive scripts to a callable API.

## Resources

- [Reading and writing files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Cleanup with finally](https://docs.python.org/3/tutorial/errors.html#defining-clean-up-actions)
- [Standard streams](https://docs.python.org/3/library/sys.html#sys.stdin)

## AI Usage

AI assisted documentation and isolated file-I/O example checks. Historical
implementation assistance is not established; see the
[collection disclosure](../README.md#ai-usage).
