import numpy as np
# Create a 4x4 matrix with values ​​from 1 to 16.

print(np.arange(1,17).reshape(4,4), '\n')

# Create a DataFrame that generates 4x3 random numbers

from numpy.random import randn
import pandas as pd
data_frame = pd.DataFrame(data = 10*randn(4,3), 
index = ['row1','row2','row3','row4'], 
columns = ['Columns1','Columns2','Columns3'])

print(data_frame,'\n')


# Arr=np.array([[50,12,np.nan,16],[np.nan, np.nan,80,70],[93,np.nan,16,np.nan]]) values convert array to DataFrame. Apply what can be done about missing values
Arr=np.array([[50,12,np.nan,16],[np.nan, np.nan,80,70],[93,np.nan,16,np.nan]]) 
data_frame1 = pd.DataFrame(Arr)
avg=data_frame1.mean()
data_frame1.fillna(avg, inplace=True)
print(data_frame1)


