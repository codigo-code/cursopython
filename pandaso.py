# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 20:45:55 2019

@author: dante.panella
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import interpolate as inter

data = pd.read_csv('VC.txt',header=1,delim_whitespace=True)


#acomodo X
x = data.iloc[:,0]
y = data.iloc[:,1]

print(x)
print(y)

plt.plot(x,y,'ro')
plt.xlabel('Carreras')
plt.ylabel('Turnos')

f= inter.interp1d(x,y,1)
print (f(337))


coeficientes = np.polyfit(x,y,1) # coeficientes
polinomio = np.poly1d(coeficientes) #polinomios
print('Coeficientes ' , coeficientes) #coeficientes
print('polinomios ' , polinomio) #ajuste
ys= polinomio(x)
plt.plot(x,ys,1)
plt.show()