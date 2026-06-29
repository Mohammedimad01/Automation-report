import pandas as pd

def clean_data(df):
    before = len(df)
    df.drop_duplicates(inplace=True)
    df.dropna(subset=['Sales', 'Order Date', 'Profit'], inplace=True)
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Ship Date']  = pd.to_datetime(df['Ship Date'])
    df['Profit Margin'] = (df['Profit'] / df['Sales']).round(4)
    df['Year']  = df['Order Date'].dt.year
    df['Month'] = df['Order Date'].dt.month
    df.to_csv("data/processed/clean_data.csv", index=False)
    print(f"[CLEAN] {before} → {len(df)} rows after cleaning")
    return df