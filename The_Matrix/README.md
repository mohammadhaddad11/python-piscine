*42 curriculum exercises · mhaddad*

# The Matrix

Virtual environments, Python dependencies, live weather analysis, and environment-based configuration.

## Description

| Exercise | Focus |
| --- | --- |
| `ex0` | Virtual-environment detection and interpreter paths |
| `ex1` | Open-Meteo request, pandas/NumPy analysis, Matplotlib plot |
| `ex2` | dotenv configuration and required-setting checks |

## Instructions

Requirements: Python 3.10+ and dependencies listed below. Run from this directory:

```sh
python3 -m pip install -r ex1/requirements.txt -r ex2/requirements.txt
python3 ex0/construct.py
MPLBACKEND=Agg python3 ex1/loading.py
cp ex2/.env.example ex2/.env
python3 ex2/oracle.py
```

## Technical Notes

Run in a virtual environment. Set local values in `ex2/.env` and never commit secrets. Copy the example only if you do not already have an environment file. Existing process variables take precedence by default. The configuration exercise checks settings but does **not** connect to the displayed database or endpoint. Its hardcoded-secrets status message is fixed text, not a scanner; API-key masking can still expose the first three characters.

The weather example fetches a three-day forecast, analyzes hourly temperatures, and writes `matrix_analysis.png` in the working directory. Network access is required; that output file may be overwritten.

## Resources

- [venv](https://docs.python.org/3/library/venv.html) · [Open-Meteo](https://open-meteo.com/en/docs) · [python-dotenv](https://bbc2.github.io/python-dotenv/)
- [Distribution metadata](https://docs.python.org/3/library/importlib.metadata.html)

## AI Usage

AI assistance supported documentation and verification during portfolio publication. See the [collection's AI usage note](../README.md#ai-usage).
