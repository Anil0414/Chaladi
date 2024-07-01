import pandas as pd

data ={
    'name': ['John', 'Jane', 'Jack'],
    'base_salary': [50000, 60000, 55000],
    'bonus': [5000, 6000, 5500]
}
df = pd.DataFrame(data)
print(df)
df.rename(columns={'base_salary':'salary'}, inplace=True)
df['total_salary'] = df['salary'] + df['bonus']

print(df)
