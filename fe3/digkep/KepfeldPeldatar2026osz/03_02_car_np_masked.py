
import cv2
import time

# Képek beolvasása
im = cv2.imread('car_numberplate_rs.jpg', cv2.IMREAD_COLOR)
mask = cv2.imread('car_numberplate_rs_mask.png', cv2.IMREAD_COLOR)
edge = cv2.imread('car_numberplate_rs_mask_edge.png', cv2.IMREAD_GRAYSCALE)

# Kép sor és oszlop méret egyezőség ellenőrzése
assert im.shape[0:2] == mask.shape[0:2]
assert im.shape[0:2] == edge.shape[0:2]

# Kép és maszk megjelenítése
cv2.imshow('im', im)
cv2.imshow('mask', mask)

# Maszkolt BGR kép előállítása
masked = cv2.bitwise_and(im, mask)
cv2.imshow('masked', masked)
cv2.waitKey(0)

# Eredeti képen a maszk területe fehérre színezve
im_roi = im.copy()
im_roi[mask > 0] = 255
cv2.imshow('im_roi', im_roi)
cv2.waitKey(0)

# Vörös színű körvonal az eredeti képre
# Numpy feltételes indexeléssel
im_np_edge = im.copy()
start_time = time.perf_counter()
im_np_edge[edge > 0] = [0, 0, 255]
end_time = time.perf_counter()
print('Numpy élrajzolás:', (end_time - start_time) * 1000.0, "ezredmásodperc.")
cv2.imshow('im_np_edge', im_np_edge)
cv2.waitKey(0)

# Vörös színű körvonal az eredeti képre
# Nagyon lassú változat! Csak ha végképp nincs más lehetőség!
im_edge = im.copy()
start_time = time.perf_counter()
for y in range(0, im.shape[0]):
    for x in range(0, im.shape[1]):
        if edge[y, x] > 0:
            im_edge[y, x] = [0, 0, 255]

end_time = time.perf_counter()
print('Élrajzolás for ciklusokkal:', (end_time - start_time) * 1000.0, "ezredmásodperc.")
cv2.imshow('im_edge', im_edge)
cv2.waitKey(0)

# Vörös színű körvonal az eredeti képre
# OpenCV bitenkénti logikai függvényekkel
# Nagyságrendekkel gyorsabb! (255x)
im_ocv_edge = im.copy()
start_time = time.perf_counter()
b, g, r = cv2.split(im_ocv_edge)
r = cv2.bitwise_or(r, edge)
g = cv2.bitwise_and(g, ~edge)
b = cv2.bitwise_and(b, ~edge)
im_ocv_edge = cv2.merge((b, g, r))
end_time = time.perf_counter()
print('OpenCV élrajzolás:', (end_time - start_time) * 1000.0, "ezredmásodperc.")
cv2.imshow('im_ocv_edge', im_ocv_edge)
cv2.waitKey(0)

cv2.destroyAllWindows()
