import pandas as pd

df = pd.read_csv(r'C:\Users\Anilc\OneDrive\Desktop\Python\Data\SeoulBikeData.csv', encoding='ISO-8859-1')

df = pd.DataFrame(df)


df['Date'] = pd.to_datetime(df['Date'],format='%d/%m/%Y')


df['Month'] = df['Date'].dt.month

mon_rent = df.groupby('Month')['Rented Bike Count'].sum().reset_index()

max_rentals_month = mon_rent.loc[mon_rent['Rented Bike Count'].idxmax()]
min_rentals_month = mon_rent.loc[mon_rent['Rented Bike Count'].idxmin()]


print("\nMonth with the highest number of rentals:",min_rentals_month )
print("\nMonth with the lowest number of rentals:", max_rentals_month)

