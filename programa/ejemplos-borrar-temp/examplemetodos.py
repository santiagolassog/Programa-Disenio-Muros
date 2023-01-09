import math

def metodoClick():
    print('hice un solo click')
    print(1+1)
    print(math.sin(8))
    nombres('AAA', 'BBBB')
    print(aniosAge(1997,2022))


def nombres(name, lasName):
    print(name + ' ' + lasName)

def aniosAge(anioNaci,FechaActual):
    return FechaActual-anioNaci / 3 

metodoClick()



def metodoClick2():
    print('otro boton click')
    print(27 - aniosAge(1997,2022))

metodoClick2()