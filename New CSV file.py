import numpy as np
import pandas as pd

df = pd.read_csv('colors.json')
dfnew=df
dfnew.to_csv('example1',index=False)