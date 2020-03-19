import cv2 as cv


def bi_demo(image):
    dst = cv.bilateralFilter(image, 0, 100, 2)
    cv.imshow('bi_demo', dst)


print("----- Hello Python -----")
src = cv.imread("../res/hezhao.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)

bi_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()
