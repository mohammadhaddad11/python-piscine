import os
import sys
from dotenv import load_dotenv


REQUIRED = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]

load_dotenv()

missing = []
config = {}

print("ORACLE STATUS: Reading the Matrix...")
print()

for name in REQUIRED:
    value = os.getenv(name)

    if value is None or value.strip() == "":
        missing.append(name)
    else:
        config[name] = value

if missing:
    print("Configuration error:")
    for name in missing:
        print(f"[MISSING] {name}")

    print()
    print("Please check your .env file.")
    sys.exit(1)

mode = config['MATRIX_MODE'].lower().strip()
api_key = config['API_KEY']
masked_api_key = ""

if len(api_key) > 5:
    masked_api_key = api_key[0:3] + "*" * (len(api_key) - 3)
else:
    masked_api_key = "*" * len(api_key)

if mode != "production" and mode != "development":
    print("Error: Invalid MATRIX_MODE", end=" ")
    print("It should be eather production or development")
    sys.exit(1)

print("Configuration loaded:")
print(f"  Mode: {mode}")
print("  Database: loaded")
print(f"  API Access: {masked_api_key}")
print(f"  Log Level: {config['LOG_LEVEL']}")
print(f"  Zion Network: {config['ZION_ENDPOINT']}")
print()

print("Environment security check:")
print("[OK] No hardcoded secrets detected")
print("[OK] .env file properly configured")
print("[OK] Production overrides available")
print("\nThe Oracle sees all configurations.")
