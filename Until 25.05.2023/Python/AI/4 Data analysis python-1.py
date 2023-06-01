import numpy as np
import pandas as pd

pd.set_option("display.precision",2)

df= pd.read_csv('test.csv')
df.head
print(df.shape)
(3333,20)

'''print(df.columns)
print(df.info)'''
'''df.describe
df.describe(include=['object','bool'])'''

#df['test'].value_counts()

#df.sort_values(by='Total day charge', ascending=False).head()
'''df.sort_values(by=['',''],
               ascending=[True,False]).head()'''

# df['test'].mean()


