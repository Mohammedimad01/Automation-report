import pandas as pd
import os

def load_data(path="data/raw/Sample - Superstore.csv"):
    if not os.path.exists(path):
        raise FileNotFoundError(f"No file found at {path}")
    
    df = pd.read_csv(path, encoding='latin-1')
    print(f"[INGEST] Loaded {len(df)} rows, {len(df.columns)} columns")
    return df