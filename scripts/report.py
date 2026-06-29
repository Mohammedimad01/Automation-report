import pandas as pd
from datetime import datetime

def generate_report(summary, by_region, by_category, by_month):
    date_str  = datetime.today().strftime('%Y-%m-%d')
    filename  = f"reports/Sales_Report_{date_str}.xlsx"

    with pd.ExcelWriter(filename, engine='xlsxwriter') as writer:
        wb = writer.book

        # formats
        bold   = wb.add_format({'bold': True, 'font_size': 11})
        header = wb.add_format({'bold': True, 'bg_color': '#1a7a4a',
                                'font_color': 'white', 'border': 1})
        money  = wb.add_format({'num_format': '$#,##0.00'})
        pct    = wb.add_format({'num_format': '0.00%'})

        # Sheet 1: KPI Summary
        ws1 = writer.sheets.get('KPI Summary') or wb.add_worksheet('KPI Summary')
        ws1.write('A1', 'Metric', bold)
        ws1.write('B1', 'Value', bold)
        for i, (k, v) in enumerate(summary.items(), start=1):
            ws1.write(i, 0, k)
            ws1.write(i, 1, str(v))
        ws1.set_column('A:A', 22)
        ws1.set_column('B:B', 18)

        # Sheet 2–4: Tables
        by_region.to_excel(writer,   sheet_name='By Region',   index=False)
        by_category.to_excel(writer, sheet_name='By Category', index=False)
        by_month.to_excel(writer,    sheet_name='Monthly',     index=False)

    print(f"[REPORT] Saved: {filename}")
    return filename