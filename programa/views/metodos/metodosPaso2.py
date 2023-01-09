from math import *

## SI PU>=0 USAMOS FIVC1     SI PU<= USAMOS FIVC2

def calculoFiVc1 (x,y,z):
    fiVc1=0.17*0.75*sqrt(x)*y*z
    return fiVc1

def calculoAg (x,y):
    ag=x*y
    return ag

def calculoFiVc2(a,b,x,y,z):

    fiVc2=0.17*0.75*(1+0.29*a/b)*sqrt(x)*y*z

    return fiVc2
    