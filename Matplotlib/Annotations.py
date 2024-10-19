# -*- coding: utf-8 -*-
"""Annotations

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sTPVcAWPZ4wEEOIpXQgu_qDfZYmhsZzI
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x_view=[202,121,312,514]
label=['Naruto','Luffy','Boruto','Xin']
anime=['Naruto','Luffy','Boruto','Xin','Naruto','Naruto','Naruto','Luffy','Boruto','Boruto','Xin']
anime_Frame=pd.DataFrame(anime,columns=['Char'])
char=anime_Frame['Char'].value_counts()

x_copy_view=[202,121,312,514,212,123,454,546]
y_view=[221,421,112,554,312,523,354,246]
z_view=[222,421,316,214,712,623,354,446]
bins=[100,200,300,400,500,600,700,800]
days=range(1,9)

min_y=min(y_view)
days_co=days[y_view.index(min_y)]
plt.plot(days,y_view,label='Y')
plt.grid()
plt.xlabel('Day')
plt.ylabel('View')
plt.legend()
plt.annotate('Lowest Value',xy=(days_co,min_y),xytext=(2,112),arrowprops=dict(facecolor='black',shrink=0.05))
plt.show()

