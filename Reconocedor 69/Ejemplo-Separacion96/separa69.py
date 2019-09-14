# -*- coding: utf-8 -*-
"""
Created on Tue Feb 05 13:47:58 2019

@author: mcs54190
"""
from PIL import Image
from numpy import * 
from pylab import *
from scipy.ndimage import *
from matplotlib.patches import Rectangle
from drawnow import drawnow
import matplotlib.pyplot as mpl
import time

def repite():
    mpl.imshow(block([[A],[B]]))

#<=======================  Primera Parte =================================>#
print ('primera parte del programa: Entrenamiento del sistema')
bin1 = array(Image.open('entrena6.bmp'))
bin2 = array(Image.open('entrena9.bmp'))
figure(1)
imshow(bin1)
figure(2)
imshow(bin2)
#imshow(block([[bin1],[bin2]]))
#---------------------------------------------------------------------------
con8 = generate_binary_structure(2,2)
Ima6, Can6 = label(bin1, structure = con8)
Ima9, Can9 = label(bin2, structure = con8)
#imshow(block([[Ima6],[Ima9]]))
#--------------------------------------------------------------------------
for j in range (1, 3, 1):
    if (j == 1):
        numero = Ima6
        cantidad = Can6
        print('Se procesa el numero 6')
    else:
        numero  = Ima9
        cantidad = Can9
        print('Se procesa el numero 9')
    dato = []
    for i in range (1, cantidad, 1):
        print('Objeto %s de %s' % (i, cantidad))
        s1 = np.where(numero == i, 1, 0)
        s2 = binary_fill_holes(s1).astype(int)
        s3 = np.logical_xor(s1, s2)
        Fil1, Col1 = np.nonzero(s1)
        Fil2, Col2 = np.nonzero(s3)
        objmin = min(Fil2)
        objmax = max(Fil2)
        NFmin  = min(Fil1)
        NFmax  = max(Fil1)
        NCmin  = min(Col1)
        NCmax  = max(Col1)
        medio = (objmax-objmin)/2.0 + objmin
        dato.append((medio-NFmin)/(NFmax-NFmin))
    if (j == 1):
        datos6 = dato
    else:
        datos9 = dato

figure(3)
mpl.hist(datos9, bins = 'auto', alpha=0.75, rwidth=0.3, color = 'r', label='num 9')
mpl.hist(datos6, bins = 'auto', alpha=0.75, rwidth=0.3, color = 'g', label='num 6')
mpl.legend(loc='upper right')

#<=======================  Segunda Parte =================================>#
print ('Segunda parte del programa: Prueba del sistema')
time.sleep(2.0)
umbral = 0.5
prueba = (array(Image.open('prueba69.bmp')))
Ima, Can = label(prueba, structure = con8)
A = zeros_like(Ima)
B = zeros_like(Ima)
figure(4)
mpl.imshow(block([[A],[B]]))

for j in range (1, Can, 1):
    s1 = np.where(Ima == j, 1, 0)
    s2 = binary_fill_holes(s1).astype(int)
    s3 = np.logical_xor(s1, s2)
    Fil1, Col1 = np.nonzero(s1)
    Fil2, Col2 = np.nonzero(s3)
    if (len(Fil2) == 0):
        continue
    objmin = min(Fil2)
    objmax = max(Fil2)
    NFmin  = min(Fil1)
    NFmax  = max(Fil1)
    NCmin  = min(Col1)
    NCmax  = max(Col1)
    medio = (objmax-objmin)/2.0 + objmin
    dato.append((medio-NFmin)/(NFmax-NFmin))
    if (dato[-1] > umbral):
        print ('seis')
        A[Fil1, Col1] = 1
        drawnow(repite)
        time.sleep(1)
    else:
        print ('Nueve')
        B[Fil1, Col1] = 1
        drawnow(repite)
        time.sleep(1)

#figure(3)
#imshow(s1)
#RECT = Rectangle((NCmin, NFmin),NCmax-NCmin, NFmax-NFmin, linewidth = 1, edgecolor = 'r', facecolor = 'none')
#gca().add_patch(RECT)
#for i in range(N6):
#    np.where(L6 == i+1, 1, 0)
    
#rect = Rectangle((H,F), I-H, G-F, linewidth=1, edgecolor='r', facecolor='none')
#mpl.gca().add_patch(rect)
positivo6 = int(input('Cuantos 6,s fueron identificados correctamente: '))
positivo9 = int(input('Cuantos 9,s fueron identificados correctamente: '))
negativo6 = 14.0 - positivo6
negativo9 = 16.0 - positivo9

MatrizConfucion  = [[positivo6, negativo6],[positivo9, negativo9]]
Par = ((positivo9 + positivo6) / (16.0 + 14.0)) * 100
print ('El desempeno del clasificador es = %s %%' %Par)

figure(5)
imshow(prueba)

mpl.show()