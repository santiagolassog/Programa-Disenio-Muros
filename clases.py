"""-------------------------------------------------------
Importación de librerías
-------------------------------------------------------"""
from math import *
import numpy as np
"""-------------------------------------------------------
CARACTERÍSTICAS DE UN MURO:
----------------------------------------------------------
1) fc: resistencia a la compresión del concreto
2) fy: fluencia del acero
3) Es: módulo de elasticidad
4) ld: lambda --> factor propio de los materiales
5) cargas: cargas críticas a las que estará sometido el muro
6) geometria: dimensiones del muro
-------------------------------------------------------"""
class muro:
    
    def __init__(self, fc, fy, Es, ld, cargas, geometria):
        self.fc = float(fc)
        self.fy = float(fy)
        self.Es = float(Es)
        self.ld = float(ld)
        self.cargas = list(cargas)
        self.geometria = list(geometria)
        self.info_acero = {2:32,3:71,4:129,5:199,6:284,7:387,
                           8:510,9:645,10:819,11:1006,14:1452,18:2581}
    
    def calcular(self,y):
        return y
        
    def calcularAreaMuro(self):
        area = self.geometria[2] * self.geometria[3] 
        return area
    """------------------------------------------------
    # PASO 1: Calcula la altura efectiva del muro
    ------------------------------------------------"""
    def calcularAlturaEfectiva(self,x):
       d = 0.8 * x
       return d
   
    def calcularFiVmax(self,a,y,z):
       fiVmax = 0.83 * 0.75 * sqrt(a) * y * z
       #print(fiVmax)
       return fiVmax

    """------------------------------------------------
    # PASO 2: Calcula la altura efectiva del muro
    ------------------------------------------------"""
    # def verificar1(self):
    #     fiVmax = calcularFiVmax(self.fc,calcularAlturaEfectiva(self.geometria[2]),self.geometria[3])
    #     return fiVmax
    #     # if self.cargas[1] <= fiVmax:
    #     #     print('Diseñar a cortante')
    #     # else:
    #     #     print('Redimensionar el muro. Cambiar valores de geometría')
    
    def calcularFiVc(self):
        a = self.cargas[0]
        b = self.calcularAreaMuro()
        x = self.fc
        d = self.calcularAlturaEfectiva(self.geometria[2])
        z = self.geometria[3]
        
        # Primeras operaciones
        fiVc1 = 0.17*0.75*sqrt(x)*d*z
        fiVc2 = 0.17*0.75*(1+0.29*a/b)*sqrt(x)*d*z
        
        if self.cargas[0] >= 0:
            fiVc = fiVc1
        else:
            fiVc = fiVc2
        
        # Segunda operación
        b2 = self.geometria[2]
        fiVc3 = 0.27*0.75*sqrt(x)*d*z+((0.75*a*d)/(4*b2))
        
        if fiVc <= fiVc3:
            fiVc4 = fiVc3
        else:
            fiVc4 = fiVc
        
        x2 = self.cargas[2]
        y2 = self.cargas[1]
        z2 = self.geometria[2]
        MuVuLw2 = (x2/y2)-(z2/2)
        fiVc5 = 0.75*(0.05*sqrt(x)+((z2*(0.1*sqrt(x)+0.2*(a/(z2*z))))/(MuVuLw2)))*d*z
        
        if MuVuLw2 < 0:
            fiVc_final = fiVc4
        else:
            fiVc_final = fiVc5
        
        print(fiVc_final)
        return fiVc_final
    
    """------------------------------------------------
    # PASO 4: Calcula refuerzo horizontal
    ------------------------------------------------"""
    def calcularCuantiaHorizontal(self):
        vu=self.cargas[1]
        vc=self.calcularFiVc()
        
        ph1=(vu-vc)/(0.75*self.fy*self.calcularAlturaEfectiva(self.geometria[2])*self.geometria[3])
        ph2=0.0025
        ph=max(ph1,ph2)
        print(ph)
        return ph
    
     
    """------------------------------------------------
    # PASO 5: Calcula refuerzo vertical
    ------------------------------------------------"""
    
    def calcularCuantiaVertical(self):
        
        pv1=0.0025+0.5*(2.5-self.geometria[1]/self.geometria[2])*(self.calcularCuantiaHorizontal()-0.0025)
        pv2=0.0025
        pv=max(pv1,pv2)
        print(pv)
        return pv
    
    def calcularSeparacion(self, nh, nv, capas):
        d=self.calcularAlturaEfectiva(self.geometria[2])
        Avv=self.info_acero.pop(nv)
        Avh=self.info_acero.pop(nh)
        ShHorizontal=(Avh/10000*capas)/(self.calcularCuantiaHorizontal()*self.geometria[3])
        ShVertical=(Avv/10000*capas)/(self.calcularCuantiaVertical()*self.geometria[3])
        Sh2=self.geometria[2]/5*100
        Sh3=self.geometria[3]*3*100
        Sh4=45
        ShvFinal=min(ShVertical,Sh2,Sh3,Sh4)
        ShhFinal=min(ShHorizontal,Sh2,Sh3,Sh4)
        
        print(ShvFinal,ShhFinal)
        
        return (ShvFinal,ShhFinal)
    
"""-------------------------------------------------------
PROGRAMA PRINCIPAL:
-------------------------------------------------------"""   
# m1 = muro(28,420,200,1,[2.5,1.28,15.25],[31.5,3.5,5,0.3,0.05])
# m1.calcularFiVmax(m1.fc,m1.calcularAlturaEfectiva(m1.geometria[2]),m1.geometria[3])
# m1.calcularFiVc()
# m1.calcularCuantiaHorizontal()
# m1.calcularCuantiaVertical()
# m1.calcularSeparacion(3,6,2)