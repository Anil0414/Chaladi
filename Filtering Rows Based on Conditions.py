import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'New York', 'Chicago'],
    'Score': [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

age_condition = df[df['Age'] > 25]
print("\nRows where Age is greater than 25:")
print(age_condition)

