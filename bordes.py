from PIL import Image
from numpy import array, zeros
from sys import argv


RobertsX = array([[0, 1], [-1, 0]])
RobertsY = array([[1, 0], [0, -1]])
SobelX = array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
SobelY = array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
PrewittX = array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
PrewittX = array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])


def grises(imagen):

    width, height = imagen.size
    imagen = imagen.convert('RGB')
    pixels = imagen.load()

    for x in xrange(width):
        for y in xrange(height):
            r, g, b = pixels[x, y]
            prom = (r + b + g) / 3
            pixels[x, y] = prom, prom, prom

    return imagen


def convolucion(imagen, opcion):
    width, height = imagen.size
    pixels = imagen.load()

    valores = dict()
    borde = []

    for x in xrange(width):
        prom = 0
        for y in xrange(height):

            sumaX = 0
            sumaY = 0

            for xm in xrange(len(SobelX[0])):
                for ym in xrange(len(SobelY[0])):
                    try:
                        # valorX = SobelY[xm][ym] * pixels[x + (xm-len(SobelX[0])/2), y + (ym-len(SobelX[0])/2)][0]
                        # valorY = SobelX[xm][ym] * pixels[x + (xm-len(SobelY[0])/2), y + (ym-len(SobelY[0])/2)][0]

                        valorX = SobelX[xm][ym] * pixels[x + xm, y + ym][0]
                        valorY = SobelY[xm][ym] * pixels[x + xm, y + ym][0]

                    except:
                        pass

                    sumaX += valorX
                    sumaY += valorY


            dy = sumaY ** 2
            dx = sumaX ** 2

            g = int((dx+dy) ** (1/2.0))

            print x, y, g

            if g > 255:
                g = 255
                borde.append((x, y))

            if g < 0:
                g = 0

            pixels[x, y] = g, g, g

    visitados = []
    for x, y in borde:
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                print ""
                if x+i < width and y+j < height and x+i > 0 and y+j > 0 and ((x, y)) not in visitados and ((x, y)) in borde:
                    visitados.append((x, y))
                    if opcion == 'a':
                        pixels[x+i, y+j] = 0, 0, 0
                    if opcion == 'e':
                        pixels[x+i, y+j] = 255, 255, 255

    imagen.show()

    return


def main():

    global nombre

    if len(argv) < 2:
        print ('No especificaste la imagen. Usando "wink.png" ')
        nombre = 'wink.png'
        imagen = Image.open(nombre)
    else:
        nombre = argv[1]
        try:
            imagen = Image.open(nombre)
        except:
            print ('No existe esa imagen.')
            return

    imagen = grises(imagen)

    while True:
        opcion = raw_input('Opcion: ')

        if opcion == 'e' or opcion == 'a':

            convolucion(imagen, opcion)

        else:
            print 'Opcion no disponible. (Disponibles: e, a)'

main()