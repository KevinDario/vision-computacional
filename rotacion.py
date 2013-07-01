from PIL import Image
from sys import argv


def cambiaColor(imagen):

	width, height = imagen.size

	print (width, height)

	pixels = imagen.load()

	for x in range(width):
		for y in range(height):
			r, g, b, a = pixels[x, y]
			pixels[x, y] = b, g, r, a

	imagen.show()

def grises(imagen):

	width, height = imagen.size

	imagen = imagen.convert('RGB')

	pixels = imagen.load()

	for x in xrange(width):
		prom = 0
		for y in xrange(height):
			r, g, b = pixels[x, y]
			prom = (r + b + g) / 3
			pixels[x, y] = prom, prom, prom

	imagen.show()


def bordes():
	robertsx = [(0, 1), (-1, 0)]
	robertsy = [(1, 0), (0, -1)]


def rotar(imagen):

	rotada = imagen.rotate(180)

	rotada.save(nombre.split('.', 1)[0] + '-rotada.png')
	rotada.show()


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

	while True:
		opcion = raw_input('Opcion: ')

		if opcion == 'r':
			resize(imagen)
		elif opcion == 'g':
			grises(imagen)
		elif opcion == 'c':
			cambiaColor(imagen)
		elif opcion == 'ro':
			rotar(imagen)
		else:
			print ('No existe esta opcion. (Disponibles: r, g, c, ro')

main()
