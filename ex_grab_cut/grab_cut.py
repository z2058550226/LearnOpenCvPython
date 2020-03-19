import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def show_mask(m, name='mask'):
    mask_snap_shot = cv.multiply(m, np.ones(m.shape[:2], np.uint8) * 50)
    cv.imshow(name, mask_snap_shot)


img = cv.imread('../res/sculpture.jpg')
cv.imshow('original_image', img)
mask = np.zeros(img.shape[:2], np.uint8)

bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
rect = (200, 0, 350, 750)
# cv.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv.GC_INIT_WITH_RECT)
#
# mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
# show_mask(mask2)
# img = img * mask2[:, :, np.newaxis]
# plt.imshow(img), plt.colorbar(), plt.show()

# create new mask for user touch up
new_mask = np.ones(mask.shape[:2], np.uint8)
new_mask[90:110, 610:630] = 0  # black for background
new_mask[390:410, 620:640] = 0
new_mask[75:80, 457:463] = 255  # white for foreground
new_mask[200:300, 300:400] = 255

show_mask(mask, 'original_mask')
mask[0:750, 200:550] = 3
mask[new_mask == 0] = 0
mask[new_mask == 255] = 1
mask2, bgdModel, fgdModel = cv.grabCut(img, mask, None, bgdModel, fgdModel, 5, cv.GC_INIT_WITH_MASK)
show_mask(mask, 'mask')
show_mask(mask2, 'mask2')
mask3 = np.where((mask2 == 2) | (mask2 == 0), 0, 1).astype('uint8')
show_mask(mask3, 'mask3')
cv.imshow('img', img)
img = img * mask3[:, :, np.newaxis]
dst = cv.cvtColor(img, cv.COLOR_RGB2BGR)
plt.imshow(dst), plt.colorbar(), plt.show()
