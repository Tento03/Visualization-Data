# -*- coding: utf-8 -*-
"""Histogram

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sTPVcAWPZ4wEEOIpXQgu_qDfZYmhsZzI
"""

import matplotlib.pyplot as plt
import numpy as np

x_view=[202,121,312,514,212,723,754,846]
x_copy_view=[202,121,312,514,212,123,454,546]
y_view=[221,421,512,554,312,523,354,246]
z_view=[222,421,316,214,712,623,354,446]
bins=[100,200,300,400,500,600,700,800]
days=range(1,9)

plt.figure(figsize=(10,4))
plt.hist(x_view,bins,label='X')
plt.xlabel('Hari')
plt.ylabel('Angka')
plt.legend(loc='upper left')
plt.title('Learning Matplotlib')
plt.grid()
plt.show()


