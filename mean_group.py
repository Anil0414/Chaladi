import pandas as pd

# Sample data for DataFrame1
data1 = {
    'ID': [1, 2, 3, 4],
    'Name': ['John', 'Jane', 'Jack', 'Jill']
}
df1 = pd.DataFrame(data1)

# Sample data for DataFrame2
data2 = {
    'ID': [2, 3, 4, 5],
    'Age': [25, 30, 35, 40]
}
df2 = pd.DataFrame(data2)

# Inner join based on 'ID' column
merged_inner = pd.merge(df1, df2, on='ID', how='inner')

print("Inner join result:")
print(merged_inner)
