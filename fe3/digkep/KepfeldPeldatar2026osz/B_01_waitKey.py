
import cv2

im = cv2.imread('OpenCV-logo.png', cv2.IMREAD_COLOR)
cv2.imshow('im', im)

print('Várakozás billentyű lenyomásig, időkorlát nélkül')
key = cv2.waitKey(0)
print('Lenyomott billentyű és kódja:', chr(key), key)

print('Várakozás billentyű lenyomásra, maximum 5 másodpercig')
key = cv2.waitKey(5000)
if key != -1:
    print('Lenyomott billentyű és kódja:', chr(key), key)
else:
    print('Nem volt lenyomott billentyű!')

h, w, d = im.shape
angle = 0
step = 1.0
print('Billentyűzet-figyelő ciklus')
print('Forgási irány váltás: r')
print('Kilépés: q vagy ESC')

while True:
    key = cv2.waitKeyEx(2000)
    if key == -1:
        # Nem volt lenyomott billentyű, de végezhetünk valamilyen háttértevékenységet
        mtx_rot = cv2.getRotationMatrix2D((w / 2, h / 2), angle, 1.0)
        im_rot = cv2.warpAffine(im, mtx_rot, (w, h))
        cv2.imshow('image', im_rot)
        angle += step
        continue

    if key == 27 or key == ord('q'):
        break

    if key == ord('r'):
        step = -step

    print('Lenyomott billentyű és kódja:', chr(key), key)

cv2.destroyAllWindows()
