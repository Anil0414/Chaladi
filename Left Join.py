import pandas as pd

# Creating example DataFrames
df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value1': [1, 2, 3]})
df2 = pd.DataFrame({'key': ['B', 'C', 'D'], 'value2': [4, 5, 6]})

# Inner Join
inner_join = pd.merge(df1, df2, on='key', how='inner')
print("Inner Join:\n", inner_join)

# Outer Join
outer_join = pd.merge(df1, df2, on='key', how='outer')
print("\nOuter Join:\n", outer_join)

# Left Join
left_join = pd.merge(df1, df2, on='key', how='left')
print("\nLeft Join:\n", left_join)

# Right Join
right_join = pd.merge(df1, df2, on='key', how='right')
print("\nRight Join:\n", right_join)
