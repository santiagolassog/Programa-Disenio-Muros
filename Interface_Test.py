from tkinter import Tk, Label, Button, Entry, LabelFrame
import tkinter as tk
from tkinter import DISABLED, ttk
import clases

# SE CREA LA VENTANA DONDE SE REALIZARÁ EL DISENIO POR NSR10
interface = Tk()

interface.title("Diseño de Muros")
interface.geometry("750x500")

"""-------------------------------------------------------------------------------
-------------------------------------------------------------------------------"""
def get_values():
    
    fc = float(entryFc.get())
  
    fy = float(entryFy.get())
    ld = float(entryld.get())
    Es = float(entryEs.get())
      
    Lw = float(entryLw.get())
    Hw = float(entryHw.get())
    hw = float(entryhw.get())
    h = float(entryh.get())
    Cr = float(entryCr.get())
    
    Pu = float(entryPu.get())
    Mu = float(entryMu.get())
    Vu = float(entryVu.get())  
    
    # Crea un objeto de tipo muro
    m1 = clases.muro(fc,fy,Es,ld,[Pu,Vu,Mu],[Hw,hw,h,Lw,Cr])
    
    # Aquí se llaman todos los  para el cálculo
    res = m1.calcularAlturaEfectiva(hw)
    
    # Aquí se muestran los resultados en la interfaz
    entryd.configure(text="{:.3f}".format(res)) 
    
"""-------------------------------------------------------------------------------
-------------------------------------------------------------------------------"""
    
# SE CREA EL CUADRO DONDE DONDE IRÁN CONTENIDOS LOS DATOS INICIALES PARA EL DISEÑO
datos_iniciales = ttk.LabelFrame(interface, text = "Datos Iniciales: ")
datos_iniciales.grid(column=0, row=0, padx=5, pady=10)  

# SE CREA EL CUADRO DONDE DONDE IRÁN CONTENIDOS LOS DATOS INICIALES PARA EL DISEÑO
datos_iniciales = ttk.LabelFrame(interface, text = "Datos Iniciales: ")
datos_iniciales.grid(column=0, row=0, padx=5, pady=10)  

# SE CREA EL CUADRO DONDE IRÁN TODOS LOS CALCULOS DEL DISEÑO A CORTANTE POR NSR10
disenio_cortante = ttk.LabelFrame(interface, text = "Diseño a cortante: ")        
disenio_cortante.grid(column=4, row=0, padx=5, pady=10)      

# TITULO PROPIEDADES MECANICAS DEL MATERIAL
LabelPm = tk.Label(datos_iniciales,text="Propiedades Mecánicas: ", fg="red")
LabelPm.grid(column=0, row=1, padx=2, pady=2)

# RESISTENCIA A LA COMPRESIÓN DEL CONCRETO F'c
fc = ttk.Label(datos_iniciales, text="F'c:")
fc.grid(column=0, row=2, padx=2, pady=2)

unidadesFc = ttk.Label(datos_iniciales, text="MPa")
unidadesFc.grid(column=2, row=2, padx=2, pady=2)

entryFc = ttk.Entry(datos_iniciales)
entryFc.grid(column=1, row=2, padx=2, pady=2)

## FLUENCIA DEL ACERO Fy

fy = ttk.Label(datos_iniciales, text="Fy:")        
fy.grid(column=0, row=3, padx=2, pady=2)

unidadesFy = ttk.Label(datos_iniciales, text="MPa")
unidadesFy.grid(column=2, row=3, padx=2, pady=2)

entryFy = ttk.Entry(datos_iniciales)
entryFy.grid(column=1, row=3, padx=2, pady=2)

# Factor de modificación de cocnretos livianos: Lambda
ld = ttk.Label(datos_iniciales, text="Factor modificacion concreto (λ):")        
ld.grid(column=0, row=4, padx=2, pady=2)

unidadesld = ttk.Label(datos_iniciales, text="Adim")
unidadesld.grid(column=2, row=4, padx=2, pady=2)

entryld = ttk.Entry(datos_iniciales)
entryld.grid(column=1, row=4, padx=2, pady=2)  

# Modulo de Elasticidad: Es
Es = ttk.Label(datos_iniciales, text="Módulo de elasticidad (Es):")        
Es.grid(column=0, row=5, padx=2, pady=2)

unidadesEs = ttk.Label(datos_iniciales, text="Adim")
unidadesEs.grid(column=2, row=5, padx=2, pady=2)

entryEs = ttk.Entry(datos_iniciales)
entryEs.grid(column=1, row=5, padx=2, pady=2)  

# TITULO PROPIEDADES GEOMETRICAS DE LA SECCIÓN DEL MURO

