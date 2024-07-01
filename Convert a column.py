import pandas as pd

# Sample data with date strings in 'DD-MM-YYYY' format
data = {
    'Date': ['01-01-2024', '02-01-2024', '03-01-2024', '04-01-2024', '05-01-2024'],
    'Value': [10, 20, 15, 25, 30]
}
df = pd.DataFrame(data)

df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')


df.set_index('Date', inplace=True)

print("DataFrame with datetime index:")
print(df)
# Pivot the DataFrame
pivot_df = df.pivot(index='Date', columns='Store', values='Sales')

print("Pivoted DataFrame:")
print(pivot_df)
