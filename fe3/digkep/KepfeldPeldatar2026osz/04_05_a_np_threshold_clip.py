
import cv2
import numpy as np

im_src = cv2.imread('car_numberplate_rs.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Eredeti', im_src)

im_thresh = np.ndarray(im_src.shape, im_src.dtype)

im_thresh[im_src >= 120] = 255
im_thresh[im_src < 120] = 0
cv2.imshow('Kuszobolt 120 ertekkel', im_thresh)

im_thresh.fill(0)
im_thresh[(im_src >= 80) & (im_src <= 160)] = 255
cv2.imshow('Kuszoboles 80-160 tartomanyban', im_thresh)

im_clip = im_src.copy()
im_clip[im_src < 80] = 0
im_clip[im_src > 160] = 0
cv2.imshow('Vagas ket kuszobbel', im_clip)
cv2.waitKey(0)

cv2.destroyAllWindows()
