from metodos.metodosPaso1 import alturaEfectiva , calculoFiVmax
from metodos.metodosPaso2 import calculoFiVc1 , calculoAg , calculoFiVc2
from metodos.metodosPaso3 import calculoFiVc3
from metodos.metodosPaso4 import calculoMuVuLw2, calculoFiVc4
from metodos.metodosPaso5 import calculoPh
from math import *
from tkinter import messagebox as ms
import tkinter as tk
from tkinter import DISABLED, ttk

class disenioMurosNsr10:


  def __init__(self):

    ##SE CREA LA VENTANA DONDE SE REALIZARÁ EL DISENIO POR NSR10
      self.interfazNsr10=tk.Tk()
      self.interfazNsr10.title("Diseño de Muros")
      
    ## SE CREA EL CUADRO DONDE DONDE IRÁN CONTENIDOS LOS DATOS INICIALES PARA EL DISEÑO
      self.datosIniciales=ttk.LabelFrame(self.interfazNsr10, text="Datos Iniciales: ")        
      self.datosIniciales.grid(column=0, row=0, padx=5, pady=10)  

    ## SE CREA EL CUADRO DONDE IRÁN TODOS LOS CALCULOS DEL DISEÑO A CORTANTE POR NSR10

      self.disenioCortante=ttk.LabelFrame(self.interfazNsr10, text="Diseño a cortante: ")        
      self.disenioCortante.grid(column=4, row=0, padx=5, pady=10)      
    
   
      self.datos()
     

    ## SE CREA EL BOTON QUE AL HACER CLICK REALIZA LOS CALCULOS

      self.boton = ttk.Button(self.interfazNsr10, text="Calcular", command=self.metodosClick )
      self.boton.grid(column=5, row=9)

      self.interfazNsr10.mainloop()
      
  ## MÉTODO QUE CONTIENE TODAS LAS CAJAS DONDE SE CAPTARÁN LOS VALORES INICIALES PARA EL DISEÑO, TITULOS Y UNIDADES A MANEJAR
  def datos(self):
      
      # TITULO PROPIEDADES MECANICAS DEL MATERIAL
      self.LabelPm=tk.Label(self.datosIniciales,text="Propiedades Mecánicas: ", fg="red")
      self.LabelPm.grid(column=0, row=1, padx=2, pady=2)

      ## RESISTENCIA A LA COMPRESIÓN DEL CONCRETO F'c

      self.fc=ttk.Label(self.datosIniciales, text="F'c:")
      self.fc.grid(column=0, row=2, padx=2, pady=2)
      self.unidadesFc=ttk.Label(self.datosIniciales, text="MPa")
      self.unidadesFc.grid(column=2, row=2, padx=2, pady=2)
      self.entryFc=ttk.Entry(self.datosIniciales)
      self.entryFc.grid(column=1, row=2, padx=2, pady=2)

        ## FLUENCIA DEL ACERO Fy

      self.fy=ttk.Label(self.datosIniciales, text="Fy:")        
      self.fy.grid(column=0, row=3, padx=2, pady=2)
      self.unidadesFy=ttk.Label(self.datosIniciales, text="MPa")
      self.unidadesFy.grid(column=2, row=3, padx=2, pady=2)
      self.entryFy=ttk.Entry(self.datosIniciales)
      self.entryFy.grid(column=1, row=3, padx=2, pady=2)

      ## TITULO PROPIEDADES GEOMETRICAS DE LA SECCIÓN DEL MURO

      self.LabelPg=tk.Label(self.datosIniciales,text="Propiedades Geométricas: ", fg="red")
      self.LabelPg.grid(column=0, row=4, padx=2, pady=2) 
        
        ## LARGO DEL MURO Lw

      self.Lw=ttk.Label(self.datosIniciales, text="Largo del muro (Lw):")        
      self.Lw.grid(column=0, row=5, padx=2, pady=2)
      self.unidadesLw=ttk.Label(self.datosIniciales, text="m")
      self.unidadesLw.grid(column=2, row=5, padx=2, pady=2)
      self.entryLw=ttk.Entry(self.datosIniciales)
      self.entryLw.grid(column=1, row=5, padx=2, pady=2)  

        ##ALTURA DEL MURO DESDE LA CIMENTACIÓN  Hw

      self.Hw=ttk.Label(self.datosIniciales, text="Altura del muro (Hw):")        
      self.Hw.grid(column=0, row=6, padx=2, pady=2)
      self.unidadesHw=ttk.Label(self.datosIniciales, text="m")
      self.unidadesHw.grid(column=2, row=6, padx=2, pady=2)
      self.entryHw=ttk.Entry(self.datosIniciales)
      self.entryHw.grid(column=1, row=6, padx=2, pady=2) 

        ##ALTURA DE ENTRE PISO hw

      self.hw=ttk.Label(self.datosIniciales, text="Altura entrepiso (hw):")        
      self.hw.grid(column=0, row=7, padx=2, pady=2)
      self.unidadeshw=ttk.Label(self.datosIniciales, text="m")
      self.unidadeshw.grid(column=2, row=7, padx=2, pady=2)
      self.entryhw=ttk.Entry(self.datosIniciales)
      self.entryhw.grid(column=1, row=7, padx=2, pady=2) 

        ##ESPESOR DEL MURO h

      self.h=ttk.Label(self.datosIniciales, text="Espesor del muro (h):")        
      self.h.grid(column=0, row=8, padx=2, pady=2)
      self.unidadesh=ttk.Label(self.datosIniciales, text="m")
      self.unidadesh.grid(column=2, row=8, padx=2, pady=2)
      self.entryh=ttk.Entry(self.datosIniciales)
      self.entryh.grid(column=1, row=8, padx=2, pady=2) 

        ##RECUBRIMIENTO Cr

      self.Cr=ttk.Label(self.datosIniciales, text="Recubrimiento (Cr):")        
      self.Cr.grid(column=0, row=9, padx=2, pady=2)
      self.unidadesCr=ttk.Label(self.datosIniciales, text="m")
      self.unidadesCr.grid(column=2, row=9, padx=2, pady=2)
      self.entryCr=ttk.Entry(self.datosIniciales)
      self.entryCr.grid(column=1, row=9, padx=2, pady=2)

        ##ALTURA EFECTIVA d

      self.d=ttk.Label(self.datosIniciales, text="Altura efectiva (d):")        
      self.d.grid(column=0, row=10, padx=2, pady=2)
      self.unidadesd=ttk.Label(self.datosIniciales, text="m")
      self.unidadesd.grid(column=2, row=10, padx=2, pady=2)
      self.entryd=ttk.Label(self.datosIniciales, state=DISABLED)
      self.entryd.grid(column=1, row=10, padx=2, pady=2) 

  # TITULO COMBINACIÓN DE CARGA CRITICA
      self.LabelCc=tk.Label(self.datosIniciales,text="Combinación de Carga Crítica: ", fg="red")
      self.LabelCc.grid(column=0, row=11, padx=2, pady=2) 

      ## CARGA AXIAL ÚLTIMA Pu/Nu

      self.Pu=ttk.Label(self.datosIniciales, text="Carga axial crítica (Pu):")        
      self.Pu.grid(column=0, row=12, padx=2, pady=2)
      self.unidadesPu=ttk.Label(self.datosIniciales, text="MN")
      self.unidadesPu.grid(column=2, row=12, padx=2, pady=2)
      self.LabelPu=ttk.Entry(self.datosIniciales)
      self.LabelPu.grid(column=1, row=12, padx=2, pady=2) 

      ## MOMENTO ULTIMO
      self.Mu=ttk.Label(self.datosIniciales, text="Momento crítico (Mu):")        
      self.Mu.grid(column=0, row=13, padx=2, pady=2)
      self.unidadesMu=ttk.Label(self.datosIniciales, text="MN.m")
      self.unidadesMu.grid(column=2, row=13, padx=2, pady=2)
      self.LabelMu=ttk.Entry(self.datosIniciales)
      self.LabelMu.grid(column=1, row=13, padx=2, pady=2) 
      
      ## CORTANTE ÚLTIMO 

      self.Vu=ttk.Label(self.datosIniciales, text="Cortante crítico (Vu):")        
      self.Vu.grid(column=0, row=14, padx=2, pady=2)
      self.unidadesVu=ttk.Label(self.datosIniciales, text="MN")
      self.unidadesVu.grid(column=2, row=14, padx=2, pady=2)
      self.LabelVu=ttk.Entry(self.datosIniciales)
      self.LabelVu.grid(column=1, row=14, padx=2, pady=2)  

