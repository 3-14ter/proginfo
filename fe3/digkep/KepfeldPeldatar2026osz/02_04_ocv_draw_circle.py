
# OpenCV2 képmátrix létrehozása, megjelenítés és fájlba mentése
# OpenCV online dokumentáció: https://docs.opencv.org/

# Modul definíciók importálása
import numpy as np
import cv2

# 320x200x3 méretű Numpy tömb létrehozása BGR színes képnek
im = np.ndarray((200, 320, 3), np.uint8)
# Feltöltés 192 (világosszürke) színnel
im.fill(192)
# Kör rajzolása az (50, 100) középponttal, 40 sugárral, vörös színnel, kitöltve
cv2.circle(im, (50, 100), 40, (0, 0, 192), -1)
# További rajzoló függvények:
#   https://docs.opencv.org/5.0/py_tutorials/py_gui/py_drawing_functions/py_drawing_functions.html

# --- Régi szövegkiírás (Klasszikus vektoros Hershey font, nincs ékezet) ---
text_old = "Udvozlet az OpenCV 4-bol!"  # Az ékezetes karakterek szétesnének
font_old = cv2.FONT_HERSHEY_SIMPLEX
font_scale_old = 0.8
color_old = (128, 128, 0)  # Ciánkék
thickness_old = 1
position_old = (20, 30)

cv2.putText(im, text_old, position_old, font_old, font_scale_old, color_old, thickness_old)

# Az OpenCV 5.0 új szövegkiírása egyelőre csak C++-ból érhető el.

# Kép megjelenítése ablakban
cv2.imshow('im', im)
cv2.waitKey(0)

# Kép mentése fájlba
cv2.imwrite('ocv_test1_out.png', im)

# Összes ablak bezárása
cv2.destroyAllWindows()