LabelPg = tk.Label(datos_iniciales,text="Propiedades Geométricas: ", fg="red")
LabelPg.grid(column=0, row=4, padx=2, pady=2) 

# LARGO DEL MURO Lw

Lw=ttk.Label(datos_iniciales, text="Largo del muro (Lw):")        
Lw.grid(column=0, row=5, padx=2, pady=2)

unidadesLw = ttk.Label(datos_iniciales, text="m")
unidadesLw.grid(column=2, row=5, padx=2, pady=2)

entryLw = ttk.Entry(datos_iniciales)
entryLw.grid(column=1, row=5, padx=2, pady=2)  

# ALTURA DEL MURO DESDE LA CIMENTACIÓN  Hw

Hw = ttk.Label(datos_iniciales, text="Altura del muro (Hw):")        
Hw.grid(column=0, row=6, padx=2, pady=2)

unidadesHw = ttk.Label(datos_iniciales, text="m")
unidadesHw.grid(column=2, row=6, padx=2, pady=2)

entryHw = ttk.Entry(datos_iniciales)
entryHw.grid(column=1, row=6, padx=2, pady=2) 

# ALTURA DE ENTRE PISO hw

hw = ttk.Label(datos_iniciales, text="Altura entrepiso (hw):")        
hw.grid(column=0, row=7, padx=2, pady=2)

unidadeshw = ttk.Label(datos_iniciales, text="m")
unidadeshw.grid(column=2, row=7, padx=2, pady=2)

entryhw = ttk.Entry(datos_iniciales)
entryhw.grid(column=1, row=7, padx=2, pady=2) 

# ESPESOR DEL MURO h

h = ttk.Label(datos_iniciales, text="Espesor del muro (h):")        
h.grid(column=0, row=8, padx=2, pady=2)

unidadesh = ttk.Label(datos_iniciales, text="m")
unidadesh.grid(column=2, row=8, padx=2, pady=2)

entryh = ttk.Entry(datos_iniciales)
entryh.grid(column=1, row=8, padx=2, pady=2) 

# RECUBRIMIENTO Cr

Cr = ttk.Label(datos_iniciales, text="Recubrimiento (Cr):")        
Cr.grid(column=0, row=9, padx=2, pady=2)

unidadesCr = ttk.Label(datos_iniciales, text="m")
unidadesCr.grid(column=2, row=9, padx=2, pady=2)

entryCr = ttk.Entry(datos_iniciales)
entryCr.grid(column=1, row=9, padx=2, pady=2)

# Carga axial critica: Pu
Pu=ttk.Label(datos_iniciales, text="Carga axial crítica (Pu):")        
Pu.grid(column=0, row=15, padx=2, pady=2)

unidadesPu=ttk.Label(datos_iniciales, text="MN")
unidadesPu.grid(column=2, row=15, padx=2, pady=2)

entryPu=ttk.Entry(datos_iniciales)
entryPu.grid(column=1, row=15, padx=2, pady=2) 


# Momento crtico: Mu
Mu=ttk.Label(datos_iniciales, text="Momento crítico (Mu):")        
Mu.grid(column=0, row=16, padx=2, pady=2)

unidadesMu=ttk.Label(datos_iniciales, text="MN.m")
unidadesMu.grid(column=2, row=16, padx=2, pady=2)

entryMu=ttk.Entry(datos_iniciales)
entryMu.grid(column=1, row=16, padx=2, pady=2) 
 
# Cortante critico: Vu
Vu=ttk.Label(datos_iniciales, text="Cortante crítico (Vu):")        
Vu.grid(column=0, row=17, padx=2, pady=2)

unidadesVu=ttk.Label(datos_iniciales, text="MN")
unidadesVu.grid(column=2, row=17, padx=2, pady=2)

entryVu=ttk.Entry(datos_iniciales)
entryVu.grid(column=1, row=17, padx=2, pady=2) 


# ALTURA EFECTIVA d

d = ttk.Label(datos_iniciales, text="Altura efectiva (d):")        
d.grid(column=0, row=10, padx=2, pady=2)

unidadesd = ttk.Label(datos_iniciales, text="m")
unidadesd.grid(column=2, row=10, padx=2, pady=2)

entryd = ttk.Label(datos_iniciales, state=DISABLED)
entryd.grid(column=1, row=10, padx=2, pady=2) 

# TITULO COMBINACIÓN DE CARGA CRITICA
LabelCc = tk.Label(datos_iniciales,text="Combinación de Carga Crítica: ", fg="red")
LabelCc.grid(column=0, row=11, padx=2, pady=2) 

# CARGA AXIAL ÚLTIMA Pu/Nu

Pu = ttk.Label(datos_iniciales, text="Carga axial crítica (Pu):")        
Pu.grid(column=0, row=12, padx=2, pady=2)

