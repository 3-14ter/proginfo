
# OpenCV2 képbeolvasás, szürkeárnyalatos konverzió
# OpenCV online dokumentáció: https://docs.opencv.org/

# OpenCV modul definíciók importálása
import cv2

# Kép beolvasása fájlból szürkeárnyalatosként
im_gray = cv2.imread('OpenCV-logo.png', cv2.IMREAD_GRAYSCALE)

# Képméret kiíratása konzolra
print('im_gray.shape:', im_gray.shape)

# Kép megjelenítése ablakban
cv2.imshow('im_gray', im_gray)
cv2.waitKey(0)

# Kép beolvasása fájlból színes képként
im_color = cv2.imread('OpenCV-logo.png', cv2.IMREAD_COLOR)
print('im_color.shape:', im_color.shape)
im_gray2 = cv2.cvtColor(im_color, cv2.COLOR_BGR2GRAY)
print('im_gray2.shape:', im_gray2.shape)

# Kép megjelenítése ablakban
cv2.imshow('im_gray2', im_gray2)
cv2.waitKey(0)

cv2.destroyAllWindows()
