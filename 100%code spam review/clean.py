# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 14:12:13 2023

@author: COMPUTER
"""

import pandas as pd
import numpy as np
#reading dataset
df=pd.read_csv('E:/project 2023/spam review detection/spam.csv',encoding='latin-1')
#checking size of dataframe
df.shape
df.head(5)
df.info()
#dropping un necessary columns
df.drop(columns=['Unnamed: 2','Unnamed: 3','Unnamed: 4'],inplace=True)
#renaming the columns
df.rename(columns={'lable':'target','text':'text'},inplace=True)
df.head(2)
df.to_csv("spam1.csv")
