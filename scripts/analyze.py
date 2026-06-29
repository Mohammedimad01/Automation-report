import pandas as pd

def analyze(df):
    summary = {
        'Total Sales':      round(df['Sales'].sum(), 2),
        'Total Profit':     round(df['Profit'].sum(), 2),
        'Avg Margin (%)':   round(df['Profit Margin'].mean() * 100, 2),
        'Total Orders':     df['Order ID'].nunique(),
        'Top Region':       df.groupby('Region')['Sales'].sum().idxmax(),
        'Top Category':     df.groupby('Category')['Profit'].sum().idxmax(),
        'Top Sub-Category': df.groupby('Sub-Category')['Sales'].sum().idxmax(),
    }

    by_region = (df.groupby('Region')
                   .agg(Sales=('Sales','sum'), Profit=('Profit','sum'))
                   .round(2).reset_index())

    by_category = (df.groupby('Category')
                     .agg(Sales=('Sales','sum'), Profit=('Profit','sum'))
                     .round(2).reset_index())

    by_month = (df.groupby(['Year','Month'])['Sales']
                  .sum().round(2).reset_index()
                  .rename(columns={'Sales':'Monthly Sales'}))

    print(f"[ANALYZE] KPIs computed. Top region: {summary['Top Region']}")
    return summary, by_region, by_category, by_month