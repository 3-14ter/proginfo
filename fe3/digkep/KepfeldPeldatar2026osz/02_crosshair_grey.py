import cv2

im_clean = cv2.imread('OpenCV-logo.png', cv2.IMREAD_GRAYSCALE)

color = [0, 0, 0] if im_clean.ndim == 3 else 192


def mouse_move(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        print(f"Pos: (x={x}, y={y}) -> val: {im_clean[y, x]}")
        im = im_clean.copy()

        # Célkereszt rajzolás
        im[y, :] = color
        im[:, x] = color

        cv2.imshow('OpenCV-logo', im)


cv2.imshow('OpenCV-logo', im_clean)
cv2.setMouseCallback('OpenCV-logo', mouse_move)

cv2.waitKey(0)
cv2.destroyAllWindows()