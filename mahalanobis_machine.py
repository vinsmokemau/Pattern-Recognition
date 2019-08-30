"""."""
from skimage import io

import numpy as np

import matplotlib.pyplot as plt

from distances.distances import mahalanobis_distance

image = io.imread('img1_opt.jpg')

[rows, columns, layers] = image.shape

means = []
covariances = []
for i in '1234':
    plt.figure(i)
    plt.imshow(image)

    positions = np.uint32(plt.ginput(0, 0))

    values = image[positions[:, 1], positions[:, 0], :]
    means.append(np.mean(values, axis=0))
    covariances.append(np.cov(values.T, ddof=1))

out = np.zeros([rows, columns], dtype=np.uint8())

scales = [i for i in range(0, 256, (256 // len(means)))]

for row in range(rows):
    for column in range(columns):
        pixel = image[row, column, :]
        distances = []
        for mean, covariance in zip(means, covariances):
            distances.append(mahalanobis_distance(pixel, mean, covariance))
        pos = np.argmin(distances)
        out[row, column] = scales[pos]

plt.figure(5)
plt.imshow(out)
plt.show()
