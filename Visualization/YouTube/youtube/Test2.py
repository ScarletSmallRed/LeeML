import pandas as pd
import numpy as np

df = pd.DataFrame({"Name":["Alice", "Bob", "Mallory", "Mallory", "Bob" , "Mallory"],"City": ["Seattle", "Seattle", "Portland", "Seattle", "Seattle", "Portland"], "Val":[4,3,3,np.nan,np.nan,6]})
print(df)
print(df.groupby('Name')['Val'].count())
print(df.groupby('Name')['Val'].sum())
print('*' * 100)
print(df.groupby('City')['Val'].count())
print(df.groupby('City')['Val'].sum())
