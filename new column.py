import pandas as pd

Data = {
    'Name' : ['Anil','Ganesh','Kumar'],
    'age' : [21,22,33],
    }
df = pd.DataFrame(Data)


df['Name Length'] = df ['Name'].apply(lambda  x: len(x))
print(df)