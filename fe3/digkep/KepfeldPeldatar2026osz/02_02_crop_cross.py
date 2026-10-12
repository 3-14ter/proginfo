import cv2

# A fekete vízszintes sáv magassága pixelben
STRIPE_HEIGHT = 10


def mouse_click(event, x, y, flags, param):
    global im

    if event == cv2.EVENT_MOUSEMOVE:
        # A sáv felső és alsó határának kiszámítása (kép szélein belül tartva)
        y_start = max(0, y - STRIPE_HEIGHT // 2)
        y_end = min(im.shape[0], y + STRIPE_HEIGHT // 2)

        # Croppolós / slicing felülírás a teljes szélesség mentén:
        # A kijelölt sor-tartomány minden oszlopának és csatornájának 0 (fekete) értéket adunk
        im[y_start:y_end, :] = 0

        # Frissített kép újbóli megjelenítése
        cv2.imshow('OpenCV-logo', im)


# Kifejezetten az OpenCV-logo.png betöltése
im = cv2.imread('OpenCV-logo.png', cv2.IMREAD_COLOR)

cv2.imshow('OpenCV-logo', im)
cv2.setMouseCallback('OpenCV-logo', mouse_click)

cv2.waitKey(0)
cv2.destroyAllWindows()