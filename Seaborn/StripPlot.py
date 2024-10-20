# -*- coding: utf-8 -*-
"""StripPlot

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sTPVcAWPZ4wEEOIpXQgu_qDfZYmhsZzI
"""

import seaborn as sns

sns.get_dataset_names()

iris=sns.load_dataset('iris')
tips=sns.load_dataset('tips')
iris

tips

import pandas as pd

x_view=[202,121,312,514,202,121,121]
anime=['Naruto','Luffy','Boruto','Xin','Naruto','Naruto','Naruto','Luffy','Boruto','Boruto','Xin']
anime_Frame=pd.DataFrame(anime,columns=['Char'])
char=anime_Frame['Char'].value_counts()

sns.stripplot(x='sex',y='total_bill',data=tips,hue='day')

sns.stripplot(x='day',y='tip',data=tips,hue='sex')

