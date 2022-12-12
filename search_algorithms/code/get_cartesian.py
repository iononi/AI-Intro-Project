import image_process as img

original_labyrith = img.load_image("img/borderless.png")

WIDTH = 20.7
HIGH =20.7
PIXEL_WIDTH = original_labyrith.shape[0]
PIXEL_HIGH = original_labyrith.shape[1]

def pixel_to_cartesian(point:tuple):
    # para este caso la imagen es de 375 x 375 pixeles
    # 375 pixeles representan 20.7cm
    pixel_x, pixel_y = point
    cart_x = round(pixel_x * WIDTH / PIXEL_WIDTH, 2)
    cart_y = round(pixel_y * HIGH / PIXEL_HIGH, 2)
    return cart_x, cart_y

file = open('cartesian_path.txt', 'w')

with open('coordenadas.txt', 'r') as f:
    w = input('Ingresa el ancho: (default es 20.7): ')
    h = input('Ingresa el alto: (default es 20.7): ')

    try:
        w = float(w) # si la conversion es posible, usala
        h = float(h)
        WIDTH = w
        HIGH = h
    except:
        pass

    for line in f:
        x, y = [int(data) for data in line.split(', ')]
        cart_x, cart_y = pixel_to_cartesian((x, y))
        print('{}, {}'.format(cart_x, cart_y), file=file)

file.close()