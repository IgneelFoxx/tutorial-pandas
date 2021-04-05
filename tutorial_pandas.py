#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 16:55:43 2021
Tutorial de pandas para la manipulación de datos.
@author: IgneelFoxx
"""

import pandas as pd
import matplotlib.pyplot as plt

#lectura del archivo
data= pd.read_csv('car.data', header= None) #header= None, indica que no tiene
             #una primera fila que indique que significa cada uno de los datos

"""
CAR car acceptability
. PRICE overall price
. . buying buying price
. . maint price of the maintenance
. TECH technical characteristics
. . COMFORT comfort
. . . doors number of doors
. . . persons capacity in terms of persons to carry
. . . lug_boot the size of luggage boot
. . safety estimated safety of the car

Class Values:

unacc, acc, good, vgood

Attributes:

buying: vhigh, high, med, low.
maint: vhigh, high, med, low.
doors: 2, 3, 4, 5more.
persons: 2, 4, more.
lug_boot: small, med, big.
safety: low, med, high.
"""

data.columns= ['Price','Maintenence Cost','Doors Numbers','Capacity',
               'Size','Safety','Decision']

print("Data Shape: ",data.shape)
print("Total de datos: ",data.size)

#Podemos obtener información de una columna en especifico
data['Decision'].value_counts()
# Out[19]: 
# unacc    1210
# acc       384
# good       69
# vgood      65
# Name: Decision, dtype: int64

#podemos incluso gráficar datos, para observar de mejor forma el comportamiento
decision= data['Decision'].value_counts()
# decision.plot(kind= 'bar')
# plt.show()

#Podemos conocer cuales son los paramatros que contiene una columna
print("array:", data['Price'].unique())

#Podemos remplazar incluso la información que contiene una tabla, esto es útil
data['Price'].replace(('vhigh','high','med','low'),(4,3,2,1), 
                             inplace= True)
print("array:", data['Price'].unique())

#hagamos una gráfica "detallada"
price= data['Price'].value_counts()
colors= ['yellow','red','blue','green']
# price.plot(kind= 'bar', color= colors)
# plt.xlabel("Precio")
# plt.ylabel("Cars")
# plt.title("Precio de carros")
# plt.show()

#Tambien podemos gráficar un pastel
safety= data['Safety'].value_counts()
labels= ['low', 'med', 'high']
size= [576,576,576]
explode= [0.01,0.01,0.01] #Para dejar espacios entre el pastel
plt.pie(size,labels= labels, colors= colors, explode= explode, shadow= True,
        autopct= '%.2f%%')
plt.title("Niveles de seguridad", fontsize= 10)
plt.axis('off')
plt.legend(loc= 'best')
plt.show()