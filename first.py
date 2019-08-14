"""."""
from skimage import data, io

import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

image = io.imread('test.png')

[rows, columns, layers] = image.shape

red = image[:, :, 0]
green = image[:, :, 1]
blue = image[:, :, 2]

'''
plt.figure(2)
plt.imshow(image)
plt.show()
'''

'''
plt.figure()
plt.imshow(image)
position = np.uint32(plt.ginput(0, 0))


value = image[position[:, 1], position[:, 0], :]
'''

'''
plt.figure(3)
graph = plt.axes(projection='3d')
graph.scatter3D(red.flatten(), green.flatten(), blue.flatten())
graph.set_xlabel('Red Label')
graph.set_ylabel('Green Label')
graph.set_zlabel('Blue Label')
plt.show()
'''

cla1 = (0, 0, 0)
cla2 = (237, 28, 36)
cla3 = (178, 0, 214)
cla4 = (0, 180, 127)

salida = np.zeros([rows, columns], dtype=np.uint16())

for row in range(rows):
    for column in range(columns):
        red_pixel = image[row, column, 0]
        green_pixel = image[row, column, 1]
        blue_pixel = image[row, column, 2]
        distance_cla1 = np.sqrt(
            (cla1[0] - red_pixel)**2 +
            (cla1[1] - green_pixel)**2 +
            (cla1[2] - blue_pixel)**2
        )
        distance_cla2 = np.sqrt(
            (cla2[0] - red_pixel)**2 +
            (cla2[1] - green_pixel)**2 +
            (cla2[2] - blue_pixel)**2
        )
        distance_cla3 = np.sqrt(
            (cla3[0] - red_pixel)**2 +
            (cla3[1] - green_pixel)**2 +
            (cla3[2] - blue_pixel)**2
        )
        distance_cla4 = np.sqrt(
            (cla4[0] - red_pixel)**2 +
            (cla4[1] - green_pixel)**2 +
            (cla4[2] - blue_pixel)**2
        )
        pos = np.argmin(
            [distance_cla1, distance_cla2, distance_cla3, distance_cla4]
        )
        if pos == 0:
            salida[row, column] = 0
        elif pos == 1:
            salida[row, column] = 85
        elif pos == 2:
            salida[row, column] = 170
        else:
            salida[row, column] = 255

plt.figure(4)
plt.imshow(salida)
plt.show()
