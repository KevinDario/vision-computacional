from PIL import Image
from sys import argv


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

	return imagen

def rojos(imagen):

	width, height = imagen.size
	imagen = imagen.convert('RGB')
	pixels = imagen.load()

	for x in xrange(width):
		prom = 0
		for y in xrange(height):
			r, g, b = pixels[x, y]
			prom = (r + b + g) / 3
			pixels[x, y] = 255, prom, prom

	return imagen


def invierteColor(imagen):

	width, height = imagen.size
	imagen = imagen.convert('RGB')
	pixels = imagen.load()

	for x in xrange(width):
		for y in xrange(height):
			r, g, b = pixels[x, y]
			pixels[x, y] = b, g, r

	return imagen


def rotar(imagen):
	""" Rota una imagen en 180 grados y la guarda como "nombre-rotada.png" """

	rotada = imagen.rotate(180)

	rotada.save(nombre.split('.', 1)[0] + '-rotada.png')

	return rotada



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

		if opcion == 'rotar':
			rotar(imagen).show()
		elif opcion == 'grises':
			grises(imagen).show()
		elif opcion == 'rojos':
			rojos(imagen).show()
		elif opcion == 'invertir':
			invierteColor(imagen).show()
		else:
			print ('No existe esta opcion. (Disponibles: grises, rojos, rotar, invertir')

main()
