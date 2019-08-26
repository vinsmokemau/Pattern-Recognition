"""."""
from skimage import io
from skimage.color import rgb2gray
from skimage.morphology import binary

import numpy as np

import matplotlib.pyplot as plt

image = io.imread('placa.jpg')
gray = rgb2gray(image)
plt.figure(1)
plt.imshow(gray, cmap='gray')

binary_img = gray < 0.4
plt.figure(2)
plt.imshow(binary_img, cmap='gray')

sum_by_rows = np.sum(binary_img, axis=1)
plt.figure(3)
plt.plot(sum_by_rows)

crop = binary_img[125:340, :]
plt.figure(4)
plt.imshow(crop, cmap='gray')

sum_by_cols = np.sum(crop, axis=0)
plt.figure(5)
plt.plot(sum_by_cols)

crop_in_crop1 = crop[:, 200:300]
plt.figure(6)
plt.imshow(crop_in_crop1, cmap='gray')

crop_in_crop2 = crop[:, 400:500]
crop_in_crop2 = binary.binary_opening(crop_in_crop2)
plt.figure(7)
plt.imshow(crop_in_crop2, cmap='gray')

graph = []
rows, columns = crop_in_crop2.shape
for row in range(rows):
    for column in range(columns):
        if crop_in_crop2[row, column] == 1:
            graph.append(column)
            break

for row in range(rows):
    for column in range(columns - 1, 0, -1):
        if crop_in_crop2[row, column] == 1:
            graph.append(column)
            break
plt.figure(8)
plt.plot(graph)

plt.show()
