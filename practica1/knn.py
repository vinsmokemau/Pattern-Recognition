"""."""
from skimage import io

import numpy as np

import matplotlib.pyplot as plt

from classifier.intuitive import intuitive_classifier, euclidian_distance

image = io.imread('img1_opt.jpg')

[rows, columns, layers] = image.shape

classes = intuitive_classifier(image)

neighbors = []

k = 3

for img_class in classes:
    if len(classes[img_class][1]) >= k - 1:
        for neighbor in classes[img_class][1]:
            neighbors.append((neighbor, img_class))

out = np.zeros([rows, columns], dtype=np.uint8())

scales = [i for i in range(0, 256, (256 // len(classes)))]

image = io.imread('img2_opt.jpg')

for row in range(rows):
    for column in range(columns):
        votes = [0 for x in range(len(classes))]
        pixel = image[row, column, :]
        distances = [
            euclidian_distance(pixel, neighbor[0]) for neighbor in neighbors
        ]
        lowers = sorted(distances)[:3]
        indexes = [distances.index(lower) for lower in lowers]
        winner_classes = [neighbors[index][1] for index in indexes]
        for winner_class in winner_classes:
            votes[int(winner_class[-1])] += 1
        pos = np.argmax(np.array(votes))
        out[row, column] = scales[pos]

plt.figure(4)
plt.imshow(out)
plt.show()
