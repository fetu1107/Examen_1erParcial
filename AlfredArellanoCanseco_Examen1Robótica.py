#!/usr/bin/env python
# coding: utf-8

# # Diseña un programa que identifique 
# 
# - enteros
# - reales (10.0 15.0 0.0 ...) reales inválidos (.0 . 0.)
# - identificadores (hola, hola234, ...)
# - operador de adicción (+)
# - operador de sustracción (-)
# 
# 
# entrada ="678.32 1234 hola mundo234 34 + -"
# 
# Salida:
# ```
# ['real', '678.32']
# ['Entero', '1234']
# ['Id', 'hola']
# ['Id', 'mundo234']
# ['Entero', '34']
# ['Op +', '+']
# ['Op -', '-']
# ['Fin de Archivo', '$']
# ```
# 
# 
# entrada ="678.32 + 1234-hola+muNdO234-34 + -"
# 
# Salida:
# ```
# ['real', '678.32']
# ['Op +', '+']
# ['Entero', '1234']
# ['Op -', '-']
# ['Id', 'hola']
# ['Op +', '+']
# ['Id', 'muNdO234']
# ['Op -', '-']
# ['Entero', '34']
# ['Op +', '+']
# ['Op -', '-']
# ['Fin de Archivo', '$']
# ```
# 
# entrada ="12 .34 1. @ % 1234.532 1234123.41234  1.1+0.0-10.3 hola mundo1234 como2143 estas1234 "
# 
# Salida:
# ```
# ['Entero', '12']
# ['Error', '.']
# ['Entero', '34']
# ['Error', '1. ']
# ['Error', '@']
# ['Error', '%']
# ['real', '1234.532']
# ['real', '1234123.41234']
# ['real', '1.1']
# ['Op +', '+']
# ['real', '0.0']
# ['Op -', '-']
# ['real', '10.3']
# ['Id', 'hola']
# ['Id', 'mundo1234']
# ['Id', 'como2143']
# ['Id', 'estas1234']
# ['Fin de Archivo', '$']
# ```

# In[3]:


ord_1=[]
letras=""
op=""
error=""
reales=""
def conver(texto):
    for i in range(len(texto)):
           ord_1.append(ord(texto[i])) 
           

        
entrada=input("escribe tu mama:")
x=len(entrada)
print(x,type(x))
conver(entrada)
print(ord_1)

bandera=1

for i in range(x):

        
    if ord_1[i] >= 48 and ord_1[i] <= 57:
        reales+=(chr(ord_1[i]))
    
    elif (ord_1[i] >= 97 and ord_1[i] <= 122) or (ord_1[i] >= 65 and ord_1[i] <= 90) :
        letras+=(chr(ord_1[i])) 

    elif ord_1[i] == 43:
        print("'Op +' ," ,chr(ord_1[i])) 
       
    elif ord_1[i] == 45:#-    
        print("'Op -' ," ,chr(ord_1[i])) 

    else:
        print("'Error' ,",chr(ord_1[i]))   
    
    if ord_1[i]==32 or i==(x-1):
        print("'reales' ," ,reales)      
        print("'letras' ,",letras)
        reales=""
        letras=""  
    
    
    
    
    
print("'Fin del archivo' ,","$")


# In[5]:


entrada ="678.32 + 1234-hola+muNdO234-34 + -"


# # Grafica la siguiente función 
# 
# $$f(x) = \sin(e^x) - \cos(x)$$

# In[2]:


get_ipython().run_line_magic('matplotlib', 'notebook')
import matplotlib.pyplot as plt
from sympy import *
init_printing()


x = var("x")
f = sin(exp(x))-cos(x)
f


# In[5]:


plot(f)


# # Utilizando sympy 
# 
# Dos números suman 25 y el doble de uno de ellos es 14. ¿Qué números son?

# In[20]:


import sympy as sp
# x+y = 25
# 2x=14
x1, x2 = var("x1 x2")

eq_0=sp.Eq(2*x1,14)
eq_1=sp.Eq(x1+x2,25)

