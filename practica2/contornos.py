"""."""
from skimage import io
from skimage.color import rgb2gray

import matplotlib.pyplot as plt

image = io.imread('unos/uno5.jpg')
gray = rgb2gray(image)
[rows, columns] = gray.shape

for row in range(rows):
    for column in range(columns):
        if gray[row, column] > 100:
            gray[row, column] = 255
        else:
            gray[row, column] = 0

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

cero_media = [14, 11, 10, 9, 9, 8, 7, 7, 6, 6, 6, 6, 5, 6, 8, 9, 13, 13, 14, 17, 19, 20, 20, 21, 21, 20, 20, 19]
uno_media = [14, 14, 14, 13, 13, 13, 13, 13, 12, 12, 12, 12, 13, 13, 12, 12, 12, 12, 12, 12, 15, 15, 15, 15, 15, 15, 15, 15, 15, 14, 15, 15, 14, 14, 14, 14, 14, 14, 14, 13]
ceros1 = [14, 14, 14, 14, 14, 14, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 15, 15, 15, 15]
ceros2 = [16, 15, 15, 15, 15, 14, 14, 14, 13, 13, 13, 13, 13, 13, 12, 12, 12, 12, 12, 12, 16, 17, 17, 16, 16, 16, 16, 15, 15, 15, 15, 15, 14, 14, 14, 14, 14, 14, 14, 13]
ceros3 = [12, 11, 10, 10, 10, 11, 11, 11, 11, 12, 12, 13, 14, 14, 14, 14, 14, 14, 15, 15, 13, 14, 14, 14, 14, 14, 15, 15, 15, 15, 17, 17, 17, 17, 17, 18, 18, 18, 18, 17]
ceros4 = [17, 17, 17, 16, 16, 16, 15, 14, 13, 13, 13, 12, 12, 11, 11, 10, 10, 9, 8, 8, 18, 18, 18, 18, 17, 17, 17, 16, 16, 15, 15, 14, 14, 13, 13, 12, 11, 11, 10, 10]

graph2 = []
for c1, c2, c3, c4 in zip(ceros1, ceros2, ceros3, ceros4):
    c = (c1 + c2 + c3 + c4) // 4
    graph2.append(c)

plt.figure(1)
plt.plot(graph)
plt.plot(graph2)
print(graph2)

plt.show()
