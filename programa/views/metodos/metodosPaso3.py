## CALCULO FIVC3 Y VERIFICACIÓN FIVC CALCULADO EN PASO DOS

from math import *


def calculoFiVc3(a,b,x,y,z):

    fiVc3=0.27*0.75*sqrt(x)*y*z+((0.75*a*y)/(4*b))
    return fiVc3
    
