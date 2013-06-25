from PIL import Image

nombre = 'wink.png'

imagen = Image.open(nombre)
imagen.show()

rotada = imagen.rotate(180)

rotada.save(nombre.split('.', 1)[0] + '-rotada.png')
rotada.show()
print 'hola'
