# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 09:47:55 2023

@author: LASSODS
"""
from tkinter import messagebox, ttk
import tkinter as tk
import clases

class Application(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Combobox")
        
        # self.info_acero = {2:32,3:71,4:129,5:199,6:284,7:387,
        #                    8:510,9:645,10:819,11:1006,14:1452,18:2581}
        
        self.m1 = clases.muro(1, 1, 1, 1, [1,1], [1,1])
        self.aceros = self.m1.info_acero
        
        self.combo = ttk.Combobox(
            self,
            state="readonly",
            values=[i for i in self.aceros.keys()]
        )
        self.combo.place(x=50, y=50)
        self.button = ttk.Button(
            text="Mostrar selección",
            command=self.show_selection
        )
        self.button.place(x=50, y=100)
        main_window.config(width=300, height=200)
        self.place(width=300, height=200)
    def show_selection(self):
        # Obtener la opción seleccionada.
        selection = self.combo.get()
        messagebox.showinfo(
            message=f"La opción seleccionada es: {selection}",
            title="Selección"
        )
main_window = tk.Tk()
app = Application(main_window)
app.mainloop()