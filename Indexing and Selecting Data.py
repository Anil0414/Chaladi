import pandas as pd

data ={
    'name' : ['John','Jane','Jack'],
    'age' : [21,22,33],
    'city': ['New York','Chicago','Houston']
}
df = pd.DataFrame(data)
#print(df)
#age_column = df['age']
#print(age_column)
age_column1 = df.age
print(age_column1)