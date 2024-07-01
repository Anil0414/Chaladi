import pandas as pd

data = {
    'Date': ['2024-01-01', '2024-01-04', '2024-01-06', '2024-01-07', '2024-01-08'],
    'Store': ['Store A', 'Store B', 'Store C', 'Store E', 'Store F'],
    'Product': ['Product 1', 'Product 4', 'Product 2', 'Product 3', 'Product 5'],
    'Sales': [100, 150, 200, 250, 50]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Pivot the DataFrame
pivot_df = df.pivot(index='Date', columns='Store', values='Sales')

print("\nPivoted DataFrame:")
print(pivot_df)
