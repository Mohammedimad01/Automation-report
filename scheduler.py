import schedule, time
from scripts.ingest  import load_data
from scripts.clean   import clean_data
from scripts.analyze import analyze
from scripts.report  import generate_report

def run_full_pipeline():
    print("Running scheduled pipeline...")
    df = load_data()
    df = clean_data(df)
    summary, r, c, m = analyze(df)
    generate_report(summary, r, c, m)

# Run every Monday at 8:20 PM
schedule.every().monday.at("20:20").do(run_full_pipeline)

print("Scheduler running. Press Ctrl+C to stop.")
while True:
    schedule.run_pending()
    time.sleep(60)