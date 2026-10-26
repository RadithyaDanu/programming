import pandas as pd

df = pd.read_csv('data.csv')

df['date'] = pd.to_datetime(df['date'])

print(df.period_range("2026-06-01", "1381-06-30", freq="M"))
