import pandas as pd
# Sample data with two datetime columns
data = {
    'Start_Date': ['2024-01-01', '2024-04-15', '2024-06-25', '2024-07-07', '2024-08-08'],
    'End_Date': ['2024-01-10', '2024-04-20', '2024-07-01', '2024-07-10', '2024-08-15'],
    'Event': ['Event 1', 'Event 2', 'Event 3', 'Event 4', 'Event 5']
}
df = pd.DataFrame(data)

# Convert 'Start_Date' and 'End_Date' columns to datetime
df['Start_Date'] = pd.to_datetime(df['Start_Date'])
df['End_Date'] = pd.to_datetime(df['End_Date'])

# Calculate the time difference in days
df['Time_Difference'] = (df['End_Date'] - df['Start_Date']).dt.days

print("\nDataFrame with time difference:")
print(df)
