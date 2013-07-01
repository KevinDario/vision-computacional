#Libreria de numpy se trae como np
import numpy as np
#Libreria de Tkinter para interfaz grafica
import Tkinter
#libraria de PIL se importa ImageDraw
from PIL import ImageDraw
#libreria de Image
import Image
#libreria de ImageTk
import ImageTk
#libreria de sys importa argv
from sys import argv
#se importa la libreria tiempo
import time
 
#es la funcion que hace la convolucion tomando 
#como parametro imagen y la mascara
def convolucion(imagen, h):
#toma el ancho y altura de imagen
    iwidth, iheight = imagen.size
#toma la imagen en escala de grises
    imagen = imagen.convert('L')
#carga la imagen para que pueda ser manipulada
    im = imagen.load()
#toma los renglones y filas de la mascara
    mheight, mwidth = h.shape
#imprime el tamanio de imagen
    print "Imagen size: ",imagen.size
#imprime el tamanio de la mascara
    print "H: ",h.shape
#crea una matriz de zeros dado el ancho y altura de la imagen
    g = np.zeros(shape=(iheight, iwidth))
#recorre la altura y anchura
    for x in xrange(iheight):
        for y in xrange(iwidth):
#inicializa en 0 sum
            sum = 0.0
#recorre las filas y columnas de la mascara
            for j in xrange(mheight):
                zj = ( j - ( mheight / 2 ) )
                for i in xrange(mwidth):
                    zi = ( i - ( mwidth / 2 ) )
# se realiza la convolucion
                    try:
                        sum += im[y + zi, x + zj] * h[i,j]
                    except:
                        pass
            print x, y
#se reemplaza el pixel por la convolucion
            g[x,y] = sum
    print "Convolucion"
    print g
#regresa una matriz
    return g
 
#crea el efecto de escala de grises en una imagen
# toma como parametro la imagen
def escalaDeGrises(im):
#toma el ancho y altura de la imagen
    width, height = im.size
# se imprimen las proporciones de la imagen
    print width, height
# se toma en RGB la imagen
    im = im.convert('RGB')
# se carga la imagen para una facil manipulacion
    pix = im.load()
#inicializa en 0 el promedio
    promedio = 0.0
#se recorre la altura y ancho de la imagen
    for y in xrange(height):
            for x in xrange(width):
#se guarda el pixel con variables r, g, b
                r, g, b = pix[x, y]
# se promedian
                promedio = (r+g+b)/3.0
#se toman los valores absolutos
                pix[x, y] = int(promedio), int(promedio), int(promedio)
# se crea un arreglo de los pixeles
    data = np.array(im)
#se crea una imagen apartir del arreglo de pixeles
    im2 = Image.fromarray(data)
#regresa imagen
    return im2
 
# crea una imagen nueva apartir de una matriz
def nuevaImagen(matriz):
#toma filas y columnas de la matriz
    height, width = matriz.shape
#imprime las proporciones de la matriz
    print matriz.shape
#crea una imagen nueva en escala de grises
    imagen = Image.new(mode='L', size =(width,height))
#carga la imagen para una manipulacion facil
    im = imagen.load()
#imprime las proporciones de la imagen
    print imagen.size
#recorre la altura y ancho de la imagen
    for x in xrange(height):
        for y in xrange(width):
#vacia el valor de la matriz a la imagen segun las coordenadas
            im[y, x] = matriz[x, y]
#se crea un arreglo de la imagen
    data = np.array(imagen)
# se imprime arreglo
    print data
#se crea una nueva imagen apartir de los datos
    im = Image.fromarray(data)
#nos regresa la imagen
    return im
 
#crea una binarizacion de una imagen
#toma como parametro una imagen
def binarizacion(imagen):
#toma el ancho y altura de la imagen
    width, height = imagen.size
#convierte en escala de grises la imagen
    imagen = imagen.convert('L')
#carga la imagen para una manipulacion faci.
    im = imagen.load()
#recorre la altura y ancho de la imagen
    for x in xrange(height):
        for y in xrange(width):
#toma el valor del pixel segun la coordenada de la imagen
            pixel = im[y, x]
#si el valor del pixel es menor a 3 entonces se hace negro
            if pixel < 3:
                im[y, x] = 0
            else:
#si no entonces se hace blanco
                im[y, x] = 255
#se guarda la imagen como matriz
    data = np.array(imagen)
#se crea la imagen apartir de la matriz
    im = Image.fromarray(data)
#nos regresa la imagen
    return im
 
def main():
#abre una imagen segun el paramtetro dado argv
    imagen = Image.open(argv[1])
#se guarda en variable original
    original = imagen
#se crea la escala de grises de la imagen
    escalaGrises = escalaDeGrises(imagen)
#se crean las mascaras de prewitt para x y para y
    px = np.array([[-1,0,1], [-1,0,1], [-1,0,1]])
    py = np.array([[1,1,1], [0,0,0], [-1,-1,-1]])
#se toma tiempo
    t1 = time.time()
#se hace la convolucion para x y para y
#para luego sacar el cuadrado de ellas
    gx = convolucion(escalaGrises, px)
    gx = gx ** 2
    gy = convolucion(escalaGrises, py)
    gy = gy ** 2
#se saca la suma y raiz cuadrado de gx y gy
#g es la matriz resultante que ya ha filtrado
# los bordes
    g = (gx + gy ) ** 1.0/2.0
    print g
#se toma el minimo y el maximo de la matriz g
    min = np.min(g)
    max = np.max(g)
#se toman las proporciones de la matriz g
    h, w = g.shape
#se crea una matriz de unos con las proporciones de g
    minimos = np.ones(shape=(h, w))
#se multiplica la matriz de unos por el minimo
    minimos *= min
#se resta g - min
    g = g - min
    print "Restando el minimo", g
#se divide g entre la resta de max - min
    g = g / (max - min)
    print "Dividiendo el max-min",g
#nos da como resultado valores entre 1.0 y 0.0
    print "Max: ",np.max(g)," Min: ",np.min(g)
#se repite lo mismo pero enlugar de multiplicar por el
#minimo se multiplica la matriz por una matriz de 255
    bn = np.ones(shape=(h, w))
    bn *= 255
    g = g * bn
#obtenemos valores entre 0 y 255
    print "Max: ",np.max(g)," Min: ",np.min(g)
#se crea la imagen apartir de la matriz
    imagen_nueva = nuevaImagen(g)
# se binariza la matriz
    imagen_binaria = binarizacion(imagen_nueva)
#se muestran en interfaz grafica la matriz
    root = Tkinter.Tk()
    tkimageModf = ImageTk.PhotoImage(imagen_nueva)
    tkimageOrig = ImageTk.PhotoImage(imagen_binaria)
    Tkinter.Label(root, image = tkimageModf).pack(side="left")
    Tkinter.Label(root, image = tkimageOrig).pack(side="right")
    t2 = time.time()
    print "Tiempo TOTAL: ",t2-t1," segundos"
    root.mainloop()
main()