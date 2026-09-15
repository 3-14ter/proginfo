import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel,
                               QWidget, QVBoxLayout, QSlider, QHBoxLayout, QFileDialog, QMessageBox)
from PySide6.QtGui import QPixmap, QImage


class ImageProcessorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # 1. Initialize Data
        self.im = cv2.imread('hk_flower_h.jpg')
        if self.im is None:
            self.im = np.zeros((400, 600, 3), dtype=np.uint8)
            cv2.putText(self.im, "Image Not Found", (150, 200),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        self.new_image = self.im.copy()
        self.brightness = 0
        self.contrast = 0

        # 2. Setup Matplotlib Figure
        self.fig = plt.figure(figsize=(4, 4), dpi=25)
        self.ax = self.fig.add_subplot(111)
        self.x = np.arange(0, 256, 1)

        # 3. Setup UI
        self.init_ui()
        self.do_brightness_contrast()

    def init_ui(self):
        self.setWindowTitle('PySide6 Image Processor')
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Image Display
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.image_label)

        # Sliders
        main_layout.addWidget(QLabel("Brightness"))
        self.bsl = self.create_slider(self.change_brightness)
        main_layout.addWidget(self.bsl)
        self.lbl_br = QLabel("Value: 0")
        main_layout.addWidget(self.lbl_br)

        main_layout.addWidget(QLabel("Contrast"))
        self.csl = self.create_slider(self.change_contrast)
        main_layout.addWidget(self.csl)
        self.lbl_ct = QLabel("Value: 0")
        main_layout.addWidget(self.lbl_ct)

        # Button Row (Horizontal Layout)
        button_layout = QHBoxLayout()

        self.btn_reset = QPushButton('Reset')
        self.btn_reset.clicked.connect(self.reset_values)

        self.btn_save = QPushButton('Save Image')
        self.btn_save.clicked.connect(self.save_image)

        self.btn_quit = QPushButton('Quit')
        self.btn_quit.clicked.connect(self.close)  # Built-in QWidget close method

        button_layout.addWidget(self.btn_reset)
        button_layout.addWidget(self.btn_save)
        button_layout.addWidget(self.btn_quit)

        main_layout.addLayout(button_layout)

    def create_slider(self, callback):
        slider = QSlider(Qt.Orientation.Horizontal)
        slider.setMinimum(-255)
        slider.setMaximum(255)
        slider.setValue(0)
        slider.setTickInterval(10)
        slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        slider.valueChanged.connect(callback)
        return slider

    def reset_values(self):
        self.bsl.setValue(0)
        self.csl.setValue(0)
        self.do_brightness_contrast()

    def change_brightness(self):
        self.brightness = self.bsl.value()
        self.do_brightness_contrast()

    def change_contrast(self):
        self.contrast = self.csl.value()
        self.do_brightness_contrast()

    def save_image(self):
        # Open file dialog to choose save location
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save Image", "processed_image.jpg", "Images (*.jpg *.png *.bmp)"
        )

        if file_path:
            # OpenCV uses BGR, so we can save self.new_image directly
            success = cv2.imwrite(file_path, self.new_image)
            if success:
                QMessageBox.information(self, "Success", f"Image saved to:\n{file_path}")
            else:
                QMessageBox.critical(self, "Error", "Failed to save image.")

    def get_diagram_as_image(self):
        self.fig.canvas.draw()
        data = np.array(self.fig.canvas.renderer.buffer_rgba())
        return cv2.cvtColor(data, cv2.COLOR_RGBA2BGR)

    def cv2_to_pixmap(self, img):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, ch = img_rgb.shape
        bytes_per_line = ch * w
        qt_img = QImage(img_rgb.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
        return QPixmap.fromImage(qt_img)

    def do_brightness_contrast(self):
        self.lbl_br.setText(f'Brightness: {self.brightness}')
        self.lbl_ct.setText(f'Contrast: {self.contrast}')

        # Contrast adjustment algorithm
        denominator = (255 * (259 - self.contrast))
        if denominator == 0: denominator = 1  # Safety check
        factor = (259 * (self.contrast + 255)) / denominator

        lut = np.arange(0, 256, 1)
        lut = np.uint8(np.clip(self.brightness + factor * (np.float32(lut) - 128.0) + 128, 0, 255))
        self.new_image = cv2.LUT(self.im, lut)

        # Update Matplotlib plot
        self.ax.clear()
        self.ax.plot(self.x, self.x, 'g--', linewidth=5)
        self.ax.plot(self.x, lut, 'r-', linewidth=5)
        self.ax.set_xlim([0, 255])
        self.ax.set_ylim([0, 255])
        self.ax.axis('off')

        # Overlay plot onto image
        lut_im = self.get_diagram_as_image()
        lh, lw, _ = lut_im.shape
        self.new_image[0:lh, 0:lw] = lut_im

        # Update display
        self.image_label.setPixmap(self.cv2_to_pixmap(self.new_image))


if __name__ == '__main__':
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)

    main_win = ImageProcessorApp()
    main_win.show()
    sys.exit(app.exec())