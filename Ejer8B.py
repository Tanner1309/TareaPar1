import matplotlib.pyplot as plt
import numpy as np
import math
#se piden los datos necesarios
print("Este programa resuelve la ecuacion f(x)=sin(x)-csc(x)+1")
xl=int(input("Inserte el valor del limite menor: "))
xu=float(input("Inserte el valor del limite mayor: "))
#se obtiene el primer xr
xr=(xl+xu)/2
#se declara la lista donde se guardaran los valores de los errores 
ve=[]
xrr=[]
while True:
    #se evalua en la funcion xl xu y xr
    fxl=math.sin(math.radians(xl))-(1/math.sin(math.radians(xl)))+1
    fxr=math.sin(math.radians(xr))-(1/math.sin(math.radians(xr)))+1
    fxu=math.sin(math.radians(xu))-(1/math.sin(math.radians(xu)))+1
    #se guarda el valor de xr para calcular el error
    xra=xr
    if (fxl*fxr) < 0:
        xu=xr
    elif (fxu*fxr) < 0:
        xl=xr
    xrn=(xl+xu)/2
    #se evalua el error
    e=math.fabs(xrn-xra)
    ve.append(e)
    xrr.append(xrn)
    if e <= 0.00001:
        break
    xr=(xl+xu)/2
#lineas para mostrar el grafico de error
#se pasa la lista a arreglo
vecE=np.array(ve)
vecXr=np.array(xrr)
#se obtiene el tamano del vector 
x=vecE.size
#se crea el vector x
vecX=np.arange(0,x)
print("El resultado mas cercano es:",xr)
#se hace la grafica
plt.plot(vecX,vecE,"r--")
plt.plot(vecX,vecXr,"b--")
#se muestra la grafica
plt.show()