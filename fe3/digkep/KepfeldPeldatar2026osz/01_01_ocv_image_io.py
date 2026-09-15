
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
cv2.waitKey(2000)

h, w, d = im.shape
angle = 0
step = 1.0
print('Billentyűzet-figyelő ciklus')
print('Forgási irány váltás: r')
print('Kilépés: q vagy ESC')
count = 0

while True:
    key = cv2.waitKeyEx(100)
    if key == -1:
        continue
    
    if key == 27 or key == ord('q'):
        break

    if key == ord('h'):
        img_uj = cv2.flip(img_uj, 1)
        cv2.imshow("image", img_uj)
    if key == ord('H'):
        im = img_uj
        im = cv2.flip(img_uj, 1)
        cv2.imshow(f"{im}_{count}", img_uj)

    if key == ord('v'):
        img_uj = cv2.flip(img_uj, 0)
        cv2.imshow("image", img_uj)
    if key == ord('V'):
        im = img_uj
        im = cv2.flip(img_uj, 1)

        cv2.imshow(f"{im}_{count}", img_uj)
    if key == ord('t'):
        img_uj = cv2.transpose(im)
        cv2.imshow("image", img_uj)

    print('Lenyomott billentyű és kódja:', chr(key), key)


# Tükrözés a függőleges középtengelyre és megjelenítés
'''im_flipped = cv2.flip(im, 1)
cv2.imshow('image', im_flipped)
cv2.imwrite('OpenCV-logo-flipped.png', im_flipped)
cv2.waitKey(2000)

# Tükrözés mindkét középtengelyre és megjelenítés
im_flipped2 = cv2.flip(im, -1)
cv2.imshow('image', im_flipped2)
cv2.waitKey(2000)'''

# Összes ablak bezárása
cv2.destroyAllWindows()
