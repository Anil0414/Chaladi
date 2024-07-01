import pandas as pd

df = pd.read_csv(r'C:\Users\Anilc\OneDrive\Desktop\Python\Data\SeoulBikeData.csv', encoding='ISO-8859-1')

df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')

df['Month'] = df['Date'].dt.month
average_monthly_stats = df.groupby('Month').agg({
    'Temperature(°C)': 'mean',
    'Humidity(%)': 'mean',
    'Wind speed (m/s)': 'mean'
}).reset_index()

print(average_monthly_stats)