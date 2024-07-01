import pandas as pd


df1 = pd.read_excel(r'C:\Users\Anilc\OneDrive\Desktop\Python\Data\Excel_Sample.xlsx', sheet_name='Sheet1')

print("DataFrame from Excel:")
print(df1)

df1.to_excel('Excel_Sample_Output.xlsx', sheet_name='Sheet1', index=False)
