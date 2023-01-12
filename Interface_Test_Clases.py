from tkinter import Tk, Label, Button, Entry, LabelFrame, Frame
import tkinter as tk
from tkinter import DISABLED, ttk
import clases

"""CLASE PRINCIPAL"""
class Aplicacion(Frame):
 
    # Método constructor de la app
    def __init__(self, master=None):
        
        # Método principal // Tamaño de la ventana
        super().__init__(master,width=800,height=500)
        self.master = master
        self.pack()
        self.crear_elementos()
    
    # Función que realiza los cálculos
    def get_values(self):
        
        fc = float(self.entryFc.get())
      
        fy = float(self.entryFy.get())
        ld = float(self.entryld.get())
        Es = float(self.entryEs.get())
          
        Lw = float(self.entryLw.get())
        Hw = float(self.entryHw.get())
        hw = float(self.entryhw.get())
        h = float(self.entryh.get())
        Cr = float(self.entryCr.get())
        
        Pu = float(self.entryPu.get())
        Mu = float(self.entryMu.get())
        Vu = float(self.entryVu.get())  
        
        # Crea un objeto de tipo muro
        m1 = clases.muro(fc,fy,Es,ld,[Pu,Vu,Mu],[Hw,hw,h,Lw,Cr])
        
        # Aquí se llaman todos los  para el cálculo
        res = m1.calcularAlturaEfectiva(hw)
        
        # Aquí se muestran los resultados en la interfaz
        self.entryd.configure(text="{:.3f}".format(res)) 
    
    def crear_elementos(self):
        
        # SE CREA EL CUADRO DONDE DONDE IRÁN CONTENIDOS LOS DATOS INICIALES PARA EL DISEÑO
        self.datos_iniciales = ttk.LabelFrame(self, text = "Datos Iniciales: ")
        self.datos_iniciales.grid(column=0, row=0, padx=5, pady=10)  
    
        # SE CREA EL CUADRO DONDE DONDE IRÁN CONTENIDOS LOS DATOS INICIALES PARA EL DISEÑO
        self.datos_iniciales = ttk.LabelFrame(self, text = "Datos Iniciales: ")
        self.datos_iniciales.grid(column=0, row=0, padx=5, pady=10)  
    
        # SE CREA EL CUADRO DONDE IRÁN TODOS LOS CALCULOS DEL DISEÑO A CORTANTE POR NSR10
        self.disenio_cortante = ttk.LabelFrame(self, text = "Diseño a cortante: ")        
        self.disenio_cortante.grid(column=4, row=0, padx=5, pady=10)      
    
        # TITULO PROPIEDADES MECANICAS DEL MATERIAL
        self.LabelPm = tk.Label(self.datos_iniciales,text="Propiedades Mecánicas: ", fg="red")
        self.LabelPm.grid(column=0, row=1, padx=2, pady=2)
    
        # RESISTENCIA A LA COMPRESIÓN DEL CONCRETO F'c
        self.fc = ttk.Label(self.datos_iniciales, text="F'c:")
        self.fc.grid(column=0, row=2, padx=2, pady=2)
    
        self.unidadesFc = ttk.Label(self.datos_iniciales, text="MPa")
        self.unidadesFc.grid(column=2, row=2, padx=2, pady=2)
    
        self.entryFc = ttk.Entry(self.datos_iniciales)
        self.entryFc.grid(column=1, row=2, padx=2, pady=2)
    
        ## FLUENCIA DEL ACERO Fy
    
        self.fy = ttk.Label(self.datos_iniciales, text="Fy:")        
        self.fy.grid(column=0, row=3, padx=2, pady=2)
    
        self.unidadesFy = ttk.Label(self.datos_iniciales, text="MPa")
        self.unidadesFy.grid(column=2, row=3, padx=2, pady=2)
    
        self.entryFy = ttk.Entry(self.datos_iniciales)
        self.entryFy.grid(column=1, row=3, padx=2, pady=2)
    
        # Factor de modificación de cocnretos livianos: Lambda
        self.ld = ttk.Label(self.datos_iniciales, text="Factor modificacion concreto (λ):")        
        self.ld.grid(column=0, row=4, padx=2, pady=2)
    
        self.unidadesld = ttk.Label(self.datos_iniciales, text="Adim")
        self.unidadesld.grid(column=2, row=4, padx=2, pady=2)
    
        self.entryld = ttk.Entry(self.datos_iniciales)
        self.entryld.grid(column=1, row=4, padx=2, pady=2)  
    
        # Modulo de Elasticidad: Es
        self.Es = ttk.Label(self.datos_iniciales, text="Módulo de elasticidad (Es):")        
        self.Es.grid(column=0, row=5, padx=2, pady=2)
    
        self.unidadesEs = ttk.Label(self.datos_iniciales, text="Adim")
        self.unidadesEs.grid(column=2, row=5, padx=2, pady=2)
    
        self.entryEs = ttk.Entry(self.datos_iniciales)
        self.entryEs.grid(column=1, row=5, padx=2, pady=2)  
    
        # TITULO PROPIEDADES GEOMETRICAS DE LA SECCIÓN DEL MURO
        self.LabelPg = tk.Label(self.datos_iniciales,text="Propiedades Geométricas: ", fg="red")
        self.LabelPg.grid(column=0, row=4, padx=2, pady=2) 
    
        # LARGO DEL MURO Lw    
        self.Lw=ttk.Label(self.datos_iniciales, text="Largo del muro (Lw):")        
        self.Lw.grid(column=0, row=5, padx=2, pady=2)
    
        self.unidadesLw = ttk.Label(self.datos_iniciales, text="m")
        self.unidadesLw.grid(column=2, row=5, padx=2, pady=2)
    
        self.entryLw = ttk.Entry(self.datos_iniciales)
        self.entryLw.grid(column=1, row=5, padx=2, pady=2)  
    
        # ALTURA DEL MURO DESDE LA CIMENTACIÓN  Hw
        self.Hw = ttk.Label(self.datos_iniciales, text="Altura del muro (Hw):")        
        self.Hw.grid(column=0, row=6, padx=2, pady=2)
    
        self.unidadesHw = ttk.Label(self.datos_iniciales, text="m")
        self.unidadesHw.grid(column=2, row=6, padx=2, pady=2)
    
        self.entryHw = ttk.Entry(self.datos_iniciales)
        self.entryHw.grid(column=1, row=6, padx=2, pady=2) 
    
        # ALTURA DE ENTRE PISO hw
        self.hw = ttk.Label(self.datos_iniciales, text="Altura entrepiso (hw):")        
        self.hw.grid(column=0, row=7, padx=2, pady=2)
    
        self.unidadeshw = ttk.Label(self.datos_iniciales, text="m")
        self.unidadeshw.grid(column=2, row=7, padx=2, pady=2)
    
        self.entryhw = ttk.Entry(self.datos_iniciales)
        self.entryhw.grid(column=1, row=7, padx=2, pady=2) 
    
        # ESPESOR DEL MURO h
        self.h = ttk.Label(self.datos_iniciales, text="Espesor del muro (h):")        
        self.h.grid(column=0, row=8, padx=2, pady=2)
    
        self.unidadesh = ttk.Label(self.datos_iniciales, text="m")
        self.unidadesh.grid(column=2, row=8, padx=2, pady=2)
    
        self.entryh = ttk.Entry(self.datos_iniciales)
        self.entryh.grid(column=1, row=8, padx=2, pady=2) 
    
        # RECUBRIMIENTO Cr
    
        self.Cr = ttk.Label(self.datos_iniciales, text="Recubrimiento (Cr):")        
        self.Cr.grid(column=0, row=9, padx=2, pady=2)
    
        self.unidadesCr = ttk.Label(self.datos_iniciales, text="m")
        self.unidadesCr.grid(column=2, row=9, padx=2, pady=2)
    
        self.entryCr = ttk.Entry(self.datos_iniciales)
        self.entryCr.grid(column=1, row=9, padx=2, pady=2)
    
        # Carga axial critica: Pu
        self.Pu=ttk.Label(self.datos_iniciales, text="Carga axial crítica (Pu):")        
        self.Pu.grid(column=0, row=15, padx=2, pady=2)
    
        self.unidadesPu=ttk.Label(self.datos_iniciales, text="MN")
        self.unidadesPu.grid(column=2, row=15, padx=2, pady=2)
    
        self.entryPu=ttk.Entry(self.datos_iniciales)
        self.entryPu.grid(column=1, row=15, padx=2, pady=2) 
    
        # Momento crtico: Mu
        self.Mu=ttk.Label(self.datos_iniciales, text="Momento crítico (Mu):")        
        self.Mu.grid(column=0, row=16, padx=2, pady=2)
    
        self.unidadesMu=ttk.Label(self.datos_iniciales, text="MN.m")
        self.unidadesMu.grid(column=2, row=16, padx=2, pady=2)
    
        self.entryMu=ttk.Entry(self.datos_iniciales)
        self.entryMu.grid(column=1, row=16, padx=2, pady=2) 
         
        # Cortante critico: Vu
        self.Vu=ttk.Label(self.datos_iniciales, text="Cortante crítico (Vu):")        
        self.Vu.grid(column=0, row=17, padx=2, pady=2)
    
        self.unidadesVu=ttk.Label(self.datos_iniciales, text="MN")
        self.unidadesVu.grid(column=2, row=17, padx=2, pady=2)
    
        self.entryVu=ttk.Entry(self.datos_iniciales)
        self.entryVu.grid(column=1, row=17, padx=2, pady=2) 
    
        # ALTURA EFECTIVA d
        self.d = ttk.Label(self.datos_iniciales, text="Altura efectiva (d):")        
        self.d.grid(column=0, row=10, padx=2, pady=2)
    
        self.unidadesd = ttk.Label(self.datos_iniciales, text="m")
        self.unidadesd.grid(column=2, row=10, padx=2, pady=2)
    
        self.entryd = ttk.Label(self.datos_iniciales, state=DISABLED)
        self.entryd.grid(column=1, row=10, padx=2, pady=2) 
    
        # TITULO COMBINACIÓN DE CARGA CRITICA
        self.LabelCc = tk.Label(self.datos_iniciales,text="Combinación de Carga Crítica: ", fg="red")
        self.LabelCc.grid(column=0, row=11, padx=2, pady=2) 
    
        # CARGA AXIAL ÚLTIMA Pu/Nu
        self.Pu = ttk.Label(self.datos_iniciales, text="Carga axial crítica (Pu):")        
        self.Pu.grid(column=0, row=12, padx=2, pady=2)
    
        self.unidadesPu = ttk.Label(self.datos_iniciales, text="MN")
        self.unidadesPu.grid(column=2, row=12, padx=2, pady=2)
    
        self.LabelPu = ttk.Entry(self.datos_iniciales)
        self.LabelPu.grid(column=1, row=12, padx=2, pady=2) 
    
        # MOMENTO ULTIMO
        self.Mu = ttk.Label(self.datos_iniciales, text="Momento crítico (Mu):")        
        self.Mu.grid(column=0, row=13, padx=2, pady=2)
    
        self.unidadesMu= ttk.Label(self.datos_iniciales, text="MN.m")
        self.unidadesMu.grid(column=2, row=13, padx=2, pady=2)
    
        self.LabelMu = ttk.Entry(self.datos_iniciales)
        self.LabelMu.grid(column=1, row=13, padx=2, pady=2) 
    
        # CORTANTE ÚLTIMO 
        self.Vu = ttk.Label(self.datos_iniciales, text="Cortante crítico (Vu):")        
        self.Vu.grid(column=0, row=14, padx=2, pady=2)
    
        self.unidadesVu=ttk.Label(self.datos_iniciales, text="MN")
        self.unidadesVu.grid(column=2, row=14, padx=2, pady=2)
    
        self.LabelVu = ttk.Entry(self.datos_iniciales)
        self.LabelVu.grid(column=1, row=14, padx=2, pady=2)  
    
        """"DISENIO CORTANTE"""
        # TITULO INTRODUCTORIO A EL CALCULO DEL FIVMAX
        self.LabelFiVmax = tk.Label(self.disenio_cortante,text="Cortante Máximo (ΦVmax): ", fg="red")
        self.LabelFiVmax.grid(column=4, row=1, padx=2, pady=2)
    
        # TITULO INTRODUCTORIO A LA VERIFICACIÓN ESTABLECIDA
        self.LabeltituloCheck1=tk.Label(self.disenio_cortante,text="Verificación: Vu <= ΦVmax:", fg="red")
        self.LabeltituloCheck1.grid(column=4, row=3, padx=2, pady=2)
    
        # TITULO INTRODUCTORIO A EL CALCULO DEL FIVC FINAL
        self.LabelTituloFivcfinal = tk.Label(self.disenio_cortante,text="Cortante Asumido por el Concreto (ΦVc):", fg="red")
        self.LabelTituloFivcfinal.grid(column=4, row=5, padx=2, pady=2)
    
        # TITULO INTRODUCTORIO AL CALCULO DE CUANTIA HORIZONTAL
        self.LabelTituloPh = tk.Label(self.disenio_cortante,text="Cuantía de Acero Horizontal :", fg="red")
        self.LabelTituloPh.grid(column=4, row=7, padx=2, pady=2)
    
        # SE CREA LA CAJA DONDE SE CALCULA EL FIVAMX
        self.fiVmax = ttk.Label(self.disenio_cortante, text="ΦVmax")
        self.fiVmax.grid(column=4, row=2, padx=2, pady=2)
    
        self.entrycalculoFiVmax = ttk.Label(self.disenio_cortante, state=DISABLED, width="8")
        self.entrycalculoFiVmax.grid(column=5, row=2, padx=2, pady=2)
    
        self.unidadesFiVmax = ttk.Label(self.disenio_cortante, text="MN")
        self.unidadesFiVmax.grid(column=6, row=2, padx=2, pady=2)
    
        self.check1 = ttk.Label(self.disenio_cortante, text="¿Cumple?")
        self.check1.grid(column=4, row=4, padx=2, pady=2)
    
        self.labelcheck1 = ttk.Label(self.disenio_cortante, state=DISABLED, width="8")
        self.labelcheck1.grid(column=5, row=4, padx=2, pady=2)
    
        # SE CREA LA CAJA DONDE SE CALCULA EL VALOR DE ΦVc DEPENDIENDO EL CHEQUEO PU >= 01
        self.fiVc = ttk.Label(self.disenio_cortante, text="ΦVc")
        self.fiVc.grid(column=4, row=6, padx=2, pady=2)
    
        self.entrycalculofiVc = ttk.Label(self.disenio_cortante, state=DISABLED, width="8")
        self.entrycalculofiVc.grid(column=5, row=6, padx=2, pady=2)
    
        self.unidadesfiVc = ttk.Label(self.disenio_cortante, text="MN")
        self.unidadesfiVc.grid(column=6, row=6, padx=2, pady=2)
    
        # SE CREA CAJA DONDE IRA EL VALOR DE LA CUANTIA HORIZONTAL
        self.ph=ttk.Label(self.disenio_cortante, text="ρh (Cuantía Horizontal)")
        self.ph.grid(column=4, row=8, padx=2, pady=2)
    
        self.entrycalculoPh=ttk.Label(self.disenio_cortante, state=DISABLED, width="8")
        self.entrycalculoPh.grid(column=5, row=8, padx=2, pady=2)
    
        """-------------------------------------------------------------------------------
        -------------------------------------------------------------------------------"""
        # BOTÓN DE CÁLCULO
        boton = ttk.Button(self, text="Calcular", command=self.get_values)
        boton.grid(column=4, row=5)
        """-------------------------------------------------------------------------------
        -------------------------------------------------------------------------------"""
    

if __name__ == "__main__":   
     
    interface = Tk()
    interface.wm_title("Diseño de Muros")
    app = Aplicacion(interface)
    interface.mainloop()