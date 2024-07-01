import pandas as pd

df = pd.read_csv(r'C:\Users\Anilc\OneDrive\Desktop\Python\Data\SeoulBikeData.csv', encoding='ISO-8859-1')
#print(df)

hourly_rentals = df.groupby('Hour')['Rented Bike Count'].sum().reset_index()

max_rentals_hour = hourly_rentals.loc[hourly_rentals['Rented Bike Count'].idxmax()]
min_rentals_hour = hourly_rentals.loc[hourly_rentals['Rented Bike Count'].idxmin()]

print(f'The hour with the highest number of rentals is {max_rentals_hour["Hour"]} with {max_rentals_hour["Rented Bike Count"]} rentals.')
print(f'The hour with the lowest number of rentals is {min_rentals_hour["Hour"]} with {min_rentals_hour["Rented Bike Count"]} rentals.')