import pandas as pd

df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value1': [1, 2, 3]})
df2 = pd.DataFrame({'key': ['B', 'C', 'D'], 'value2': [4, 5, 6]})

inner_join = pd.merge(df1, df2, on='key', how='inner')
print(df1,df2)
print(inner_join)
