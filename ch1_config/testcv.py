import cv2 as cv

print("----- Hello Python -----")
src = cv.imread("../res/in_leaves.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)

cv.waitKey(0)
cv.destroyAllWindows()
