from PIL import Image
from numpy import array, zeros
from sys import argv
from math import fabs


RobertsX = array([[0, 1], [-1, 0]])
RobertsY = array([[1, 0], [0, -1]])
SobelX = array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
SobelY = array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
PrewittX = array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
PrewittX = array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])

mascaras = {'rx':array([[0, 1], [-1, 0]]), 'ry':array([[1, 0], [0, -1]]), \
			'sx':array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]), 'sy':array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]]), \
			'px':array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]), 'py':array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])}


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

def convolucion(imagen, mascara):
	width, height = imagen.size
	pixels = imagen.load()

	valores = dict()

	for x in xrange(width):
		prom = 0
		for y in xrange(height):

			valor = suma = 0

			for xm in xrange(len(mascara[0])):
				for ym in xrange(len(mascara[0])):
					try:
						valor = mascara[xm][ym] * pixels[x + (xm-len(mascara[0])/2), y + (ym-len(mascara[0])/2)][0]

					except:
						pass

					suma += valor

			valores[x, y] = suma

	return valores



def normalizar(valores, width, height):

	maxi = mini = 0

	for x, y in valores:
		if valores[x, y] < mini:
			mini = valores[x, y]
		if valores[x, y] > maxi:
			maxi = valores[x, y]

	imagen = Image.new('RGB', (width, height))
	pixeles = imagen.load()

	l = fabs(mini) + fabs(maxi) * 1.0

	for x, y in valores:

		p = (valores[x, y] - mini) / l
		p = int(p * 255)

		pixeles[x, y] = p, p, p

	imagen.show()



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
		opcion = raw_input('Mascara: ')

		if opcion in mascaras:

			valores = convolucion(imagen, mascaras[opcion])
			width, height = imagen.size
			normalizar(valores, width, height)

		else:
			print "Esa mascara no esta disponible. (Disponibles: rx, ry, sx, sy, px, py)"

main()