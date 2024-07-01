import pandas as pd

# Sample data for DataFrame1
data1 = {
    'ID': [1, 2, 3],
    'Name': ['John', 'Jane', 'Jack']
}
df1 = pd.DataFrame(data1)

# Sample data for DataFrame2
data2 = {
    'ID': [4, 5],
    'Name': ['Jill', 'Jake']
}
df2 = pd.DataFrame(data2)

# Concatenate vertically
concatenated_df = pd.concat([df1, df2], axis=0)

print("Concatenated DataFrame:")
print(concatenated_df)