## TITULO INTRODUCTORIO A EL CALCULO DEL FIVMAX

      self.LabelFiVmax=tk.Label(self.disenioCortante,text="Cortante Máximo (ΦVmax): ", fg="red")
      self.LabelFiVmax.grid(column=4, row=1, padx=2, pady=2)

## TITULO INTRODUCTORIO A LA VERIFICACIÓN ESTABLECIDA
      
      self.LabeltituloCheck1=tk.Label(self.disenioCortante,text="Verificación: Vu <= ΦVmax:", fg="red")
      self.LabeltituloCheck1.grid(column=4, row=3, padx=2, pady=2)

##TITULO INTRODUCTORIO A EL CALCULO DEL FIVC FINAL
      self.LabelTituloFivcfinal=tk.Label(self.disenioCortante,text="Cortante Asumido por el Concreto (ΦVc):", fg="red")
      self.LabelTituloFivcfinal.grid(column=4, row=5, padx=2, pady=2)

## TITULO INTRODUCTORIO AL CALCULO DE CUANTIA HORIZONTAL
      self.LabelTituloPh=tk.Label(self.disenioCortante,text="Cuantía de Acero Horizontal :", fg="red")
      self.LabelTituloPh.grid(column=4, row=7, padx=2, pady=2)


      #SE CREA LA CAJA DONDE SE CALCULA EL FIVAMX

      self.fiVmax=ttk.Label(self.disenioCortante, text="ΦVmax")
      self.fiVmax.grid(column=4, row=2, padx=2, pady=2)
      self.entrycalculoFiVmax=ttk.Label(self.disenioCortante, state=DISABLED, width="8")
      self.entrycalculoFiVmax.grid(column=5, row=2, padx=2, pady=2)
      self.unidadesFiVmax=ttk.Label(self.disenioCortante, text="MN")
      self.unidadesFiVmax.grid(column=6, row=2, padx=2, pady=2)
      

      self.check1=ttk.Label(self.disenioCortante, text="¿Cumple?")
      self.check1.grid(column=4, row=4, padx=2, pady=2)
      self.labelcheck1=ttk.Label(self.disenioCortante, state=DISABLED, width="8")
      self.labelcheck1.grid(column=5, row=4, padx=2, pady=2)

      #SE CREA LA CAJA DONDE SE CALCULA EL VALOR DE ΦVc DEPENDIENDO EL CHEQUEO PU >= 01
      self.fiVc=ttk.Label(self.disenioCortante, text="ΦVc")
      self.fiVc.grid(column=4, row=6, padx=2, pady=2)
      self.entrycalculofiVc=ttk.Label(self.disenioCortante, state=DISABLED, width="8")
      self.entrycalculofiVc.grid(column=5, row=6, padx=2, pady=2)
      self.unidadesfiVc=ttk.Label(self.disenioCortante, text="MN")
      self.unidadesfiVc.grid(column=6, row=6, padx=2, pady=2)

      #SE CREA CAJA DONDE IRA EL VALOR DE LA CUANTIA HORIZONTAL
      self.ph=ttk.Label(self.disenioCortante, text="ρh (Cuantía Horizontal)")
      self.ph.grid(column=4, row=8, padx=2, pady=2)
      self.entrycalculoPh=ttk.Label(self.disenioCortante, state=DISABLED, width="8")
      self.entrycalculoPh.grid(column=5, row=8, padx=2, pady=2)
     
      
      

