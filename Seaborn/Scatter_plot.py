# -*- coding: utf-8 -*-
"""Scatter Plot

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

sns.scatterplot(x="sepal_length",y="sepal_width",data=iris,hue='species')

sns.scatterplot(x='tip',y='total_bill',data=tips,hue='day',size='size',palette='YlGnBu')
