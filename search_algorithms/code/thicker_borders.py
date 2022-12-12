# GENERA LA IMAGEN CON GROSOR
import numpy as np
import cv2
from PIL import Image

path_ = 'img/borderless.png'
img_pil3 = Image.open(path_)

# imagen binarizada formato RGB
picture = Image.new('RGB', img_pil3.size)
for i in range(img_pil3.size[0]):
    for j in range(img_pil3.size[1]):
        color = img_pil3.getpixel((i, j))
        if color < (100, 100, 100):
            picture.putpixel((i, j), (0, 0, 0))
        else:
            picture.putpixel((i, j), (255, 255, 255))

# imagen binarizada 0-1
img_np_binary = np.zeros(picture.size)
for i in range(picture.size[0]):
    for j in range(picture.size[1]):
        color = picture.getpixel((i, j))
        if color == (0, 0, 0):
            img_np_binary[i][j] = 0
        if color == (255, 255, 255):
            img_np_binary[i][j] = 1

img_np_binary_copy = img_np_binary[:]

black_points = []
for i in range(img_np_binary_copy.shape[0]):
    for j in range(img_np_binary_copy.shape[1]):
        if img_np_binary_copy[i][j] == 0:
            black_points.append((i, j))

THICK = 17 # pixeles de grosor
for bp in black_points:
    x, y = bp
    # si el de la izquierda es negro pero el de la derecha no
    if (x-1, y) in black_points and (x+1, y) not in black_points:
        # poner los siguientes THICK a la derecha de negro
        img_np_binary_copy[x: x+THICK+1, y] = 0
        # for i in range(x, x+THICK+1):
        #     img_np_binary_copy[i, y] = 0
    # si el de la derecha es negro px-THICK: x, yero el de la izquierda no
    elif (x+1, y) in black_points and (x-1, y) not in black_points:
        # poner los sigueintes THICK a la izquierda de blanco
        img_np_binary_copy[x-THICK: x, y] = 0
        # for i in range(x-THICK, x+1):
        #     img_np_binary_copy[i, y] = 0        
    # elif (x+1, y) not in black_points and (x-1, y) not in black_points:
    #     img_np_binary_copy[x-THICK: x+THICK+1, y] = 0
    # elif el de arriba es negro pero el de abajo no
    elif (x, y+1) in black_points and (x, y-1) not in black_points:
        # poner el de abajo como negro
        img_np_binary_copy[x, y: y+THICK+1] = 0
    # elif el de abajo es negro pero el de arriba no
    elif (x, y-1) in black_points and (x, y+1) not in black_points:
        img_np_binary_copy[x, y-THICK: y] = 0

GUARDAR = True
if GUARDAR:
    im = Image.new('1', img_np_binary_copy.shape)
    pixels = im.load()
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            if img_np_binary_copy[i][j].astype(np.int64) == 1:
                pixels[i, j] = 1
            else:
                pixels[i, j] = 0
    im.save('thicker_img.png')
else:
    cv2.imshow('thicker', img_np_binary_copy)
    cv2.waitKey(0)
