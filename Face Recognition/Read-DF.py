# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 12:52:16 2022

@author: aakaa
"""

import pandas as pd
import numpy as np

df=pd.read_csv('Data.csv')
df.head()
x=df['Encodings'][0].split(',')
x=np.array(x)
x=x.astype(np.float)