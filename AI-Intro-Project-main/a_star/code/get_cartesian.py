WIDTH = 20.7
HIGH =20.7
PIXEL_WIDTH = 375
PIXEL_HIGH = 375

def pixel_to_cartesian(point:tuple):
    # para este caso la imagen es de 375 x 375 pixeles
    # 375 pixeles representan 20.7cm
    pixel_x, pixel_y = point
    cart_x = round(pixel_x * WIDTH / PIXEL_WIDTH, 2)
    cart_y = round(pixel_y * HIGH / PIXEL_HIGH, 2)
    return cart_x, cart_y

file = open('cartesian_path.txt', 'w')

with open('coordenadas.txt', 'r') as f:
    for line in f:
        x, y = [int(data) for data in line.split(', ')]
        cart_x, cart_y = pixel_to_cartesian((x, y))
        print('{}, {}'.format(cart_x, cart_y), file=file)

file.close()