import cv2 as cv
import numpy as np


def add_demo(m1, m2):
    """像素相加，前提是这两张图片的宽高相同"""
    dst = cv.add(m1, m2)
    cv.imshow('add_demo', dst)


def subtract_demo(m1, m2):
    """像素相减"""
    dst = cv.subtract(m1, m2)
    cv.imshow('subtract', dst)


def divide_demo(m1, m2):
    dst = cv.divide(m1, m2)
    cv.imshow('divide', dst)


def multiply_demo(m1, m2):
    dst = cv.multiply(m1, m2)
    cv.imshow('multiply', dst)


def logic_demo(m1, m2):
    """逻辑运算，相对简单，这里就是对每一个Mat中的值进行按位运算"""
    dst_and = cv.bitwise_and(m1, m2)
    cv.imshow('logic_and', dst_and)
    dst_or = cv.bitwise_or(m1, m2)
    cv.imshow('logic_or', dst_or)
    dst_xor = cv.bitwise_xor(m1, m2)
    cv.imshow('logic_xor', dst_xor)
    dst_not = cv.bitwise_not(m1, m2)
    cv.imshow('logic_not', dst_not)


def contrast_brightness_demo(image, contrast, brightness):
    height, width, channel = image.shape
    blank = np.zeros([height, width, channel], image.dtype)
    dst = cv.addWeighted(image, contrast, blank, 1 - contrast, brightness)
    cv.imshow('contrast-brightness-demo', dst)


def others(m1, m2):
    """cv::mean会求出整体图像的各个通道的均值(可能有1-4个，没有的通道都为0)，通过这个数据的表征，
    我们能看出颜色的色调(哪个通道均值比较高)、图片的明暗成都(整体均值大小)。
    第二个就是Standard Deviation, 标准差，也叫均方差，这里不是方差Variance。
    这里标准差数据表征了图片的五颜六色的程度(各个通道颜色的差异程度)，也可以理解为对比度"""
    M1, dev1 = cv.meanStdDev(m1)
    M2, dev2 = cv.meanStdDev(m2)
    h, w = m1.shape[:2]
    print(M1)
    print(M2)
    print(dev1)
    print(dev2)
    print('Height: %s, Width: %s' % (h, w))

    img = np.zeros([h, w], np.uint8)
    m, dev = cv.meanStdDev(img)
    print(m)
    print(dev)


print("----- Hello Python -----")
img_linux = cv.imread("../res/linux.png")
img_windows = cv.imread("../res/windows.png")
print(img_linux.shape)
print(img_windows.shape)
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow('image1', img_linux)
cv.imshow('image2', img_windows)

# add_demo(img_linux, img_windows)
# subtract_demo(img_linux, img_windows)
# divide_demo(img_linux, img_windows)
# multiply_demo(img_linux, img_windows)
# others(img_linux, img_windows)
# logic_demo(img_windows, img_linux)

megumi = cv.imread('../res/over_flower.jpg')
cv.imshow('megumi', megumi)
contrast_brightness_demo(megumi, 1.5, 0)

cv.waitKey(0)
cv.destroyAllWindows()
