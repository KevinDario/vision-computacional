from PIL import Image

imagen = Image.open("wink.png")
imagen.show()

rotada = imagen.rotate(180)
rotada.show()
