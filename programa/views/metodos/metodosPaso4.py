
## CALCULO DE MU/VU-LW/2

from cmath import sqrt


def calculoMuVuLw2(x,y,z):
    MuVuLw2=(x/y)-(z/2)
    return MuVuLw2

def calculoFiVc4(a,b,x,y,z):
    fiVc4=0.75*(0.05*sqrt(x)+((a*(0.1*sqrt(x)+0.2*(b/(a*z))))/(calculoMuVuLw2(x,y,z))))*y*z
    return fiVc4