import pandas as pd

def prepare_data(file):
    df = pd.read_excel(file)

    df = df.dropna(subset=['Avg_Temp', 'Rainfall_mm', 'Yield_Qty'])

    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
        df = df.sort_values('Date')

    df['Efficiency'] = df['Yield_Qty'] / (df['Rainfall_mm'] + 1)

    return df

def get_summary_stats(df):
    stats = {
        "Total Yield": df['Yield_Qty'].sum(),
        "Avg Temp": df['Avg_Temp'].mean(),
        "Max Rain": df['Rainfall_mm'].max()
    }
    return stats
