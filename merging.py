import pandas as pd

# Sample data for DataFrame1
data1 = {
    'ID': [1, 2, 3,4,5],
    'Name': ['John', 'Jane', 'Jack','Anil','Ganesh']
}
df1 = pd.DataFrame(data1)
print(df1)
# Sample data for DataFrame2
data2 = {
    'ID': [4, 5,3],
    'Name': ['Jill', 'Jake','Anil']
}
df2 = pd.DataFrame(data2)
print(df2)
# Concatenate vertically
concatenated_df = pd.concat([df1, df2], axis=2)

print("Concatenated DataFrame:")
print(concatenated_df)
