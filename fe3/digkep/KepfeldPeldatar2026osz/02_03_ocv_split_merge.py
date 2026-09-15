
# OpenCV2 képbeolvasás, színtér konverzió
# OpenCV modul definíciók importálása
import cv2

# Kép beolvasása fájlból
im_bgr = cv2.imread('GolyoAlszik_rs.jpg', cv2.IMREAD_COLOR)
cv2.imshow('im_bgr', im_bgr)

# Szürkeárnyalat
im_gray = cv2.cvtColor(im_bgr, cv2.COLOR_BGR2GRAY)
cv2.imshow('im_gray', im_gray)
cv2.waitKey(0)

# Színcsatornákra bontás és megjelenítés
im_b, im_g, im_r = cv2.split(im_bgr)
cv2.imshow('red', im_r)
cv2.imshow('green', im_g)
cv2.imshow('blue', im_b)
cv2.waitKey(0)

# Vörös csatorna nullázása és BGR kép előállítása
im_r[:, :] = 0
im_bgr2 = cv2.merge((im_b, im_g, im_r))
cv2.imshow('bg0', im_bgr2)
cv2.imwrite('Golyo_GB.jpg', im_bgr2)
cv2.waitKey(0)

# Színcsatorna ablakok bezárása
cv2.destroyWindow('red')
cv2.destroyWindow('green')
cv2.destroyWindow('blue')
cv2.destroyWindow('bg0')

# Áttérés Lab színtérbe
# L: szürkeárnyalat
# a, b: kromatikusok (szín információ)
im_Lab = cv2.cvtColor(im_bgr, cv2.COLOR_BGR2Lab)
print('im_Lab.shape:', im_Lab.shape)
cv2.imshow('im_Lab', im_Lab)

# Lab csatornákra bontás
im_L, im_a, im_b = cv2.split(im_Lab)
cv2.imshow('im_L', im_L)
cv2.imshow('im_a', im_a)
cv2.imshow('im_b', im_b)
cv2.waitKey(0)

# im_b nullázása és új BGR kép összerakása
im_b.fill(0)
im_Lab2 = cv2.merge([im_L, im_a, im_b])
im_bgr2 = cv2.cvtColor(im_Lab2, cv2.COLOR_Lab2BGR)
cv2.imshow('im_bgr2', im_bgr2)
cv2.waitKey(0)

cv2.destroyAllWindows()
