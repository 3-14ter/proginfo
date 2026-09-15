# nagya@inf.u-szeged.hu, 6195 call 


# OpenCV2 képbeolvasás, megjelenítés és tükrözés
# OpenCV online dokumentáció: https://docs.opencv.org/


# OpenCV modul definíciók importálása
import cv2


# OpenCV verziószám kiíratása
print('OpenCV verzió:', cv2.__version__)


# Kép beolvasása fájlból
im = cv2.imread('OpenCV-logo.png', cv2.IMREAD_COLOR)


# Képméret kiíratása konzolra
print(im.shape)


# Kép megjelenítése ablakban
cv2.imshow('image', im)
cv2.waitKey(0)


# Tükrözés a függőleges középtengelyre és megjelenítés
im_flipped = cv2.flip(im, 1)
cv2.imshow('image', im_flipped)
cv2.imwrite('OpenCV-logo-flipped.png', im_flipped)
cv2.waitKey(0)


# Tükrözés mindkét középtengelyre és megjelenítés
im_flipped2 = cv2.flip(im, -1)
cv2.imshow('image', im_flipped2)
cv2.waitKey(0)


# Összes ablak bezárása
cv2.destroyAllWindows()
