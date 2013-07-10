from sys import argv
from PIL import Image

""" Detecta las esquinas de las figuras picudas en una imagen. """

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


def esquinas(imagen):

	gris = grises(imagen)
	width, height = imagen.size
	pixel = gris.load()

	pixelNueva = imagen.load()	# Carga la imagen original para marcar las esquinas directamente en ella

	for x in xrange(width):
		for y in xrange(height):
			
			if x > 1 and x != width-1 and y > 1 and y != height-1:
				lista = []
				for vx in [-1, 0, 1]:
					for vy in [-1, 0, 1]:
						valor = pixel[x + vx, y + vy][0]
						lista.append(valor)

				lista = sorted(lista)
				mediana = lista[len(lista) / 2]

				valor = pixel[x, y][0]
				print mediana - valor
				if mediana - valor != 0:
					pixelNueva[x, y] = 0, 255, 0
				else:
					pixelNueva[x, y] = pixelNueva[x, y]
			else:
				pixelNueva[x, y] = pixelNueva[x, y]

	imagen.show()


def main():

	global nombre

	if len(argv) < 2:
		nombre = 'relampago.png'
		print ('No especificaste la imagen. Usando "%s" ' % nombre)
		imagen = Image.open(nombre)
	else:
		nombre = argv[1]
		try:
			imagen = Image.open(nombre)
		except:
			print ('No existe esa imagen.')
			return

	esquinas(imagen)

main()
