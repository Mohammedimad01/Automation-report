import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from scripts.ingest  import load_data
from scripts.clean   import clean_data
from scripts.analyze import analyze
from scripts.report  import generate_report

print("=" * 45)
print("  AUTOMATION-REPORT — PIPELINE STARTING")
print("=" * 45)

df                                     = load_data()
df                                     = clean_data(df)
summary, by_region, by_cat, by_month   = analyze(df)
report_path                            = generate_report(summary, by_region, by_cat, by_month)

print("=" * 45)
print(f"  ✅  Pipeline complete. Report → {report_path}")
print("=" * 45)