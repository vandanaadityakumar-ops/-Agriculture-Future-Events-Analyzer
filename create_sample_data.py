import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_sample_excel():
    # 1. Create a range of dates (Last 2 years)
    dates = pd.date_range(start='2024-01-01', periods=24, freq='MS') # Monthly Start

    data = []
    for date in dates:
        # 2. Generate realistic randomized weather
        # We'll make it slightly seasonal (hotter in middle of year)
        month = date.month
        temp = 20 + 10 * np.sin(np.pi * (month - 3) / 6) + np.random.normal(0, 2)
        rain = 50 + 40 * np.cos(np.pi * (month - 7) / 6) + np.random.normal(0, 10)
        
        # 3. Create a logic for Yield (The AI will try to find this!)
        # Yield increases with rain but decreases if it's too hot
        yield_qty = (rain * 5) + (temp * 2) + np.random.normal(0, 50)
        
        data.append({
            'Date': date,
            'Avg_Temp': round(temp, 1),
            'Rainfall_mm': round(abs(rain), 1),
            'Yield_Qty': round(abs(yield_qty), 1)
        })

    # 4. Create DataFrame and Save to Excel
    df = pd.DataFrame(data)
    df.to_excel('farm_report.xlsx', index=False)
    
    print("✅ Success! 'farm_report.xlsx' has been created.")
    print(df.head()) # Preview the first few rows

if __name__ == "__main__":
    generate_sample_excel()