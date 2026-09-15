# Visualize the Hough transformation
# Attila Tanács, 2020-2026
# University of Szeged, Hungary

import cv2
import numpy as np
import math

point_list = []
pts_color_list = [(0, 255, 255), (255, 255, 0), (255, 0, 255), (0, 0, 255), (0, 255, 0), (255, 0, 0), (255, 255, 255)]
hough_param_clicked = []

# Szinuszgörbék pontjainak tárolása (color_idx, theta, rho)
accumulated_curves = []

# Globális lejátszási sebesség ms-ban (cv2.waitKey számára)
delay_ms = 10


def cross(p1, p2):
    if len(p1) != 2 and len(p2) != 2:
        print('Size problem!')
    return p1[0] * p2[1] - p1[1] * p2[0]


def render_hough_space_cv():
    diag_h, diag_w = 400, 400
    diag = np.ones((diag_h, diag_w, 3), dtype=np.uint8) * 255

    # Rács és tengelyek
    cv2.line(diag, (40, 20), (40, diag_h - 40), (200, 200, 200), 1)
    cv2.line(diag, (40, diag_h // 2), (diag_w - 20, diag_h // 2), (200, 200, 200), 1)

    # Kirajzoljuk az eddig összegyűjtött szinus hullám pontokat
    for c_idx, t_val, r_val in accumulated_curves:
        px = int(40 + (t_val / 180.0) * (diag_w - 60))
        py = int((diag_h // 2) - (r_val / size_max) * ((diag_h // 2) - 20))

        color_bgr = pts_color_list[c_idx % 7]
        cv2.circle(diag, (px, py), 1, color_bgr, -1)

    # Tengelyfeliratok
    cv2.putText(diag, 'Theta (0-180)', (140, diag_h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1)
    cv2.putText(diag, 'Rho', (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1)

    return diag


def visualize_rho_theta():
    global P1, rho, theta, im
    global point_list
    global hough_acc, hough_param_clicked

    im_cp = im.copy()

    a = math.cos(math.radians(theta))
    b = math.sin(math.radians(theta))
    P2 = np.asarray(P1) + np.asarray((b, -a))
    p1 = np.asarray(P1)
    p2 = np.asarray(P2)
    p3 = np.asarray((0, 0))

    rho = (cross(p2 - p1, p1 - p3)) / np.linalg.norm(p2 - p1)

    x0 = a * rho
    y0 = b * rho

    pt1 = (0, 0)
    pt2 = (int(x0), int(y0))
    cv2.line(im_cp, pt1, pt2, (255, 0, 0), 2, cv2.LINE_AA)
    pt1 = (int(x0 + size_max * (-b)), int(y0 + size_max * a))
    pt2 = (int(x0 - size_max * (-b)), int(y0 - size_max * a))
    cv2.line(im_cp, pt1, pt2, (0, 0, 255), 2, cv2.LINE_AA)

    for idx, pnt in enumerate(point_list):
        cv2.circle(im_cp, pnt, 5, pts_color_list[idx % 7], -1)

    hough_acc_work = hough_acc.copy()
    if len(hough_param_clicked) > 0:
        t = hough_param_clicked[0][0]
        r = hough_param_clicked[0][1]

        h_y = int((r + size_max) * 0.125)
        h_x = t >> 1
        hough_acc_work[h_y, :] = 255
        hough_acc_work[:, h_x] = 255

        a = math.cos(math.radians(t))
        b = math.sin(math.radians(t))
        x0 = a * r
        y0 = b * r

        pt1 = (int(x0 + size_max * (-b)), int(y0 + size_max * a))
        pt2 = (int(x0 - size_max * (-b)), int(y0 - size_max * a))
        cv2.line(im_cp, pt1, pt2, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow('im', im_cp)

    im_diag = render_hough_space_cv()
    cv2.imshow('Hough parameter space (theta-rho)', im_diag)

    # Vízszintes középtengelyre történő tükrözés (y-tengely megfordítása)
    hough_acc_flipped = cv2.flip(hough_acc_work, 0)

    hough_acc_rs = cv2.resize(hough_acc_flipped, None, None, 4, 4, cv2.INTER_NEAREST)
    cv2.imshow('Hough accumulator', hough_acc_rs)


def on_theta_trackbar_change(x):
    global rho, theta
    theta = x
    a = math.cos(math.radians(theta))
    b = math.sin(math.radians(theta))
    P2 = np.asarray(P1) + np.asarray((b, -a))
    p1 = np.asarray(P1)
    p2 = np.asarray(P2)
    p3 = np.asarray((0, 0))

    rho = (cross(p2 - p1, p1 - p3)) / np.linalg.norm(p2 - p1)
    hough_acc[int((rho + size_max) * 0.125), theta >> 1] += 32

    color_idx = len(point_list) - 1
    accumulated_curves.append((color_idx, theta, rho))

    visualize_rho_theta()


def on_mouse_event(event, x, y, param, flag):
    global P1, point_list, rho, theta

    if event == cv2.EVENT_LBUTTONDOWN:
        P1 = (x, y)
        print('Point added:', P1)
        point_list.append(P1)
        visualize_rho_theta()


def on_hough_mouse_event(event, x, y, param, flag):
    global hough_param_clicked

    if event == cv2.EVENT_MOUSEMOVE:
        hpt_theta = 2 * int(x / 4)
        # Figyelembe vesszük a tükrözött y-koordinátát az egéreseménynél
        hpt_rho = int(int(size_max) - 4 * int(y / 2))
        hpt = (hpt_theta, hpt_rho)
        hough_param_clicked = [hpt]
        visualize_rho_theta()


im = cv2.imread('sudoku_rs.jpg', cv2.IMREAD_COLOR)
edge = cv2.Canny(im, 50, 300)
im = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)
size_max = math.sqrt(im.shape[0] ** 2 + im.shape[1] ** 2)

P1 = (168, 100)
point_list.append(P1)
theta = 0

rho = 0
hough_acc = np.zeros((int(0.25 * size_max + 0.5), 90), np.uint8)
cv2.imshow('Hough accumulator', hough_acc)
cv2.namedWindow('im')
cv2.createTrackbar('theta', 'im', theta, 179, on_theta_trackbar_change)
cv2.imshow('im', im)
on_theta_trackbar_change(theta)
cv2.setMouseCallback('im', on_mouse_event)
cv2.setMouseCallback('Hough accumulator', on_hough_mouse_event)

while True:
    key = cv2.waitKey(0)

    if key == ord('q'):
        break

    if key == ord('a'):
        for val in range(0, 180, 2):
            hough_param_clicked = []
            cv2.setTrackbarPos('theta', 'im', val)
            cv2.waitKey(delay_ms)

    if key == ord('p'):
        add_points = [(226, 52), (47, 86), (272, 110), (211, 191), (221, 104), (69, 179)]
        for pt in add_points:
            P1 = pt
            print('Point added:', pt)
            point_list.append(pt)
            for val in range(0, 180, 2):
                hough_param_clicked = []
                cv2.setTrackbarPos('theta', 'im', val)
                cv2.waitKey(delay_ms)

cv2.destroyAllWindows()