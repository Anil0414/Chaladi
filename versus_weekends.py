import pandas as pd

df = pd.read_csv(r'C:\Users\Anilc\OneDrive\Desktop\Python\Data\SeoulBikeData.csv', encoding='ISO-8859-1')

df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')

df['Day of Week'] = df['Date'].dt.dayofweek

df['Weekday/Weekend'] = df['Day of Week'].apply(lambda x: 'Weekday' if x < 5 else 'Weekend')

rentals_weekday_weekend = df.groupby('Weekday/Weekend')['Rented Bike Count'].sum().reset_index()
print("\nRentals during Weekdays versus Weekends:")
print(rentals_weekday_weekend)
print(df.head())