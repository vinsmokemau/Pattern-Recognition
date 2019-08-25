"""Intuitive Classifier."""
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


def update_center(pixel, center):
    """Update the center of a class."""
    red_difference = (int(center[0]) + int(pixel[0])) // 2
    green_difference = (int(center[1]) + int(pixel[1])) // 2
    blue_difference = (int(center[2]) + int(pixel[2])) // 2
    return np.array(
        [red_difference, green_difference, blue_difference], dtype=np.uint8()
    )


def intuitive_classifier(img):
    """Get the classes of an image by the intuitive proccess."""
    [rows, columns, layers] = img.shape

    classes = {}
    no_classes = 0
    tolerance = 50

    for row in range(0, rows, 100):
        for column in range(0, columns, 100):
            if no_classes == 0:
                class_name = 'class{}'.format(no_classes)
                classes[class_name] = [img[row, column], [img[row, column]]]
                no_classes += 1
            else:
                center_distances = [
                    euclidian_distance(
                        img[row, column], classes[img_class][0]
                    ) for img_class in classes
                ]
                center_distances = np.array(center_distances)
                min_value = np.amin(center_distances)
                if min_value > tolerance:
                    class_name = 'class{}'.format(no_classes)
                    classes[class_name] = [
                        img[row, column], [img[row, column]]
                    ]
                    no_classes += 1
                else:
                    class_possition = np.where(
                        center_distances == min_value
                    )[0][0]
                    class_name = 'class{}'.format(class_possition)
                    updated_center = update_center(
                        img[row, column],
                        classes[class_name][0]
                    )
                    classes[class_name][0] = updated_center
                    classes[class_name][1].append(img[row, column])
    """
    The return gonna be a dictionary with the next structure:
        classes = {
            "class0": [pixel_center, [pixel1, pixel2, pixeln]],
            "classn": [pixel_center, [pixel1, pixel2, pixeln]],
        }."""
    return classes
