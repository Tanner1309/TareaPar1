#se importan las librerias necesarias
import matplotlib.pyplot as plt
import numpy as np
import math
#se piden los datos necesarios
print("Este programa resuelve la ecuacion f(x)=ln(x^2+1)-e^(x/2)*cos(pix)")
#se obtiene el primer xr
xl=0.1
xu=0.5
xr=(xl+xu)/2
#se declara la lista donde se guardaran los valores de los errores 
ve=[]
xrr=[]
while True:
    #se evalua en la funcion xl xu y xr
    fxl=math.log1p(xl^2+1)-math.exp(xl/2)*math.cos(3.1416*xl)
    fxr=math.log1p(xr^2+1)-math.exp(xr/2)*math.cos(3.1416*xr)
    fxu=math.log1p(xu^2+1)-math.exp(xu/2)*math.cos(3.1416*xu)
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
print("El resultado mas cercano del primer intervalo es:",xr)    
#Se hace el proceso con el segundo intervalo
xl=-2
xu=-0
xr=(xl+xu)/2
#se declara la lista donde se guardaran los valores de los errores 
ve1=[]
xrr1=[]
xr=xr-((math.log1p(xr^2+1)-math.exp(xr/2)*math.cos(3.1416*xr))/(3.1416*math.exp(x/2)*math.sin(3.1416*xr)-((math.exp(x/2)*math.cos(3.1416*xr))/2)+((2*xr)/(xr*xr+1))))
#se declara la lista donde se guardaran los valores de los errores 
while True:
    #se guarda el valor de xr para calcular el error
    xra=xr
    xrr.append(xr)
    xrn=xr-((math.log1p(xr^2+1)-math.exp(xr/2)*math.cos(3.1416*xr))/(3.1416*math.exp(x/2)*math.sin(3.1416*xr)-((math.exp(x/2)*math.cos(3.1416*xr))/2)+((2*xr)/(xr*xr+1))))
    #se evalua el error
    e=math.fabs(xra-xrn)
    ve.append(e)
    if e <= 0.000001 or e == 0.0:
        break
    xr=xrn
    
    c=c+1

#lineas para mostrar el grafico de error
#se pasa la lista a arreglo
vecE=np.array(ve)
vecXr=np.array(xrr)
vecE1=np.array(ve1)
vecXr1=np.array(xrr1)
#se obtiene el tamano del vector 
x=vecE.size
x1=vecE1.size
#se crea el vector x
vecX=np.arange(0,x)
vecX1=np.arange(0,x1)
print("El resultado mas cercano del segundo intervalo es:",xr)
plt.figure()
plt.subplot(2,2,1)
plt.plot(vecX,vecE, "go--", linewidth=2, markersize=5)
plt.title("$Error1$")
plt.subplot(2,1,2)
plt.plot(vecX,vecXr, "bo-", linewidth=2, markersize=5)
plt.title("$Resultados1$")
plt.subplot(2,2,3)
plt.plot(vecX1,vecE1, "go--", linewidth=2, markersize=5)
plt.title("$Error2$")
plt.subplot(2,1,4)
plt.plot(vecX1,vecXr1, "bo-", linewidth=2, markersize=5)
plt.title("$Resultados2$")