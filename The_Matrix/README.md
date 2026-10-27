*42 curriculum exercises. The dependency manifest identifies mhaddad.*

# The Matrix

## Description

Three exercises cover virtual-environment discovery, dependency management and
data analysis, then environment-based configuration. The weather example fetches
Irbid forecasts, computes statistics, and writes a temperature chart.

## Instructions

Python 3.10+ is declared by ex1; publication checks used Python 3.14.8.
Use an isolated environment and run from this directory:

```sh
python3 -m pip install -r ex1/requirements.txt -r ex2/requirements.txt
python3 ex0/construct.py
MPLBACKEND=Agg python3 ex1/loading.py
cp ex2/.env.example ex2/.env
python3 ex2/oracle.py
```

The copied environment file contains placeholders. Set your own local values
without committing the file. The example does not connect to the configured
database or Zion endpoint; it validates and displays configuration status.
Ex1 also includes Poetry metadata with `package-mode=false` for environment
management rather than packaging an application.

## Technical Implementation

| Exercise | Components |
| --- | --- |
| ex0 | Compare `sys.prefix`/`sys.base_prefix`, show interpreter/environment and installation paths |
| ex1 | Discover dependencies, query installed versions, fetch Open-Meteo JSON, validate equal-length hourly arrays, create a pandas DataFrame, compute NumPy statistics, plot with Matplotlib |
| ex2 | `python-dotenv`, five required settings, development/production mode validation, API-key masking |

Weather dependencies are pandas, NumPy, requests, and Matplotlib. The separate,
remote-preserved ex2 requirements file supplies `python-dotenv`. The source's
version-discovery update uses distribution metadata instead of assuming each
module exposes `__version__`.

## Design Decisions and Output

The request targets a three-day hourly forecast, includes a ten-second timeout,
and handles request/JSON failures before analysis. The validator checks structure
and array lengths, not every numeric value. The chart uses the first 24 records
and writes **`matrix_analysis.png` in the current working directory**, replacing
an existing file with that name.

`load_dotenv()` discovers an environment file; existing process variables take
precedence by default. Required keys are `MATRIX_MODE`, `DATABASE_URL`, `API_KEY`,
`LOG_LEVEL`, and `ZION_ENDPOINT`. The printed hardcoded-secrets message is a fixed
status string, not a security scanner. API-key output can reveal its first
three characters; avoid capturing real credentials in examples.

## Verification

All modules passed syntax checks. Environment detection ran successfully;
configuration checks covered valid values, missing variables, and invalid mode.
On 2026-10-27 the live Open-Meteo request succeeded with 72 hourly records and
produced a chart using a headless backend. Network availability and future
dependency compatibility are external conditions, not guaranteed features.

## Resources

- [Python venv](https://docs.python.org/3/library/venv.html).
- [Distribution metadata](https://docs.python.org/3/library/importlib.metadata.html).
- [Open-Meteo](https://open-meteo.com/en/docs).
- [python-dotenv](https://bbc2.github.io/python-dotenv/).

## AI Usage

AI assisted source/dependency comparison, documentation, and configuration/live
weather checks for publication. Original implementation assistance is not
established; see the [collection disclosure](../README.md#ai-usage).