unidadesPu = ttk.Label(datos_iniciales, text="MN")
unidadesPu.grid(column=2, row=12, padx=2, pady=2)

LabelPu = ttk.Entry(datos_iniciales)
LabelPu.grid(column=1, row=12, padx=2, pady=2) 

# MOMENTO ULTIMO
Mu = ttk.Label(datos_iniciales, text="Momento crítico (Mu):")        
Mu.grid(column=0, row=13, padx=2, pady=2)

unidadesMu= ttk.Label(datos_iniciales, text="MN.m")
unidadesMu.grid(column=2, row=13, padx=2, pady=2)

LabelMu = ttk.Entry(datos_iniciales)
LabelMu.grid(column=1, row=13, padx=2, pady=2) 

# CORTANTE ÚLTIMO 
Vu = ttk.Label(datos_iniciales, text="Cortante crítico (Vu):")        
Vu.grid(column=0, row=14, padx=2, pady=2)

unidadesVu=ttk.Label(datos_iniciales, text="MN")
unidadesVu.grid(column=2, row=14, padx=2, pady=2)

LabelVu = ttk.Entry(datos_iniciales)
LabelVu.grid(column=1, row=14, padx=2, pady=2)  

# TITULO INTRODUCTORIO A EL CALCULO DEL FIVMAX
LabelFiVmax = tk.Label(disenio_cortante,text="Cortante Máximo (ΦVmax): ", fg="red")
LabelFiVmax.grid(column=4, row=1, padx=2, pady=2)

# TITULO INTRODUCTORIO A LA VERIFICACIÓN ESTABLECIDA
LabeltituloCheck1=tk.Label(disenio_cortante,text="Verificación: Vu <= ΦVmax:", fg="red")
LabeltituloCheck1.grid(column=4, row=3, padx=2, pady=2)

# TITULO INTRODUCTORIO A EL CALCULO DEL FIVC FINAL
LabelTituloFivcfinal = tk.Label(disenio_cortante,text="Cortante Asumido por el Concreto (ΦVc):", fg="red")
LabelTituloFivcfinal.grid(column=4, row=5, padx=2, pady=2)

# TITULO INTRODUCTORIO AL CALCULO DE CUANTIA HORIZONTAL
LabelTituloPh = tk.Label(disenio_cortante,text="Cuantía de Acero Horizontal :", fg="red")
LabelTituloPh.grid(column=4, row=7, padx=2, pady=2)

# SE CREA LA CAJA DONDE SE CALCULA EL FIVAMX
fiVmax = ttk.Label(disenio_cortante, text="ΦVmax")
fiVmax.grid(column=4, row=2, padx=2, pady=2)

entrycalculoFiVmax = ttk.Label(disenio_cortante, state=DISABLED, width="8")
entrycalculoFiVmax.grid(column=5, row=2, padx=2, pady=2)

unidadesFiVmax = ttk.Label(disenio_cortante, text="MN")
unidadesFiVmax.grid(column=6, row=2, padx=2, pady=2)


check1 = ttk.Label(disenio_cortante, text="¿Cumple?")
check1.grid(column=4, row=4, padx=2, pady=2)

labelcheck1 = ttk.Label(disenio_cortante, state=DISABLED, width="8")
labelcheck1.grid(column=5, row=4, padx=2, pady=2)

# SE CREA LA CAJA DONDE SE CALCULA EL VALOR DE ΦVc DEPENDIENDO EL CHEQUEO PU >= 01
fiVc = ttk.Label(disenio_cortante, text="ΦVc")
fiVc.grid(column=4, row=6, padx=2, pady=2)

entrycalculofiVc = ttk.Label(disenio_cortante, state=DISABLED, width="8")
entrycalculofiVc.grid(column=5, row=6, padx=2, pady=2)

unidadesfiVc = ttk.Label(disenio_cortante, text="MN")
unidadesfiVc.grid(column=6, row=6, padx=2, pady=2)

# SE CREA CAJA DONDE IRA EL VALOR DE LA CUANTIA HORIZONTAL
ph=ttk.Label(disenio_cortante, text="ρh (Cuantía Horizontal)")
ph.grid(column=4, row=8, padx=2, pady=2)

entrycalculoPh=ttk.Label(disenio_cortante, state=DISABLED, width="8")
entrycalculoPh.grid(column=5, row=8, padx=2, pady=2)

"""-------------------------------------------------------------------------------
-------------------------------------------------------------------------------"""
# BOTÓN DE CÁLCULO
boton = ttk.Button(interface, text="Calcular", command=get_values)
boton.grid(column=4, row=9)
"""-------------------------------------------------------------------------------
-------------------------------------------------------------------------------"""

interface.mainloop()