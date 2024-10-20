# -*- coding: utf-8 -*-
"""Bar Plot

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sTPVcAWPZ4wEEOIpXQgu_qDfZYmhsZzI
"""

import matplotlib.pyplot as plt
import numpy as np

x_view=[202,121,312,514,212,123,454,546]
x_copy_view=[202,121,312,514,212,123,454,546]
y_view=[221,421,512,554,312,523,354,246]
z_view=[222,421,316,214,712,623,354,446]
days=range(1,9)

plt.figure(figsize=(10,4))
plt.bar(days,x_view,label='X',color='green')
plt.xlabel('Hari')
plt.ylabel('Angka')
plt.legend(loc='upper left')
plt.title('Learning Matplotlib')
plt.show()

plt.figure(figsize=(10,4))
plt.bar(days,y_view,label='Y',color='blue')
plt.xlabel('Hari')
plt.ylabel('Angka')
plt.legend(loc='upper left')
plt.title('Learning Matplotlib')
plt.show()

plt.figure(figsize=(10,4))
plt.bar(days,z_view,label='Z',color='orange')
plt.xlabel('Hari')
plt.ylabel('Angka')
plt.legend(loc='upper left')
plt.title('Learning Matplotlib')
plt.show()

plt.figure(figsize=(10,4))
plt.bar([a- 0.25 for a in days],x_view,label='X',color='green',width=0.25,align='edge')
plt.bar([a+ 0.25 for a in days],y_view,label='X Copy',color='blue',width=-0.25,align='edge')
plt.xlabel('Hari')
plt.ylabel('Angka')
plt.xticks(days)
plt.title('Learning Matplotlib')
plt.show()

