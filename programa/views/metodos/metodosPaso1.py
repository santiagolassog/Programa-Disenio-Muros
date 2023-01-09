from math import *


## PASO 1 CALCULAR ΦVmax Y COMPROBAR QUE Vu <= ΦVmax 

## Calcula la altura efectiva del muro

def alturaEfectiva(x):
   d=0.8*x
   return d

## Calcula el valor de ΦVmax 
def calculoFiVmax(a,y,z):
   fiVmax=0.83*0.75*sqrt(a)*y*z
   return fiVmax
 
