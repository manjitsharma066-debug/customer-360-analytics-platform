import subprocess
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
SQL_FILE = ROOT_DIR / "sql" / "analytics_queries.sql"

print("=" * 70)
print(" CUSTOMER 360 ANALYTICS")
print("=" * 70)

if not SQL_FILE.exists():
    raise FileNotFoundError(f"SQL file not found: {SQL_FILE}")

try:
    result = subprocess.run(
        [
            "bq",
            "query",
            "--use_legacy_sql=false",
        ],
        stdin=open(SQL_FILE, "r"),
        text=True,
        capture_output=True,
        check=True,
    )

    print(result.stdout)
    print("=" * 70)
    print("ANALYTICS EXECUTED SUCCESSFULLY")
    print("=" * 70)

except subprocess.CalledProcessError as e:
    print("ERROR EXECUTING ANALYTICS")
    print(e.stderr)