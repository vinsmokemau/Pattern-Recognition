"""."""
from skimage import io
from skimage.color import rgb2gray

import matplotlib.pyplot as plt

image = io.imread('img_7.jpg')
gray = rgb2gray(image)
[rows, columns] = gray.shape

for row in range(rows):
    for column in range(columns):
        if gray[row, column] > 100:
            gray[row, column] = 255
        else:
            gray[row, column] = 0

plt.figure(1)
plt.imshow(gray, cmap='gray')

graph = []
rows, columns = gray.shape
for row in range(rows):
    for column in range(columns):
        if gray[row, column] == 255:
            graph.append(column)
            break

for row in range(rows):
    for column in range(columns - 1, 0, -1):
        if gray[row, column] == 255:
            graph.append(column)
            break

plt.figure(8)
plt.plot(graph)
print(len(graph))
plt.show()
