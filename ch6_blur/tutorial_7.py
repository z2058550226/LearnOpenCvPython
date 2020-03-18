import cv2 as cv
import numpy as np


def clamp(pv):
    if pv > 255:
        return 255
    if pv < 0:
        return 0
    else:
        return pv


def gaussian_noise(image):
    """高斯噪声"""
    height, width, channels = image.shape
    for row in range(height):
        for col in range(width):
            s = np.random.normal(0, 20, 3)
            blue = image[row, col, 0]
            green = image[row, col, 1]
            red = image[row, col, 2]
            image[row, col, 0] = clamp(blue + s[0])
            image[row, col, 1] = clamp(green + s[1])
            image[row, col, 2] = clamp(red + s[2])
    cv.imshow('noise image', image)


def gaussian_blur_demo(image):
    dst = cv.GaussianBlur(image, (0, 0), 15)
    cv.imshow('gaussian_blur', dst)


print("----- Hello Python -----")
src = cv.imread("../res/in_leaves.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
# gaussian_noise(src)
gaussian_blur_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()
