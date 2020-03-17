import cv2 as cv
import numpy as np


def split_merge_demo(image):
    """这里讲BGR通道的分离与合并"""
    b, g, r = cv.split(image)
    cv.imshow('blue channel', b)
    cv.imshow('green channel', g)
    cv.imshow('red channel', r)

    image[:, :, 2] = 0
    cv.imshow('no red channel image', image)

    image = cv.merge([b, g, r])
    cv.imshow('merged image', image)


def extract_object_demo():
    """这里演示inRange函数在识别颜色上的作用"""
    capture = cv.VideoCapture("../res/color_space_test_video.mp4")
    while True:
        ret, frame = capture.read()
        if not ret:
            break
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        lower_hsv = np.array([37, 43, 46])
        upper_hsv = np.array([77, 255, 255])
        mask = cv.inRange(hsv, lowerb=lower_hsv, upperb=upper_hsv)
        cv.imshow("video", frame)
        cv.imshow('mask', mask)
        c = cv.waitKey(40)
        if c == 27:
            break


def color_space_demo(image):
    """展示了多种不同颜色空间的转换"""
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow('gray', gray)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    cv.imshow('hsv', hsv)
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    cv.imshow('yuv', yuv)
    ycrcb = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)
    cv.imshow('ycrcb', ycrcb)


print("----- Hello Python -----")
src = cv.imread("../res/in_leaves.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# color_space_demo(src)
# cv.imshow("input image", src)
# extract_object_demo()
split_merge_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()