ans=sp.solve((eq_0,eq_1), (x1, x2))
ans


# In[38]:


x1, x2 = var("x1 x2")

eq_0=Eq(2*x1,14)
eq_1=Eq(x1+x2,25)

x1_1=solve(eq_0,x1)

f=eq_1.subs(x1,x1_1[0])
print(f)

x2_1=solve(f,x2)
x2_1


print("x1 = ",x1_1[0])
print("x2 = ",x2_1[0])


# # Utilizando numpy resuelve
# 
# ![image.png](attachment:image.png)
# 

# In[7]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt



s=var("s")

a = np.array([[3, 0, 0], [1, 8, 0], [0,4, -2]])

b = np.array([30,18,2])

x = np.linalg.solve(a,b)
x
respuesta=x[0]+x[1]+3*x[2]
respuesta

print(x)
print(" Manzana =",x[0],"\n","Coco =",x[1],"\n","Banana =",x[2])
print(" Manzana + Coco + 3 Bananas =","???")
print(" Manzana + Coco + 3 Bananas =",respuesta)
print(x[0], "+",x[1],"+",3*x[2]," =" ,respuesta)


# # Resuelve 

# ![image.png](attachment:image.png)

# """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb."""

# In[48]:


texto="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb"
decifrado=""
l=len(texto)




for i in range(l):
    if ord(texto[i])== 32:
        decifrado+=chr(32)
    elif texto[i] == 'y':
        decifrado+="a"
    elif texto[i] == 'z':
        decifrado+="b"
    elif texto[i] == '.':
        decifrado+="."
    elif ord(texto[i]) == 39:
        decifrado+=chr(39)
    elif texto[i] == '(':
        decifrado+="("
    elif texto[i] == ')':
        decifrado+=")"
    else:
        decifrado+=chr(ord(texto[i])+2)


print(decifrado)




# # Resolver
# 
# Supongamos que una empresa productora de barras de pan tiene
# dos almacenes A1 y A2 desde los cuales debe enviar pan a tres panaderías P1, P2
# y P3. Las ofertas, las demandas y los costes de env´ıo se dan en el siguiente grafo.
# 

# ![image.png](attachment:image.png)

# In[56]:


from pulp import *


# In[70]:


mi_lp_problema = pulp.LpProblem("Mi LP Problema",pulp.LpMinimize)

x11 = pulp.LpVariable('x11', lowBound=0,cat='Continuous')
x12 = pulp.LpVariable('x12', lowBound=0,cat='Continuous')
x13 = pulp.LpVariable('x13', lowBound=0,cat='Continuous')
x21 = pulp.LpVariable('x21', lowBound=0,cat='Continuous')
x22 = pulp.LpVariable('x22', lowBound=0,cat='Continuous')
x23 = pulp.LpVariable('x23', lowBound=0,cat='Continuous')


#funcion objetivo
mi_lp_problema += 8*x11 + 6*x12 + 10*x13 + 10*x21 + 4*x22 + 9*x23


#Restricciones
mi_lp_problema += x11 + x12 + x13 == 2000
mi_lp_problema += x21 + x22 + x23 == 2500
mi_lp_problema += x11 + x21 == 1500
mi_lp_problema += x12 + x22 == 2000
mi_lp_problema += x13 + x23 == 1000
mi_lp_problema += x11 >= 0
mi_lp_problema += x12 >= 0
mi_lp_problema += x13 >= 0
mi_lp_problema += x21 >= 0
mi_lp_problema += x22 >= 0
mi_lp_problema += x23 >= 0

mi_lp_problema


# In[71]:


mi_lp_problema.solve()
pulp.LpStatus[mi_lp_problema.status]


# In[72]:


mi_lp_problema.variables()


# In[74]:


for variable in mi_lp_problema.variables():
    print("{} = {}".format(variable.name,variable.varValue))


# In[75]:


print(pulp.value(mi_lp_problema.objective)) #Valor minimo de la funcion 


# In[ ]:




