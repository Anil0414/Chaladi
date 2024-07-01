    import pandas as pd

    df = pd.read_csv(r'C:\Users\Anilc\OneDrive\Desktop\Python\Data\SeoulBikeData.csv', encoding='ISO-8859-1')
    #print(df)
    print("Original DataFrame:")
    correlation = df['Temperature(°C)'].corr(df['Rented Bike Count'])
    print(f"\nCorrelation between Temperature and Rented Bike Count: {correlation:.2f}")