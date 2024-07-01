import pandas as pd

file_path = r'C:\Users\Anilc\OneDrive\Desktop\Python\Data\SeoulBikeData.csv'

df = pd.read_csv(file_path, encoding='ISO-8859-1')

print(df)

