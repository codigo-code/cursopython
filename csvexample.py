# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 07:34:54 2019

@author: dante.panella
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import interpolate as inter

#tomado el primer encabezado en al primera fila
data = pd.read_csv('archivo2.csv',header=0)

print(data)
print(data['Cable']) # solo cable

print(data.iloc[0:3]) # muestro las 3 primeras columnas

print(data.sort_values(by='telefonos')) # %segun telefono

print('< 10% con telefono')
print(data[data.iloc[:,5]<10]) # hasta el 10% q usaben el telefono reduccion de hogares con telefonos

ano = data['Año']
compu = data['Computadora']


plt.xlabel('Computadora')
plt.ylabel('año')



plt.plot(ano,compu)

#tel = data['telefonos'] # solo extraje telefonos
#ano = data['Año']

#resTel =tel[tel>10]
 
#imprimo dos columnas
#for c1,c2 in zip(resTel,ano):
#     print (c1, c2)