import cv2 as cv
import numpy as np


def video_demo():
    capture = cv.VideoCapture(0)
    while (True):
        (ret, frame) = capture.read()
        cv.flip(frame, -1, frame)  # 左右反转，因为默认是镜像录像，如果想换成上下反转就传-1
        cv.imshow('video', frame)
        c = cv.waitKey(50)
        if c == 27:
            break


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
    # for row in range(height):
    #     for col in range()
#     update on a
#     update on a2
#     update on master


print("----- Hello Python -----")
src = cv.imread("../res/in_leaves.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
get_image_info(src)
# video_demo()
cv.imwrite("./tmp/output/result.png", src)
cv.imshow("input image", src)

cv.waitKey(0)
cv.destroyAllWindows()
