from tkinter import Tk, Label, Button, Entry, LabelFrame, Frame
import tkinter as tk
from tkinter import DISABLED, ttk
from tkinter import messagebox as ms
import clases

"""-----------------------------------------------------------------------------------
CLASE PRINCIPAL: INTERFAZ
-----------------------------------------------------------------------------------"""
class Aplicacion(Frame):
    
    """-------------------------------------------------------------------------------
    -------------------------------------------------------------------------------""" 
    # Método constructor de la app
    def __init__(self, master=None):
        
        # Método principal // Tamaño de la ventana
        super().__init__(master)
        self.master = master
        self.pack()
        
        self.crear_elementos_Datos_Iniciales()
        self.crear_elementos_Disenio_Cortante()
        self.crear_elementos_Flexion()
    """-------------------------------------------------------------------------------
    -------------------------------------------------------------------------------"""
    def abrir_ventana2(self):
        self.ventana2 = tk.Toplevel()
        self.ventana2.geometry('1000x500')
        self.ventana2.configure()
        # self.labelv2 = tk.Label(self.ventana2,text='Segunda ventana')
        # self.labelv2.grid(column=0, row=9, padx=2, pady=2)  
        
        def changetext(label):
            label.config(text="button on my left has been pressed")

        desired_number = 10

        for i in range(desired_number):
            button = tk.Button(self.ventana2,text=f"Button {i}")
            button.grid(row = i, column = 0)
            label = tk.Label(self.ventana2)
            label.grid(row = i, column = 1)
            button.config(command = lambda x=label: changetext(x))
            
    """-------------------------------------------------------------------------------
    -------------------------------------------------------------------------------"""
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
        self.m1 = clases.muro(fc,fy,Es,ld,[Pu,Vu,Mu],[Hw,hw,Lw,h,Cr])
        
        # Aquí se llaman todos los  para el cálculo
        d = self.m1.calcularAlturaEfectiva(Lw)
        Ag = self.m1.calcularAreaMuro()
        beta = self.m1.beta()
        vmax = self.m1.calcularFiVmax(fc, d, h)
        fiVc = self.m1.calcularFiVc()
        ph = self.m1.calcularCuantiaHorizontal()
        pv =self.m1.calcularCuantiaVertical()
          
        # Aquí se muestran los resultados en la interfaz
        self.entryd.configure(text="{:.3f}".format(d)) 
        self.entryAg.configure(text="{:.3f}".format(Ag)) 
        self.entrybeta1.configure(text="{:.3f}".format(beta))
        self.entrycalculoFiVmax.configure(text="{:.3f}".format(vmax)) 
        self.entrycalculofiVc.configure(text="{:.3f}".format(fiVc)) 
        self.entrycalculoPh.configure(text="{:.5f}".format(ph)) 
        self.entrycalculoPv.configure(text="{:.5f}".format(pv))
      
        # Método que hace la primera verificación
        self.verificar()
        
        # CALCULO DE LA SEPARACION DE BARRAS
        self.lista_aceroh['values'] = [i for i in self.m1.info_acero_h.keys()]
        self.lista_acerov['values'] = [i for i in self.m1.info_acero_v.keys()]
        
        select = int(self.lista_aceroh.get())
        n_capas = int(self.entryNcapash.get())
    
        select2 = int(self.lista_acerov.get())
        n_capas2 = int(self.entryNcapasv.get())
        
        sep_h = self.m1.calcularSeparacionHorizontal(select,n_capas)
        sep_v = self.m1.calcularSeparacionVertical(select2,n_capas2)
       
        self.entrySeparacionHorizontal.configure(text="{:.5f}".format(float(sep_h))) 
        self.entrySeparacionVertical.configure(text="{:.5f}".format(float(sep_v)))
        
        #SE EJECUTA EL METODO VERIFICAR 2 QUE INDICA SEGUN LA ESBELTEZ EL ESTADO DE CONTROL DEL MURO
        
        self.verificar2()  
        
        #Resultados de la interfaz para diseño a flexion
        
        esfuerzo = self.m1.esfuerzo(fc)
        fc2 = self.m1.fc2()
        self.entryfcResistente.configure(text="{:.5f}".format(esfuerzo))
        self.entryfcElemento.configure(text="{:.5f}".format(fc2))
       
        #AQUI SE EJECUTA EL METODO DE VERIFICAR 3 QUE VERIFICA SI SE REQUIEREN O NO ELEMENTOS DE BORDE
        
        self.verificar3()
        
        #AQUI VAN LOS METODOS QUE CACLULAN EL AREA DE LOS ELEMENTOS DE BORDE
        
        X = float(self.entryX.get())
        B = float(self.entryB.get()) 
        AgBorde = self.m1.calcularAgBorde(B,X)
        self.entryAgBorde.configure(text="{:.5f}".format(AgBorde))
        
        
        #AQUI VAN LOS METODOS QUE CALCULAN EL AREA DE ACERO DE LOS ELEMENTOS DE BORDE
        
        Agborde2 = self.m1.calcularAgBorde(B, X)
        Pu2 = self.m1.calcularPuAxial(X)
        Astflex = self.m1.calcularAreaAceroFlex(Agborde2, Pu2)
        self.entryAstBorde.configure(text="{:.5f}".format(Astflex))
        
        #AQUI VA EL METODO QUE CALCULA LA CUANTIA DE ACERO DE LOS ELEMENTOS DE BORDE
        
        pEb = self.m1.cuantiaEb(Astflex, Agborde2)
        self.entrypBorde.configure(text="{:.5f}".format(pEb))
        
        self.verificar4()
        
        self.lista_aceroFlex['values'] = [i for i in self.m1.info_acero_eB.keys()]
        
        select3 = int(self.lista_aceroFlex.get())
        
        nbarras = self.m1.calcularNbarrasEb(Astflex, select3)
        
        self.entryNbarraEb.configure(text="{:.5f}".format(float(nbarras)))
        
    """-------------------------------------------------------------------------------
    -------------------------------------------------------------------------------"""
    
    def verificar(self):
        
        fc = float(self.entryFc.get())
        d = self.m1.calcularAlturaEfectiva(float(self.entryLw.get()))
        h = float(self.entryh.get())
        
        Vu = float(self.entryVu.get())
        Vmax = self.m1.calcularFiVmax(fc, d, h)

        if Vu >= Vmax:
            self.labelcheck1.configure(text="NO")
            ms.showerror("Advertencia","No se cumple la primera verificación: Vu <= ΦVmax. Consejo: redimensionar muro ")
        
        else:
            self.labelcheck1.configure(text="SI")
            
            
    def verificar2(self):
            
        hw = float(self.entryhw.get())
        Lw = float(self.entryLw.get())
        k = self.m1.esbeltez(hw, Lw)  

        if k <= 2:
                self.labelcheck2.configure(text="Controla el cortante")
                
            
        else:
                self.labelcheck2.configure(text="Controla la flexión")
                
    def verificar3(self):
        
        esfuerzoElemento = self.m1.esfuerzo(float(self.entryFc.get()))
        esfuerzoFc = self.m1.fc2()
        
        if esfuerzoElemento <= esfuerzoFc:
            
                self.entryelementoBorde.configure(text="Requiere EB")
                
        else: 
                ms.showerror("Fin del diseño: ", "Utilizar acero de refuerzo horizontal y vertical obtenido en el diseño a cortante")
                self.entryelementoBorde.configure(text="No requiere EB")
                
    def verificar4(self):
        X = float(self.entryX.get())
        B = float(self.entryB.get())        
        Agborde2 = self.m1.calcularAgBorde(B, X)
        Pu2 = self.m1.calcularPuAxial(X)
        Astflex = self.m1.calcularAreaAceroFlex(Agborde2, Pu2)      
        pEb = self.m1.cuantiaEb(Astflex, Agborde2)
        
        if pEb > 4: 
            
            ms.showerror("Advertencia:  ", "Cuantía máxima por normativa del 4% pero densidad de refuerzo excesiva. Se aconseja REDIMENSIONAR ELEMENTOS DE BORDE hasta que la cuantía este entre el 2 y el 2.5% ")
        
        else:
            pass
        
    def crear_elementos_Datos_Iniciales(self):
        
        # SE CREA EL CUADRO DONDE DONDE IRÁN CONTENIDOS LOS DATOS INICIALES PARA EL DISEÑO
        self.datos_iniciales = ttk.LabelFrame(self, text = "Datos Iniciales: ")
        self.datos_iniciales.grid(column=0, row=0, padx=5, pady=10)  
         
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
        
        # FLUENCIA DEL ACERO Fy
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
        
        self.unidadesEs = ttk.Label(self.datos_iniciales, text="GPa")
        self.unidadesEs.grid(column=2, row=5, padx=2, pady=2)
        
        self.entryEs = ttk.Entry(self.datos_iniciales)
        self.entryEs.grid(column=1, row=5, padx=2, pady=2)  
        
        # TITULO PROPIEDADES GEOMETRICAS DE LA SECCIÓN DEL MURO
        self.LabelPg = tk.Label(self.datos_iniciales,text="Propiedades Geométricas: ", fg="red")
        self.LabelPg.grid(column=0, row=6, padx=2, pady=2) 
        
        # LARGO DEL MURO Lw 
        self.Lw=ttk.Label(self.datos_iniciales, text="Largo del muro (Lw):")        
        self.Lw.grid(column=0, row=7, padx=2, pady=2)
        
        self.unidadesLw = ttk.Label(self.datos_iniciales, text="m")
        self.unidadesLw.grid(column=2, row=7, padx=2, pady=2)
        
        self.entryLw = ttk.Entry(self.datos_iniciales)
        self.entryLw.grid(column=1, row=7, padx=2, pady=2)  
        
        # ALTURA DEL MURO DESDE LA CIMENTACIÓN  Hw
        self.Hw = ttk.Label(self.datos_iniciales, text="Altura total del muro (Hw):")        
        self.Hw.grid(column=0, row=8, padx=2, pady=2)
        
        self.unidadesHw = ttk.Label(self.datos_iniciales, text="m")
        self.unidadesHw.grid(column=2, row=8, padx=2, pady=2)
        
        self.entryHw = ttk.Entry(self.datos_iniciales)
        self.entryHw.grid(column=1, row=8, padx=2, pady=2) 
        
        # ALTURA DE ENTRE PISO hw
        self.hw = ttk.Label(self.datos_iniciales, text="Altura entrepiso (hw):")        
        self.hw.grid(column=0, row=9, padx=2, pady=2)
        
        self.unidadeshw = ttk.Label(self.datos_iniciales, text="m")
        self.unidadeshw.grid(column=2, row=9, padx=2, pady=2)
        
        self.entryhw = ttk.Entry(self.datos_iniciales)
        self.entryhw.grid(column=1, row=9, padx=2, pady=2) 
        
        # ESPESOR DEL MURO h
        self.h = ttk.Label(self.datos_iniciales, text="Espesor del muro (h):")        
        self.h.grid(column=0, row=10, padx=2, pady=2)
        
        self.unidadesh = ttk.Label(self.datos_iniciales, text="m")
        self.unidadesh.grid(column=2, row=10, padx=2, pady=2)
        
        self.entryh = ttk.Entry(self.datos_iniciales)
        self.entryh.grid(column=1, row=10, padx=2, pady=2) 
        
        # RECUBRIMIENTO Cr
        self.Cr = ttk.Label(self.datos_iniciales, text="Recubrimiento (Cr):")        
        self.Cr.grid(column=0, row=11, padx=2, pady=2)
        
        self.unidadesCr = ttk.Label(self.datos_iniciales, text="m")
        self.unidadesCr.grid(column=2, row=11, padx=2, pady=2)
        
        self.entryCr = ttk.Entry(self.datos_iniciales)
        self.entryCr.grid(column=1, row=11, padx=2, pady=2)   
        
        # ALTURA EFECTIVA d 
        self.d = ttk.Label(self.datos_iniciales, text="Altura efectiva (d):")        
        self.d.grid(column=0, row=12, padx=2, pady=2)
        
        self.unidadesd = ttk.Label(self.datos_iniciales, text="m")
        self.unidadesd.grid(column=2, row=12, padx=2, pady=2)
        
        self.entryd = ttk.Label(self.datos_iniciales, state=DISABLED)
        self.entryd.grid(column=1, row=12, padx=2, pady=2) 
           
        # Area bruta de la sección transversal del muro  
        self.Ag = ttk.Label(self.datos_iniciales, text="Área bruta muro (Ag):")        
        self.Ag.grid(column=0, row=13, padx=2, pady=2)
        
        self.unidadesAg = ttk.Label(self.datos_iniciales, text="m2")
        self.unidadesAg.grid(column=2, row=13, padx=2, pady=2)
        
        self.entryAg = ttk.Label(self.datos_iniciales, state=DISABLED)
        self.entryAg.grid(column=1, row=13, padx=2, pady=2) 
        
        # TITULO COMBINACIÓN DE CARGA CRITICA
        self.LabelCc = tk.Label(self.datos_iniciales,text="Combinación de Carga Crítica: ", fg="red")
        self.LabelCc.grid(column=0, row=14, padx=2, pady=2) 
        
        # CARGA AXIAL ÚLTIMA Pu/Nu   
        self.Pu = ttk.Label(self.datos_iniciales, text="Carga axial crítica (Pu):")        
        self.Pu.grid(column=0, row=15, padx=2, pady=2)
        
        self.unidadesPu = ttk.Label(self.datos_iniciales, text="MN")
        self.unidadesPu.grid(column=2, row=15, padx=2, pady=2)
        
        self.entryPu = ttk.Entry(self.datos_iniciales)
        self.entryPu.grid(column=1, row=15, padx=2, pady=2) 
        
        # MOMENTO ULTIMO
        self.Mu = ttk.Label(self.datos_iniciales, text="Momento crítico (Mu):")        
        self.Mu.grid(column=0, row=16, padx=2, pady=2)
        
        self.unidadesMu= ttk.Label(self.datos_iniciales, text="MN.m")
        self.unidadesMu.grid(column=2, row=16, padx=2, pady=2)
        
        self.entryMu = ttk.Entry(self.datos_iniciales)
        self.entryMu.grid(column=1, row=16, padx=2, pady=2) 
        
        
        #BETA 1
        self.beta1 = ttk.Label(self.datos_iniciales, text="Factor beta (β1):")        
        self.beta1.grid(column=0, row=19, padx=2, pady=2)
        
        self.unidadesbeta1= ttk.Label(self.datos_iniciales, text="Adim")
        self.unidadesbeta1.grid(column=2, row=19, padx=2, pady=2)
        
        self.entrybeta1 = ttk.Label(self.datos_iniciales)
        self.entrybeta1.grid(column=1, row=19, padx=2, pady=2) 
        
    def crear_elementos_Disenio_Cortante(self):
        
        # SE CREA EL CUADRO DONDE IRÁN TODOS LOS CALCULOS DEL DISEÑO A CORTANTE POR NSR10
        self.disenio_cortante = ttk.LabelFrame(self, text = "Diseño a cortante: ")        
        self.disenio_cortante.grid(column=4, row=0, padx=5, pady=10) 
        
        # CORTANTE ÚLTIMO 
        self.Vu = ttk.Label(self.datos_iniciales, text="Cortante crítico (Vu):")        
        self.Vu.grid(column=0, row=17, padx=2, pady=2)
        
        self.unidadesVu=ttk.Label(self.datos_iniciales, text="MN")
        self.unidadesVu.grid(column=2, row=17, padx=2, pady=2)
        
        self.entryVu = ttk.Entry(self.datos_iniciales)
        self.entryVu.grid(column=1, row=17, padx=2, pady=2)  
        
        # TITULO INTRODUCTORIO A EL CALCULO DEL FIVMAX
        self.LabelFiVmax = tk.Label(self.disenio_cortante,text="Cortante Máximo (ΦVmax): ", fg="red")
        self.LabelFiVmax.grid(column=4, row=1, padx=2, pady=2)
        
        # TITULO INTRODUCTORIO A LA VERIFICACIÓN ESTABLECIDA
        self.LabeltituloCheck1 = tk.Label(self.disenio_cortante,text="Verificación: Vu <= ΦVmax:", fg="red")
        self.LabeltituloCheck1.grid(column=4, row=3, padx=2, pady=2)
        
        # TITULO INTRODUCTORIO A EL CALCULO DEL FIVC FINAL
        self.LabelTituloFivcfinal = tk.Label(self.disenio_cortante,text="Cortante Asumido por el Concreto (ΦVc):", fg="red")
        self.LabelTituloFivcfinal.grid(column=4, row=5, padx=2, pady=2)
        
        # TITULO INTRODUCTORIO AL CALCULO DE REFUERZO DE ACERO HORIZONTAL
        self.LabelTituloPh = tk.Label(self.disenio_cortante,text="Refuerzo Acero Horizontal :", fg="red")
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
        
        # SE CREA CAJA DONDE SE ESCOGE LA BARRA A EMPLEAR EN EL REFUERZO HORIZONTAL
        
        self.acero_horizontal=ttk.Label(self.disenio_cortante, text="N° Barra de acero: ")
        self.acero_horizontal.grid(column=4, row=9, padx=2, pady=2)
        
        #SE CREA CAJA DONDE VA CONTENIDO EN NUMERO DE CAPAS QUE SE EMPLEARAN
        
        self.nCapash=ttk.Label(self.disenio_cortante, text="Número de capas: ")
        self.nCapash.grid(column=4, row=10, padx=2, pady=2)
        
        self.entryNcapash = ttk.Entry(self.disenio_cortante)
        self.entryNcapash.grid(column=5, row=10, padx=2, pady=2)
        
        # SE CREA CAJA DONDE IRA EL VALOR DE LA SEPARACIÓN DE BARRAS DEL ACERO HORIZONTAL        
        self.separación_horizontal=ttk.Label(self.disenio_cortante, text="Separación horizontal: ")
        self.separación_horizontal.grid(column=4, row=11, padx=2, pady=2)
        
        self.entrySeparacionHorizontal = ttk.Label(self.disenio_cortante)
        self.entrySeparacionHorizontal.grid(column=5, row=11, padx=2, pady=2)
        
        self.unidades_separación_horizontal = ttk.Label(self.disenio_cortante, text="cm")
        self.unidades_separación_horizontal.grid(column=6, row=11, padx=2, pady=2)
           
        # SE CREA LA LISTA DESPLEGABLE PARA EL NÚMERO DEL ACERO
        self.lista_aceroh = ttk.Combobox(self.disenio_cortante,state="readonly")
        self.lista_aceroh.grid(column=5, row=9, padx=2, pady=2)


        # TITULO INTRODUCTORIO AL CALCULO DE REFUERZO DE ACERO VERTICAL
        self.LabelTituloPv = tk.Label(self.disenio_cortante,text="Refuerzo Acero Vertical :", fg="red")
        self.LabelTituloPv.grid(column=4, row=12, padx=2, pady=2)

        # SE CREA CAJA DONDE IRA EL VALOR DE LA CUANTIA VERTICAL
        self.pv=ttk.Label(self.disenio_cortante, text="ρv (Cuantía Vertical)")
        self.pv.grid(column=4, row=13, padx=2, pady=2)
        
        self.entrycalculoPv=ttk.Label(self.disenio_cortante, state=DISABLED, width="8")
        self.entrycalculoPv.grid(column=5, row=13, padx=2, pady=2)
        
        # SE CREA CAJA DONDE SE ESCOGE LA BARRA A EMPLEAR EN EL REFUERZO VERTICAL
        
        self.acero_vertical=ttk.Label(self.disenio_cortante, text="N° Barra de acero: ")
        self.acero_vertical.grid(column=4, row=14, padx=2, pady=2)
        
        #SE CREA CAJA DONDE VA CONTENIDO EN NUMERO DE CAPAS QUE SE EMPLEARAN
        
        self.nCapasV=ttk.Label(self.disenio_cortante, text="Número de capas: ")
        self.nCapasV.grid(column=4, row=15, padx=2, pady=2)
        
        self.entryNcapasv = ttk.Entry(self.disenio_cortante)
        self.entryNcapasv.grid(column=5, row=15, padx=2, pady=2)
        
        # SE CREA CAJA DONDE IRA EL VALOR DE LA SEPARACIÓN DE BARRAS DEL ACERO VERTICAL        
        self.separación_vertical=ttk.Label(self.disenio_cortante, text="Separación vertical: ")
        self.separación_vertical.grid(column=4, row=16, padx=2, pady=2)
        
        self.entrySeparacionVertical = ttk.Label(self.disenio_cortante)
        self.entrySeparacionVertical.grid(column=5, row=16, padx=2, pady=2)
        
        self.unidades_separación_vertical = ttk.Label(self.disenio_cortante, text="cm")
        self.unidades_separación_vertical.grid(column=6, row=16, padx=2, pady=2)
        
        # SE CREA LA LISTA DESPLEGABLE PARA EL NÚMERO DEL ACERO
        self.lista_acerov = ttk.Combobox(self.disenio_cortante,state="readonly")
        self.lista_acerov.grid(column=5, row=14, padx=2, pady=2)
        
        # SE CREA CAJA DE VERIFICACIÓN DE ESBELTEZ Y CONTROL DEL DISEÑO
        self.check2 = ttk.Label(self.disenio_cortante, text="Esbeltez")
        self.check2.grid(column=4, row=17, padx=2, pady=2)
        
        self.labelcheck2 = ttk.Label(self.disenio_cortante, state=DISABLED, width="20")
        self.labelcheck2.grid(column=5, row=17, padx=2, pady=2)
 
    def crear_elementos_Flexion(self):
        
        # SE CREA EL CUADRO DONDE DONDE IRÁN CONTENIDOS LOS DATOS INICIALES PARA EL DISEÑO
        self.datos_flexion = ttk.LabelFrame(self, text = "Diseño a flexion: ")
        self.datos_flexion.grid(column=7, row=0, padx=5, pady=10)
        
        # TITULO VERIFICACION DE LOS ESFUERZOS 
        self.LabelEsfuerzos = tk.Label(self.datos_flexion,text="Verificación de Esfuerzos: ", fg="red")
        self.LabelEsfuerzos.grid(column=7, row=1, padx=2, pady=2)    
        
        # SE CREAN CAJAS DONDE IRÁ EL ESFUERZO QUE RESISTEN LOS MATERIALES POR SIMPLES PROPIEDADES MECÁNICAS
        self.fcResistente = ttk.Label(self.datos_flexion, text="Resistencia del material:")        
        self.fcResistente.grid(column=7, row=2, padx=2, pady=2)
        
        self.unidadesfcResistente=ttk.Label(self.datos_flexion, text="MPa")
        self.unidadesfcResistente.grid(column=9, row=2, padx=2, pady=2)
        
        self.entryfcResistente = ttk.Label(self.datos_flexion, state=DISABLED, width="8")
        self.entryfcResistente.grid(column=8, row=2, padx=2, pady=2)        
        
        # SE CREAN CAJAS DONDE IRÁ EL ESFUERZO QUE RESISTEN EL ELEMENTO
        
        self.fcElemento = ttk.Label(self.datos_flexion, text="Esfuerzo que recibe el elemento:")        
        self.fcElemento.grid(column=7, row=3, padx=2, pady=2)
        
        self.unidadesfcElemento=ttk.Label(self.datos_flexion, text="MPa")
        self.unidadesfcElemento.grid(column=9, row=3, padx=2, pady=2)
        
        self.entryfcElemento = ttk.Label(self.datos_flexion, state=DISABLED, width="8")
        self.entryfcElemento.grid(column=8, row=3, padx=3, pady=2)     
        
        
        # SE CREAN CAJAS DONDE SE REALIZA EL CHEQUEO DE ELEMENTOS DE BORDE
        
        self.elementoBorde = ttk.Label(self.datos_flexion, text="¿Elementos de borde? :")        
        self.elementoBorde.grid(column=7, row=4, padx=2, pady=2)

        self.entryelementoBorde = ttk.Label(self.datos_flexion, state=DISABLED, width="20")
        self.entryelementoBorde.grid(column=8, row=4, padx=3, pady=2)  
        
        # SE CREA TITULO DE CARACTERISTICAS GEOMETRICAS DEL ELEMENTO DE BORDE
        
        self.LabelEb = tk.Label(self.datos_flexion,text="Características Geometricas EB: ", fg="red")
        self.LabelEb.grid(column=7, row=5, padx=2, pady=2)  

        # SE CREAN CAJAS DONDE IRÁ EL LARGO DEL ELEMENTO DE BORDE
    
        self.X = ttk.Label(self.datos_flexion, text="Largo EB:")        
        self.X.grid(column=7, row=6, padx=2, pady=2)
                    
        self.unidadesX=ttk.Label(self.datos_flexion, text="m")
        self.unidadesX.grid(column=9, row=6, padx=2, pady=2)
                    
        self.entryX = ttk.Entry(self.datos_flexion, width="20")
        self.entryX.grid(column=8, row=6, padx=3, pady=2)     
      
        # SE CREAN CAJAS DONDE IRÁ EL ANCHO DEL ELEMENTO DE BORDE
    
        self.B = ttk.Label(self.datos_flexion, text="Ancho EB:")        
        self.B.grid(column=7, row=7, padx=2, pady=2)
                    
        self.unidadesB=ttk.Label(self.datos_flexion, text="m")
        self.unidadesB.grid(column=9, row=7, padx=2, pady=2)
                    
        self.entryB = ttk.Entry(self.datos_flexion, width="20")
        self.entryB.grid(column=8, row=7, padx=3, pady=2)     
      
        
      #SE CREA CAJA DONDE IRÁ EL AREA DEL ELEMENTO DE BORDE PROPUESTO
        
        self.AgBorde = ttk.Label(self.datos_flexion, text="Área EB:")        
        self.AgBorde .grid(column=7, row=8, padx=2, pady=2)
                    
        self.unidadesAgBorde =ttk.Label(self.datos_flexion, text="m2")
        self.unidadesAgBorde .grid(column=9, row=8, padx=2, pady=2)
                    
        self.entryAgBorde  = ttk.Label(self.datos_flexion, width="8")
        self.entryAgBorde .grid(column=8, row=8, padx=3, pady=2)  
        
        #TITULO DEL REFUERZO DE LOS ELEMENTOS DE BORDE
        
        self.LabelRefuerzoEb = tk.Label(self.datos_flexion,text=" Refuerzo en los Elementos de Borde: ", fg="red")
        self.LabelRefuerzoEb.grid(column=7, row=9, padx=2, pady=2)  
        
        #SE CREA CAJA DONDE IRÁ EL ÁREA DE ACERO DE REFUERZO DE LOS ELEMENTOS DE BORDE
        
        self.AstBorde = ttk.Label(self.datos_flexion, text="Área de acero EB (Ast):")        
        self.AstBorde .grid(column=7, row=10, padx=2, pady=2)
                    
        self.unidadesAstBorde =ttk.Label(self.datos_flexion, text="m2")
        self.unidadesAstBorde .grid(column=9, row=10, padx=2, pady=2)
                    
        self.entryAstBorde  = ttk.Label(self.datos_flexion, width="8")
        self.entryAstBorde .grid(column=8, row=10, padx=3, pady=2)  
        
        #SE CREA CAJA DONDE IRÁ LA CUANTÍA DE LOS ELEMENTOS DE BORDE
        
        self.pBorde = ttk.Label(self.datos_flexion, text="Cuantía de Acero (ρ): ")        
        self.pBorde .grid(column=7, row=11, padx=2, pady=2)
        
        self.unidadespBorde =ttk.Label(self.datos_flexion, text="%")
        self.unidadespBorde .grid(column=9, row=11, padx=2, pady=2)
                    
        self.entrypBorde  = ttk.Label(self.datos_flexion, width="8")
        self.entrypBorde .grid(column=8, row=11, padx=3, pady=2)  
        
        # SE CREA CAJA DONDE IRA EL NUMERO DE BARRA QUE SELECCIONE EL USUARIO PARA EL REFUERZO DE LOS ELEMENTOS DE BORDE
        
        self.barraEb = ttk.Label(self.datos_flexion, text="N° Barra de acero: ")        
        self.barraEb .grid(column=7, row=12, padx=2, pady=2)
        
        self.entrybarraEb  = ttk.Label(self.datos_flexion, width="8")
        self.entrybarraEb .grid(column=8, row=12, padx=3, pady=2)  
        
        #SE CREA CAJA DONDE VA EL NUMERO DE BARRAS QUE SE UTILIZAN EN EL ELEMENTO DE BORDE
        
        self.NbarraEb = ttk.Label(self.datos_flexion, text="Cantidad de barras de acero (#): ")        
        self.NbarraEb .grid(column=7, row=13, padx=2, pady=2)
        
        self.entryNbarraEb  = ttk.Label(self.datos_flexion, width="8")
        self.entryNbarraEb .grid(column=8, row=13, padx=3, pady=2)  
        
        # SE CREA LA LISTA DESPLEGABLE PARA EL NÚMERO DEL ACERO A FLEXION ELEMENTOS DE BORDE
        self.lista_aceroFlex = ttk.Combobox(self.datos_flexion,state="readonly")
        self.lista_aceroFlex.grid(column=8, row=12, padx=2, pady=2)

        """-------------------------------------------------------------------------------
        -------------------------------------------------------------------------------"""
        # BOTÓN DE CÁLCULO
        self.boton = ttk.Button(self, text="Calcular", command=self.get_values)
        self.boton.grid(column=4, row=12)
        
        # BOTÓN VENTANA 2
        self.boton = ttk.Button(self, text="Nueva ventana", command=self.abrir_ventana2)
        self.boton.grid(column=6, row=12)


"""-----------------------------------------------------------------------------------
PROGRAMA PRINCIPAL: MAIN
-----------------------------------------------------------------------------------"""
if __name__ == "__main__":   
     
    interface = Tk()
    interface.wm_title("Diseño de Muros")
    app = Aplicacion(interface)
    interface.mainloop()