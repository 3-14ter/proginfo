import cv2

# Válassz betöltési módot teszteléshez:
im_clean = cv2.imread('OpenCV-logo.png', cv2.IMREAD_COLOR)
# im_clean = cv2.imread('OpenCV-logo.png', cv2.IMREAD_GRAYSCALE)

# Szín meghatározása: színesnél sárga (BGR: [0, 255, 255]), szürkénél 192
color = [0, 0, 0] if im_clean.ndim == 3 else 192


def mouse_move(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        # Tiszta háttér másolása (így nem hagy nyomot az előző vonal)
        im = im_clean.copy()

        # Célkereszt rajzolása: vízszintes és függőleges vonal
        im[y, :] = color
        im[:, x] = color

        cv2.imshow('OpenCV-logo', im)


cv2.imshow('OpenCV-logo', im_clean)
cv2.setMouseCallback('OpenCV-logo', mouse_move)

cv2.waitKey(0)
cv2.destroyAllWindows()