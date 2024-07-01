import pandas as pd

Data = {
    'Date' :['06-25-2024','06-20-2024','06-11-2024','06-26-2024',],
    'Event':['Event1','Event2','Event3','Event4']
    }
df=pd.DataFrame(Data)
print(df)

df['Date']=pd.to_datetime(df['Date'])
print(df)
df['Day']=df['Date'].dt.day
df['Month']=df['Date'].dt.month
df['Year']=df['Date'].dt.year
print("DataFrame with extracted day, month, and year:")
print(df)