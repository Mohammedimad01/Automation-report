# Automation-report

> An end-to-end automated sales reporting pipeline built in Python — replacing hours of manual Excel work with a single-command execution and a weekly scheduler.

---

## Overview

This project replicates a real-world data analyst workflow: raw business data comes in, gets cleaned and analyzed, and a formatted Excel report is produced — automatically, on a schedule.

Inspired by work done during a Data Analyst internship, where Python automation reduced report preparation time by ~70% and saved approximately 8 hours per week.

---

## Pipeline Architecture

```
data/raw/superstore.csv
        │
        ▼
  [01] ingest.py       →   Load raw CSV (9,994 rows)
        │
        ▼
  [02] clean.py        →   Deduplicate, fix types, engineer features
        │
        ▼
  [03] analyze.py      →   Compute KPIs + 4 aggregation tables
        │
        ▼
  [04] report.py       →   Generate dated multi-sheet Excel report
        │
        ▼
  reports/Sales_Report_YYYY-MM-DD.xlsx
```

---

## Features

- **Automated ingestion** — loads raw CSV with encoding handling and row validation
- **Data cleaning** — removes duplicates, fixes date formats, drops nulls, engineers profit margin
- **KPI computation** — total sales, total profit, average margin, top region, top category
- **Multi-sheet Excel output** — KPI Summary, By Region, By Category, Monthly Trend
- **Scheduled execution** — runs automatically every Monday at 8:00 AM via `schedule`
- **Single-command pipeline** — `python run_pipeline.py` triggers the entire flow

---

## Project Structure

```
Automation-report/
│
├── data/
│   ├── raw/                  ← Raw CSV input (gitignored)
│   └── processed/            ← Cleaned output (gitignored)
│
├── reports/                  ← Generated Excel reports (gitignored)
│
├── scripts/
│   ├── __init__.py
│   ├── ingest.py             ← Data loading
│   ├── clean.py              ← Cleaning & feature engineering
│   ├── analyze.py            ← KPI & aggregation logic
│   └── report.py             ← Excel report generation
│
├── run_pipeline.py           ← Master script (run this)
├── scheduler.py              ← Weekly automation trigger
├── .gitignore
└── README.md
```

---

## Tech Stack

| Tool | Purpose |
|---|---|
| `pandas` | Data ingestion, cleaning, and aggregation |
| `xlsxwriter` | Excel report generation with custom formatting |
| `openpyxl` | Excel file reading and compatibility |
| `schedule` | Lightweight Python job scheduler |

---

## License

MIT License — free to use, modify, and distribute.
