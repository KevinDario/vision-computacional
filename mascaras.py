from numpy import array, zeros
from PIL import Image
from time import time
import math

RobertsX = array([[0, 1], [-1, 0]])
RobertsY = array([[1, 0], [0, -1]])
SobelX = array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
SobelY = array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
PrewittX = array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
PrewittX = array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])





def grises(w,h,pix,im):

    #Recorremos el arreglo de pixeles
    for j in range(h):
        for i in range(w):
            #se suman los valores R,G,B
            #y se promedian al dividirlos entre 3
            prom = sum(pix[i,j])/3
            #el promedio es el nuevo valor de cada canal
            pix[i,j] = (prom,prom,prom)
    im.save('gris.png')
    #im.show()

    return im 
 
def convolucion(im):

    w,h = im.size
    pix = im.load()
    prom = 0  
    suma = 0
    
    #Recorremos la imagen
    for j in range(h):
        for i in range(w):
            sumax = 0
            sumay = 0
	    #Recorremos la mascara
            for x in range(len(SobelX[0])):
                for y in range(len(SobelY[0])):
                    try:
			#Multiplicacion de valores
                        valorx = SobelX[x][y]*pix[i+y,j+x][1]
                        valory = SobelY[x][y]*pix[i+y,j+x][1]
 
                    except:
                        valorx = 0
                        valory = 0
		    #Suma de multiplicaciones
                    sumax = valorx + sumax
                    sumay = valory + sumay
	    #Distancia euclidiana
            xm = pow(sumax,2)
            ym = pow(sumay,2)
            g = int(math.sqrt(xm+ym))
            if g > 255:
                g = 255
            if g < 0:
                g = 0
            pix[i,j] = (g,g,g)
    im.save('prueba.png')
    im.show()

 
def main():
    im = Image.open('wink.png')
    ancho,altura = im.size
    pixels = im.load()
 
    gris = grises(ancho,altura,pixels,im)
    convolucion(gris)
 
main()