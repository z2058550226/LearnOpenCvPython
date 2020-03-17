import cv2 as cv
import numpy as np


def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)
    pixel_data = np.array(image)
    print(pixel_data)


def access_pixels(image):
    """访问一个Mat的每一个像素，在python中Mat是一个三维数组。"""
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]  # 宽度
    channels = image.shape[2]  # 取色彩通道数，OpenCv中默认是BGR，所以一般是3
    print("width : %s, height : %s channels : %s" % (width, height, channels))
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row, col, c]
                image[row, col, c] = 255 - pv
    cv.imshow("pixels_demo", image)


def inverse(image):
    """上面的函数的简化版，这里是用c执行，速度更快"""
    dst = cv.bitwise_not(image)
    cv.imshow("inverse_demo", dst)


def create_image():
    """
    img = np.zeros([400, 400, 3], np.uint8)
    img[:, :, 0] = np.ones([400, 400]) * 255  # B通道所有像素置为255
    cv.imshow("new image", img)

    img = np.ones([400, 400, 1], np.uint8)
    img = img * 127  # 单通道图像都是灰度图像
    cv.imshow("new_image", img)
    cv.imwrite('../tmp/output/created_image.png', img)
    """
    m1 = np.ones([3, 3], np.uint8)
    m1.fill(12222.388)
    print(m1)

    m2 = m1.reshape([1, 9])  # 将二维数组转变为一维数组
    print(m2)


print("----- Hello Python -----")
src = cv.imread("../res/in_leaves.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# get_image_info(src)
# time_measure_1(access_pixels, src)
create_image()
# cv.imwrite("../tmp/output/result.png", src)
cv.imshow("input image", src)

cv.waitKey(0)
cv.destroyAllWindows()
