import cv2


def mouse_click(event, x, y, flags, param):
    # Globális változó átvétele
    global im

    # Bal egérgomb lenyomásának kezelése
    if event == cv2.EVENT_LBUTTONDOWN:
        # Kattintás helyén lévő eredeti mátrixérték kiírása
        print('Pixel =', im[y, x])
        
        # Ha 3 csatornás (színes) a kép
        if im.ndim == 3:
            print('R =', im[y, x, 2])
            print('')
            # Vörös szín beállítása (BGR sorrend szerint: B=0, G=0, R=255)
            im[y, x] = [0, 0, 255]
        else:
            # Szürkeárnyalatos (2 dimenziós) kép esetén invertálás
            im[y, x] = 255 - im[y, x]

        # A módosított képmátrix újbóli megjelenítése az ablakban
        cv2.imshow('im', im)


im = cv2.imread('OpenCV-logo.png', cv2.IMREAD_COLOR)
# im = cv2.imread('OpenCV-logo.png', cv2.IMREAD_GRAYSCALE)
print('Kép indexelhető dimenziói:', im.ndim)
print('Kép mérete: ', im.shape)
print('Kép pixeltípusa: ', im.dtype)

cv2.imshow('im', im)
# Egérkezelő callback függvény beállítása az ablakhoz
cv2.setMouseCallback('im', mouse_click)
# Kilépés billentyűlenyomásra
cv2.waitKey(0)

cv2.destroyAllWindows()