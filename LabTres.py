from PIL import Image
from sys import argv


def redimensionar(imagen, width, height):

	imagen = imagen.convert('RGB')
	imagen.show()

	widthOriginal, heightOriginal = imagen.size
	pixelOriginal = imagen.load()

	nueva = Image.new('RGB', (width, height))
	pixelNueva = nueva.load()

	ratioW = width * 1.0 / widthOriginal
	ratioH = height * 1.0 / heightOriginal

	for x in xrange(width):
		for y in xrange(height):
			nx = int(x/ratioW)
			ny = int(y/ratioH)

			pixelNueva[x, y] = pixelOriginal[nx, ny]

	nueva.show()


def main():

	global nombre

	if len(argv) < 2:
		print ('No especificaste la imagen. Usando "wink.png"')
		nombre = 'wink.png'
		imagen = Image.open(nombre)
	else:
		nombre = argv[1]
		try:
			imagen = Image.open(nombre)
		except:
			print ('No existe esa imagen.')
			return

	width, height = int(argv[2]), int(argv[3])

	redimensionar(imagen, width, height)

main()