## Método que le indica al boton que metodos ejecutar al hacer click
  def metodosClick(self):
    self.calculod()
    self.calcularFiVmax()
    self.chequeo1()
    self.chequeo2()
    self.chequeo3(self.chequeo2())
    self.chequeo4(self.chequeo3(self.chequeo2()))
    self.cuantiaHorizontal(self.chequeo4(self.chequeo3(self.chequeo2())))
    
    


    
## Metodos que ejecutan los metodos creados en metodosPaso1

# Metodo que calcula la altura efectiva
  def calculod(self):
    d=alturaEfectiva(float(self.entryLw.get()))
    self.entryd.configure(text="{:.3f}".format(d))
    
# Metodo que calcula el valor de ΦVmax
  def calcularFiVmax(self):

    fiVmaxCalculado=calculoFiVmax(float(self.entryFc.get()),alturaEfectiva(float(self.entryLw.get())),float(self.entryh.get()))
    self.entrycalculoFiVmax.configure(text="{:.3f}".format(fiVmaxCalculado))

   ## Metodo que verifica el primer chequeo que Vu <= ΦVmax

  def chequeo1(self):
    Vu=float(self.LabelVu.get())
    Vmax=calculoFiVmax(float(self.entryFc.get()),alturaEfectiva(float(self.entryLw.get())),float(self.entryh.get()))

    if Vu >= Vmax:
      self.labelcheck1.configure(text="NO")
      ms.showerror("Advertencia","No se cumple la primera verificación: Vu <= ΦVmax. Consejo: redimensionar muro ")

    else:
      self.labelcheck1.configure(text="SI")
      

  ## METODOS PASO 2

  ## METODO QUE CALCULA ΦVc según se cumpla que Pu>0 o no.

  def chequeo2(self):
    Vu=float(self.LabelVu.get())
    Pu=float(self.LabelPu.get())
    Vmax=calculoFiVmax(float(self.entryFc.get()),alturaEfectiva(float(self.entryLw.get())),float(self.entryh.get()))
    
   
    if  Vu <= Vmax and Pu >= 0:
      fiVc=calculoFiVc1(float(self.entryFc.get()),alturaEfectiva(float(self.entryLw.get())),float(self.entryh.get()))
      return fiVc
      
    elif Vu <= Vmax and Pu <= 0:

      fiVc=calculoFiVc2(float(self.LabelPu.get()),calculoAg(float(self.entryLw.get()),float(self.entryh.get())),float(self.entryFc.get()),alturaEfectiva(float(self.entryLw.get())),float(self.entryh.get()))
      return fiVc
    else:
      return fiVc

 ## METODOS PASO 3
  def chequeo3 (self,pfiVc):

    fiVc3=calculoFiVc3(float(self.LabelPu.get()),float(self.entryLw.get()),float(self.entryFc.get()),alturaEfectiva(float(self.entryLw.get())),float(self.entryh.get()))
    newFiVc=0
    
    if pfiVc <= fiVc3:
      newFiVc= fiVc3
      return newFiVc
    
    else:
      newFiVc=pfiVc
      return newFiVc
 ## METODOS PASO 4
  def chequeo4 (self, pnewFiVc):
    
    fiVcFinal=0
    fiVc4=calculoFiVc4(float(self.entryLw.get()),float(self.LabelPu.get()),float(self.entryFc.get()),alturaEfectiva(float(self.entryLw.get())),float(self.entryh.get())  )
    muVuLw2=calculoMuVuLw2(float(self.LabelMu.get()), float(self.LabelVu.get()),float(self.entryLw.get()))
    
    if muVuLw2<0:
      fiVcFinal=pnewFiVc
      self.entrycalculofiVc.configure(text="{:.3f}".format(fiVcFinal))
      return fiVcFinal

    elif muVuLw2>=0 and pnewFiVc<=fiVc4:
      fiVcFinal=fiVc4
      self.entrycalculofiVc.configure(text="{:.3f}".format(fiVcFinal))
      return fiVcFinal
    else:
      fiVcFinal=pnewFiVc
      self.entrycalculofiVc.configure(text="{:.3f}".format(fiVcFinal))
      return fiVcFinal
    
## METODOS PASO 5
  def cuantiaHorizontal(self, pfiVcFinal):
    ph1=calculoPh(float(self.LabelVu.get()),float(pfiVcFinal),float(self.entryFy.get()),alturaEfectiva(float(self.entryLw.get())),float(self.entryh.get()))
    ph2=0.0025
    phFinal=max(ph1, ph2)
    self.entrycalculoPh.configure(text="{:.4f}".format(phFinal))
    return phFinal





     


app=disenioMurosNsr10()