import pandas as pd

file_path = r'C:\Users\Anilc\OneDrive\Desktop\Python\Data\Excel_Sample.xlsx'

df = pd.read_excel(file_path)

print(df.head(4))
