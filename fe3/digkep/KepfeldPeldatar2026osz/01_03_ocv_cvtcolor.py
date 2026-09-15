
# OpenCV2 képbeolvasás, színtér konverzió
# OpenCV modul definíciók importálása
import cv2

# Színes kép beolvasása fájlból
im_bgr = cv2.imread('GolyoAlszik_rs.jpg', cv2.IMREAD_COLOR)
print('im_bgr.shape:', im_bgr.shape)
cv2.imshow('im_bgr', im_bgr)

# Szürkeárnyalat
im_gray = cv2.cvtColor(im_bgr, cv2.COLOR_BGR2GRAY)
cv2.imshow('im_gray', im_gray)
print('im_gray.shape:', im_gray.shape)
cv2.waitKey(0)

# Szürkéből "színes"
im_gray2bgr = cv2.cvtColor(im_gray, cv2.COLOR_GRAY2BGR)
cv2.imshow('im_gray2bgr', im_gray2bgr)
print('im_gray2bgr.shape:', im_gray2bgr.shape)
cv2.waitKey(0)

# Áttérés Lab színtérbe
# L: szürkeárnyalat
# a, b: kromatikusok (szín információ)
im_Lab = cv2.cvtColor(im_bgr, cv2.COLOR_BGR2Lab)
print('im_Lab.shape:', im_Lab.shape)
cv2.imshow('im_Lab', im_Lab)
cv2.waitKey(0)

# Vissza BGR-be
im_bgr2 = cv2.cvtColor(im_Lab, cv2.COLOR_Lab2BGR)
cv2.imshow('im_bgr2', im_bgr2)
cv2.waitKey(0)

cv2.destroyAllWindows()
