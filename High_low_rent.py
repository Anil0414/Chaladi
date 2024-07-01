import pandas as pd

df = pd.read_csv(r'C:\Users\Anilc\OneDrive\Desktop\Python\Data\SeoulBikeData.csv', encoding='ISO-8859-1')

#print(df.head(100))

Max_rented = df['Rented Bike Count'].mean()

print(avg_bike_rented)