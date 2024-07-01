import pandas as pd

data = {
    'age': [34, 35, 22, 34, 21, 23, 67, 45, 34]
}

df = pd.DataFrame(data)
print(df)

Greater =df.age>35
print(df)