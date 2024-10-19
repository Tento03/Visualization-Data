import matplotlib.pyplot as plt
import numpy as np

view=[202,121,312,514,212,123,454,546]
days=range(1,9)
print(len(view))

plt.figure(figsize=(10,4))
plt.plot(days,view,label='Random Number',color='blue',marker='o',markerfacecolor='red',linestyle=':',linewidth=4)
plt.xlabel('Hari')
plt.ylabel('Angka')
plt.legend()
plt.show()

