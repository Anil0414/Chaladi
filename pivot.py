import pandas as pd

data ={
    'Name':['Anil','Ganesh', 'Uday'],
     'Age' : (23,34,45,),
    'Location' : ['BLR','Pune','HYD']
    }
df=pd.DataFrame(data)
print(df)

pivot = pd.pivot(df,values='Name',index=['Location'],columns=['Age'])
print(pivot)