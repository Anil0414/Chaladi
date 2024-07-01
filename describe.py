import pandas as pd

file_path = r'C:\Users\Anilc\OneDrive\Desktop\Python\Data\output.csv'

df = pd.read_csv(file_path)

print(df.describe())
