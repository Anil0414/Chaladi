import pandas as pd

# Example DataFrame
data = {
    'date': pd.date_range(start='2024-01-01', periods=10, freq='D'),
    'value': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
}
df = pd.DataFrame(data)

# Calculate the rolling mean with a window of 3
df['rolling_mean'] = df['value'].rolling(window=4).mean()

print(df)
