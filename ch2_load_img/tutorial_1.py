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


print("----- Hello Python -----")
src = cv.imread("../res/in_leaves.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
get_image_info(src)
# video_demo()
cv.imwrite("./tmp/output/result.png", src)
cv.imshow("input image", src)

cv.waitKey(0)
cv.destroyAllWindows()
