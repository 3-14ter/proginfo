import cv2
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import numpy as np

# Inicializálás
segmentor = SelfiSegmentation()

cap = cv2.VideoCapture(1)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)

    # A 'threshold' helyett 'cutThreshold'-ot kell írni az új cvzone-ban
    output_image = segmentor.removeBG(frame, imgBg=(0, 255, 0), cutThreshold=0.3)

    cv2.imshow('cvzone Hattercsere', output_image)

    if cv2.waitKey(5) & 0xFF == 27:  # ESC-re kilép
        break

cap.release()
cv2.destroyAllWindows()