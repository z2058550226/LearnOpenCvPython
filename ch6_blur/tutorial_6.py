import cv2 as cv
import numpy as np


def blur_demo(image):
    """均值模糊"""
    dst = cv.blur(image, (1, 15))
    cv.imshow('blur_demo', dst)


def median_blur_demo():
    """中值模糊可以去掉椒盐躁点"""
    leno = cv.imread('../res/leno.png')
    cv.imshow('leno', leno)
    dst = cv.medianBlur(leno, 5)
    cv.imshow('median_blur_demo', dst)


def custom_blur_demo():
    kernel = np.ones([5, 5], np.float32) / 25  # 创建一个每一个元素都是1/25的矩阵作为核
    leno = cv.imread('../res/leno.png')
    cv.imshow('leno', leno)
    dst = cv.filter2D(leno, -1, kernel)
    cv.imshow('custom_blur_demo', dst)


print("----- Hello Python -----")
src = cv.imread("../res/in_leaves.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
# blur_demo(src)
# median_blur_demo()
custom_blur_demo()

cv.waitKey(0)
cv.destroyAllWindows()
