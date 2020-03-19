import cv2 as cv


def equal_hist_demo(image):
    """直方图均衡化有对比度增强的效果"""
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    dst = cv.equalizeHist(gray)
    cv.imshow('equalHist_demo', dst)


def clahe_demo(image):
    """局部直方图均衡化效果会弱一些，不会过于均衡"""
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    dst = clahe.apply(gray)
    cv.imshow('clahe_demo', dst)


print("----- Hello Python -----")
src = cv.imread("../res/equal_hist2.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
# equal_hist_demo(src)
clahe_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()
