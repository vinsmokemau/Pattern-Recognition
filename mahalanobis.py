"""Script to test Mahalanobis distance."""
from skimage import data, io

import numpy as np

import matplotlib.pyplot as plt


def mahalanobis_distance(pixel, mean, covariance):
    """Return the Mahalanobis distance."""
    x_minus_mu = pixel - mean
    inv_covmat = np.linalg.inv(covariance)
    left_term = np.dot(x_minus_mu, inv_covmat)
    mahal_distance = np.dot(left_term, x_minus_mu.T)
    distance = np.sqrt(mahal_distance)
    return distance


# Get an image from skimage
img1 = data.chelsea()

# Get the number of rows, columns and layer of the image
[rows, columns, layers] = img1.shape

# Intialize the plot for the image
plt.figure(1)
plt.imshow(img1)

# Get the test values of the image with the mouse
positions = np.uint32(plt.ginput(0, 0))

# Create an array of the same shape of the image but with zeros
out = np.zeros([rows, columns], dtype=np.uint8())

# Get the exact pixels from the image
values = img1[positions[:, 1], positions[:, 0], :]

# Get the mean of the test values in RGB
mean = np.mean(values, axis=0)

# Get the covariance of the test values
cova = np.cov(values.T, ddof=1)

# Iterate over all the image pixel by pixel
for row in range(rows):
    for column in range(columns):
        pixel = img1[row, column, :]
        distance = mahalanobis_distance(pixel, mean, cova)
        if distance > 5:
            out[row, column] = 125

plt.figure(2)
plt.imshow(out)
plt.show()
