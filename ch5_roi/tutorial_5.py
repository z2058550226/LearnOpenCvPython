import cv2 as cv
import numpy as np


def fill_color_demo(image):
    """泛洪填充，第一个参数(30,30)表示填充点，第二个参数表示填充颜色，第三个参数表示（30，30）所指定点的像素颜色（下称相对颜色）
    三个通道减100以作为最低颜色判断范围，第四个参数就是相对颜色加50作为颜色判断范围"""
    copy_img = image.copy()
    height, width = image.shape[:2]
    mask = np.zeros([height + 2, width + 2], np.uint8)
    cv.floodFill(copy_img, mask, (30, 30), (0, 255, 255), (100, 100, 100), (50, 50, 50), cv.FLOODFILL_FIXED_RANGE)
    cv.imshow('fill_color_demo', copy_img)


def fill_binary():
    image = np.zeros([400, 400, 3], np.uint8)
    image[100:300, 100:300, :] = 255
    cv.imshow('fill_binary', image)

    mask = np.ones([402, 402, 1], np.uint8)
    mask[101:301, 101:301] = 0
    cv.floodFill(image, mask, (200, 200), (255, 204, 112), cv.FLOODFILL_MASK_ONLY)
    cv.imshow('filled binary', image)


print("----- Hello Python -----")
src = cv.imread("../res/in_leaves.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)

# face = src[150:300, 200:400]
# cv.imshow('face', face)

# fill_color_demo(src)
fill_binary()

cv.waitKey(0)
cv.destroyAllWindows()
