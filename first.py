"""."""
from skimage import data, io

import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from classifier.intuitive import intuitive_classifier

image = io.imread('img1_opt.jpg')

[rows, columns, layers] = image.shape

classes = intuitive_classifier(image)

centers = [classes[img_class][0] for img_class in classes]

salida = np.zeros([rows, columns], dtype=np.uint8())

scales = [i for i in range(0, 256, (256 // len(centers)))]

for row in range(rows):
    for column in range(columns):
        red_pixel = image[row, column, 0]
        green_pixel = image[row, column, 1]
        blue_pixel = image[row, column, 2]
        distances = [
            np.sqrt(
                (int(center[0]) - int(red_pixel))**2 +
                (int(center[1]) - int(green_pixel))**2 +
                (int(center[2]) - int(blue_pixel))**2
            ) for center in centers
        ]
        pos = np.argmin(distances)
        salida[row, column] = scales[pos]

plt.figure(4)
plt.imshow(salida)
plt.show()

'''
[rows, columns, layers] = image.shape

red = image[:, :, 0]
green = image[:, :, 1]
blue = image[:, :, 2]

plt.figure(2)
plt.imshow(image)
plt.show()
'''

"""
plt.figure()
plt.imshow(image)
position = np.uint32(plt.ginput(0, 0))

values = image[position[:, 1], position[:, 0], :]

reds = 0
greens = 0
blues = 0

for value in values:
    reds += value[0]
    greens += value[1]
    blues += value[2]

reds //= len(values)
greens //= len(values)
blues //= len(values)

print(reds, greens, blues)
"""

'''
plt.figure(3)
graph = plt.axes(projection='3d')
graph.scatter3D(red.flatten(), green.flatten(), blue.flatten())
graph.set_xlabel('Red Label')
graph.set_ylabel('Green Label')
graph.set_zlabel('Blue Label')
plt.show()
'''

"""
cla1 = (120, 30, 30)
cla2 = (164, 160, 155)
cla3 = (160, 166, 168)
cla4 = (13, 33, 86)

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
"""
