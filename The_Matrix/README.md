*42 curriculum exercises · mhaddad*

# The Matrix

The Matrix connects three practical Python tasks: identify the environment an
interpreter is using, install and exercise a real data-analysis dependency stack,
and load configuration without embedding values in the program. The central
example fetches an Irbid weather forecast, calculates summary statistics, and
creates a temperature chart.

Each exercise can run independently. Together they show how execution context,
dependencies, external data, and configuration affect an otherwise small script.

## Setup

The project declares Python 3.10+. Use a virtual environment; dependency release
compatibility also depends on the chosen interpreter version. From this directory:

```sh
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -r ex1/requirements.txt -r ex2/requirements.txt
```

Ex1 uses pandas, NumPy, requests, and Matplotlib. Ex2 separately requires
`python-dotenv`, pinned in its requirements file. The
[`pyproject.toml`](ex1/pyproject.toml) describes the data-analysis dependencies
for Poetry as well, with `package-mode=false`: it manages an environment, not
an installable application package.

## ex0 — Find out which interpreter environment is active

[`construct.py`](ex0/construct.py) compares `sys.prefix` with `sys.base_prefix`.
If they differ, it reports a virtual environment, shows the interpreter and
environment paths, and prints the first package installation path returned by
`site.getsitepackages()`. Otherwise it prints activation instructions.

```sh
python3 ex0/construct.py
```

The output changes with the interpreter used to launch the command, not merely
the shell prompt. Its purpose is diagnosing package-installation context.
A virtual environment isolates Python package selection; the script's themed
messages do not make it a security sandbox.

## ex1 — From an HTTP response to a chart

[`loading.py`](ex1/loading.py) implements the following pipeline:

```text
dependency discovery → HTTP forecast → hourly structure check
    → DataFrame/time conversion → numeric summaries → first-day chart
```

### Check dependencies before doing work

`check_dependencies()` uses `importlib.util.find_spec` to detect the four
required packages. `get_version()` asks distribution metadata for versions
rather than assuming every imported module has a `__version__` attribute.
Missing packages trigger installation guidance and a nonzero exit. The script
also prints a short pip/Poetry comparison; it does not run either installer.

### Request and validate the forecast

The request targets Open-Meteo at latitude 32.5556, longitude 35.85, asking for
three days of hourly temperature, wind speed, and relative humidity. A
ten-second timeout, HTTP status check, JSON decoding, and exception handlers
separate connection/status failures from invalid JSON.

`check_hourly()` requires a dictionary containing a dictionary of four nonempty,
equally sized lists: time, temperature, wind, and humidity. That catches missing
or mismatched columns before constructing a DataFrame. It does not validate
every timestamp or numeric element, so later conversions can still fail.

### Calculate and render

The script parses the time column with pandas, converts numeric columns to
NumPy arrays, and reports minimum/average/maximum temperature plus average
wind speed and humidity. Matplotlib plots the first 24 records with time labels,
then writes `matrix_analysis.png` in the **current working directory**.

```sh
MPLBACKEND=Agg python3 ex1/loading.py
```

`Agg` supports image generation without a desktop display. Successful output
ends with:

```text
Generating visualization...
Analysis complete!
Results saved to: matrix_analysis.png
```

Forecast values vary, so fixed temperatures are not a guaranteed result.
The script can overwrite a prior chart with that filename. Network access is
required; a live request and chart generation were checked successfully.

## ex2 — Load settings without making service connections

[`oracle.py`](ex2/oracle.py) calls `load_dotenv()` and reads five required
environment variables. Missing or whitespace-only values are reported together
before the script exits with status 1:

| Setting | Actual use |
| --- | --- |
| `MATRIX_MODE` | Normalized and restricted to `development` or `production` |
| `DATABASE_URL` | Checked for presence; not connected or parsed |
| `API_KEY` | Checked for presence and partially masked for display |
| `LOG_LEVEL` | Displayed; not used to configure a logging framework |
| `ZION_ENDPOINT` | Displayed; no request is sent to it |

For a fresh checkout, copy the placeholder file once, then edit local values:

```sh
cp ex2/.env.example ex2/.env
python3 ex2/oracle.py
```

Keep an existing `.env` instead of replacing it. Existing process environment
variables take precedence by default, making shell-provided deployment values
usable without editing the script.

With the example's placeholders, the configuration portion prints:

```text
Configuration loaded:
  Mode: development
  Database: loaded
  API Access: rep*******
  Log Level: WARNING
  Zion Network: https://zion.example.com
```

Keys longer than five characters reveal the first three characters and mask the
rest; shorter keys are fully masked. This is display formatting, not secret
storage. The subsequent “No hardcoded secrets detected” and other security
messages are fixed text, not implemented scanning or connectivity checks.

## Technical boundaries

The exercises demonstrate environment discovery, dependency introspection,
HTTP error handling, structural validation, tabular/numeric processing, chart
generation, and configuration precedence. They do not provide a web service,
database integration, or a general secrets-management system. Environment and
configuration checks were exercised, including invalid mode; dependency and
weather output can vary with package releases and the external service.

## Resources

- [venv](https://docs.python.org/3/library/venv.html)
- [Distribution metadata](https://docs.python.org/3/library/importlib.metadata.html)
- [Open-Meteo forecast API](https://open-meteo.com/en/docs)
- [python-dotenv](https://bbc2.github.io/python-dotenv/)

## AI Usage

AI assisted documentation and checking configuration/weather examples. The
available files do not establish original implementation AI use; see the
[collection disclosure](../README.md#ai-usage).
