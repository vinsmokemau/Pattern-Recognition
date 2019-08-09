"""Recognize the text of an image."""
import cv2
import numpy as np
from PIL import Image
from pytesseract import image_to_string


def get_string(img_path):
    """Get the string of an image."""
    # Read image with opencv
    img = cv2.imread(img_path)

    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Write image after removed noise
    cv2.imwrite("removed_noise.png", img)

    #  Apply threshold to get image with only black and white
    # img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    # Write the image after apply opencv to do some ...
    cv2.imwrite("thres.png", img)

    # Recognize text with tesseract for python
    result = image_to_string(Image.open("thres.png"))

    # Remove template file
    # os.remove(temp)

    return result


print('--- Start recognize text from image ---')
print(get_string("cont.jpg"))
print("------ Done ------")
