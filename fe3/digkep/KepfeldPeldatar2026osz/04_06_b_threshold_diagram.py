import numpy as np
import cv2
from matplotlib import pyplot as plt

thresh_value = 80
thresh_max_val = 200


def get_diagram_as_image(fig_in):
    fig_in.canvas.draw()
    data = np.array(fig_in.canvas.renderer.buffer_rgba())
    return cv2.cvtColor(data, cv2.COLOR_RGBA2BGR)


# Inicializálás
x = np.arange(0, 256, 1, np.uint8)
max_val_values = np.full(256, thresh_max_val, dtype=np.uint8)

fig, ax = plt.subplots(figsize=(4, 4), dpi=100)
fig.canvas.manager.set_window_title('cv2.threshold() LUT diagramok')

ax.set_xlim([0, 255])
ax.set_ylim([-10, 265])

# Állandó elemek kirajzolása egyszer
ax.plot(x, x, 'g--', label='Eredeti')
ax.axvline(x=thresh_value, c='b', label='thresh')
ax.plot(x, max_val_values, 'y--', linewidth=1, label='maxval')

# Referencia a dinamikus (piros) vonalra
line_result, = ax.plot(x, x, c='r', linewidth=3, label='Eredmény')

# Legend pozicionálása a jobb alsó sarokba
ax.legend(loc='lower right')


def update_thresh_result(res, title_text, fname=None):
    ax.set_title(title_text)
    line_result.set_ydata(res.ravel())

    res_lut_diag = get_diagram_as_image(fig)
    cv2.imshow('lut_result', res_lut_diag)

    if fname is not None:
        cv2.imwrite(fname, res_lut_diag)
    cv2.waitKey(0)


# Kirajzolás lépésenként
_, res1 = cv2.threshold(x, thresh_value, thresh_max_val, cv2.THRESH_BINARY)
update_thresh_result(res1, 'cv2.threshold() THRESH_BINARY', '04_06_b_thresh_binary.png')

_, res2 = cv2.threshold(x, thresh_value, thresh_max_val, cv2.THRESH_BINARY_INV)
update_thresh_result(res2, 'cv2.threshold() THRESH_BINARY_INV', '04_06_b_thresh_binary_inv.png')

_, res3 = cv2.threshold(x, thresh_value, thresh_max_val, cv2.THRESH_TRUNC)
update_thresh_result(res3, 'cv2.threshold() THRESH_TRUNC', '04_06_b_thresh_trunc.png')

_, res4 = cv2.threshold(x, thresh_value, thresh_max_val, cv2.THRESH_TOZERO)
update_thresh_result(res4, 'cv2.threshold() THRESH_TOZERO', '04_06_b_thresh_tozero.png')

_, res5 = cv2.threshold(x, thresh_value, thresh_max_val, cv2.THRESH_TOZERO_INV)
update_thresh_result(res5, 'cv2.threshold() THRESH_TOZERO_INV', '04_06_b_thresh_tozero_inv.png')

plt.close(fig)