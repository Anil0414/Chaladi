import pandas as pd

Data1 = {
    'Name': ['Anil','Kumar','Ganesh'],
    'Age' : [23,34,34,]
}
df=pd.DataFrame(Data1)
#print(df)

Date2 = {
    'Name': ['Uday','Kumar','Ganesh'],
    'Age' : [23,34,34,]
}
df2=pd.DataFrame(Date2)
#print(df2)

Merge = pd.merge(df,df2,on='Age',how='outer')
print(Merge)