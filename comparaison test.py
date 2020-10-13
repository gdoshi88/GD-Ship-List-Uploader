# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 15:51:17 2018

@author: tastetf
"""

import pandas as pd

df1 = pd.read_excel('Prelim Ship List - 041618.xlsx')
df2 = pd.read_excel('Ship List - 041618.xlsx')

difference = df1[df1!=df2]
print (difference)