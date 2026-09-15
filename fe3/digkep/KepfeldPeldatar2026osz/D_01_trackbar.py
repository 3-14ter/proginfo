
import cv2
import numpy as np


def on_param1_trackbar(x):
    print("=============================")
    print('param1 trackbar pozíció:', x)


def on_param2_trackbar(x):
    print("=============================")
    print('param2 trackbar pozíció:', x)
    param = (x - 50) / 100
    print('Átalakított paraméterérték: {}'.format(param))


# im = cv2.imread('OpenCV-logo.png', cv2.IMREAD_COLOR)
im = np.ndarray((200, 640, 3), np.uint8)
im.fill(192)
cv2.imshow('window', im)

cv2.createTrackbar('param1', 'window', 5, 10, on_param1_trackbar)
cv2.createTrackbar('param2', 'window', 10, 60, on_param2_trackbar)
cv2.waitKey(0)

print('param2 trackbar min, max, és pos paraméterének beállítása')
cv2.setTrackbarMin('param2', 'window', 20)
cv2.setTrackbarMax('param2', 'window', 80)
cv2.setTrackbarPos('param2', 'window', 30)
pos = cv2.getTrackbarPos('param2', 'window')
print('Trackbar pozíció:', pos)

cv2.waitKey(0)
cv2.destroyAllWindows()
