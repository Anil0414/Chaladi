import pandas as pd
import numpy as np

data = {
    'ID': [1, 2, 3, 4, 5],
    'Age': [25, np.nan, 35, np.nan, 40],
    'Salary': [50000, 60000, np.nan, np.nan, 80000]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

mean_age = df['Age'].mean()

df_filled['Age'].fillna(mean_age, inplace=False)

print("\nDataFrame after filling missing values in 'Age' column (inplace=False):")
print(df_filled)

print("\nOriginal DataFrame (unchanged):")
print(df)
