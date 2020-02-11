"""File that contain the types of distances."""
import numpy as np


def euclidian_distance(pixel, center):
    """Return the euclidian distance of two pixels."""
    red_difference = int(center[0]) - int(pixel[0])
    green_difference = int(center[1]) - int(pixel[1])
    blue_difference = int(center[2]) - int(pixel[2])
    euclidian_distance = np.sqrt(
        red_difference**2 +
        green_difference**2 +
        blue_difference**2
    )
    return np.uint8(euclidian_distance)


def mahalanobis_distance(pixel, mean, covariance):
    """Return the Mahalanobis distance."""
    x_minus_mu = pixel - mean
    inv_covmat = np.linalg.inv(covariance)
    left_term = np.dot(x_minus_mu, inv_covmat)
    mahal_distance = np.dot(left_term, x_minus_mu.T)
    distance = np.sqrt(mahal_distance)
    return distance
