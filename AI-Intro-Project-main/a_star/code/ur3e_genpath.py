file = open('ur3e_path.txt', 'w')

ORIGEN_X =  142.62 / 1000 # mm -> m
ORIGEN_Y = -153.30 / 1000 # mm -> m

array = []
with open('cartesian_path.txt', 'r') as f:
    for line in f:
        x, y = [float(data) for data in line.split(', ')]
        cart_x = x / 100 + ORIGEN_X
        cart_y = - y / 100 + ORIGEN_Y

        point = [round(cart_x, 4), round(cart_y, 4)]
        array.append(point)
        print(point, file=file, end=", \n")
    #print(array, sep='\n', file=file)
    print(len(array))
file.close()