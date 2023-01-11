import clases
import tkinter as tk

root = tk.Tk()

margin = 0.23

entry = tk.Entry(root)

entry.pack()

def x_calculator():
    # Entrada
    x = float(entry.get())
    print(x)
    a = clases.muro(x, x*4, x/4, x-10, [x,x],[x,x])
    q = a.calcular()
    # Saída
    print(q) 
    return q

button_calc = tk.Button(root, text="Calculate", command=x_calculator)
button_calc.pack()

root.mainloop()