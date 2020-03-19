import cv2 as cv

from matplotlib import pyplot as plt


def plot_demo(image):
    """ravel是降维函数，将多维数组拉成一维数组，这里统计了颜色数值的分布"""
    plt.hist(image.ravel(), 256, [0, 256])
    plt.show('histogram')


def image_hist(image):
    color = ['blue', 'green', 'red']
    for i, color in enumerate(color):
        hist = cv.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    plt.show()


print("----- Hello Python -----")
src = cv.imread("../res/in_leaves.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
# plot_demo(src)
image_hist(src)

cv.waitKey(0)
cv.destroyAllWindows()
