"""Euclidain Machine."""
from skimage import io

import numpy as np

import matplotlib.pyplot as plt

from classifier.intuitive import intuitive_classifier

from distances.distances import euclidian_distance

image = io.imread('img1_opt.jpg')

classes = intuitive_classifier(image)

centers = [classes[img_class][0] for img_class in classes]

scales = [i for i in range(0, 256, (256 // len(centers)))]

image = io.imread('img3_opt.jpg')

[rows, columns, layers] = image.shape

salida = np.zeros([rows, columns], dtype=np.uint8())

for row in range(rows):
    for column in range(columns):
        pixel = image[row, column, :]
        distances = [euclidian_distance(pixel, center) for center in centers]
        pos = np.argmin(distances)
        salida[row, column] = scales[pos]

plt.figure(4)
plt.imshow(salida)
plt.show()
