import pandas as pd

data= {
    'Name': ['John Doe', 'Jane Smith', 'Jack Black', 'Emily Brown', 'Tom Green'],
    'age':[25, 30, 35, 28, 22],
     'City': ['New York', 'Chicago', 'Houston', 'Los Angeles', 'Boston']
}

df=pd.DataFrame(data)
#print(df)

df['SubString'] = df['Name'].apply(lambda x:  x[:4])
print(df)
