
import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Kamerához kapcsolódás sikertelen!')
    exit(-1)

while True:
    # Beolvasás képkockánként
    ret, im_frame = cap.read()

    if not ret:
        break

    # Aktuális frame képkocka feldolgozása
    im_frame = cv2.flip(im_frame, 1)  # szelfi kamera képet tükrözni célszerű
    im_gray = cv2.cvtColor(im_frame, cv2.COLOR_BGR2GRAY)
    im_edges = cv2.Canny(im_gray, 50, 150)

    # Eredmény megjelenítése
    cv2.imshow('frame', im_edges)
    # Kell a waitkey(1), hogy a változás megjelenjen az ablakban!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Erőforrás felszabadítása
cap.release()
cv2.destroyAllWindows()
