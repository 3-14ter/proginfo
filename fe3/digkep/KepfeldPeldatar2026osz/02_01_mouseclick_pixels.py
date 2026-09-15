import cv2


def mouse_click(event, x, y, flags, param):
    # Globális változó átvétele
    global im

    # További egéresemények:
    # https://docs.opencv.org/5.0/main_modules/highgui_window_flags.html#mouseeventtypes
    if event == cv2.EVENT_LBUTTONDOWN:
        # Kattintás helyén lévő mátrixérték kiírása
        print('Pixel =', im[y, x])
        # Ha 3 csatornás a kép
        if im.ndim == 3:
            # Vörös csatorna értékének kiírása
            print('R =', im[y, x, 2])
            print('')

        # Ha változtatunk az image mátrix tartalmán, akkor újra meg kell jeleníteni
        cv2.imshow('im', im)


im = cv2.imread('OpenCV-logo.png', cv2.IMREAD_COLOR)
# im = cv2.imread('OpenCV-logo.png', cv2.IMREAD_GRAYSCALE)
print('Kép indexelhető dimenziói:', im.ndim)
print('Kép mérete: ', im.shape)
print('Kép pixeltípusa: ', im.dtype)

cv2.imshow('im', im)
# Egérkezelő callback függvény beállitása az ablakhoz
cv2.setMouseCallback('im', mouse_click)
# Kilépés billentyűlenyomásra
cv2.waitKey(0)

cv2.destroyAllWindows()
