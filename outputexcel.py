import pandas as pd

data = {
    'Name':['Anil','Ganesh','Uday'],
    'age' :[33,34,55],
    'location':['BLR','HYD','Pune']
}
df=pd.DataFrame(data)
print(df)

df.to_excel('output2024.xlsx')

print('Scuesfflly comeplted output')