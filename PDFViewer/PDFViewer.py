# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 09:26:47 2023

@author: dottd
"""

#PDF EDITOR
import sys
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import fitz  # PyMuPDF
from PIL import Image
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QHBoxLayout, QPushButton, QScrollArea
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QSize
from PIL.ImageQt import ImageQt

class PDFViewer(QMainWindow):
    def __init__(self, file_path):
        super().__init__()

        self.setWindowTitle('PDF Viewer')
        self.setGeometry(100, 100, 800, 600)

        self.pdf_path = file_path
        self.image_list = []
        self.current_page = 0

        self.load_pdf()
        self.setup_ui()

    def load_pdf(self):
        print("Loading PDF:", self.pdf_path)
        doc = fitz.open(self.pdf_path)
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
            image = self.convert_pixmap_to_image(pix)
            self.image_list.append(image)
        print("PDF loaded successfully.")

    def convert_pixmap_to_image(self, pixmap):
        width, height = pixmap.width, pixmap.height  # Get width and height
        return Image.frombytes("RGB", (width, height), pixmap.samples)

    def setup_ui(self):
        layout = QVBoxLayout()
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setup_image_display()
        self.setup_thumbnail_scroll_area()

    def setup_image_display(self):
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setPixmap(self.get_current_pixmap().scaledToWidth(800, Qt.FastTransformation))
        self.label.adjustSize()

        layout = self.centralWidget().layout()
        layout.addWidget(self.label)

    def setup_thumbnail_scroll_area(self):
        thumbnails_widget = QWidget()
        thumbnails_layout = QHBoxLayout()
        thumbnails_widget.setLayout(thumbnails_layout)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(thumbnails_widget)

        layout = self.centralWidget().layout()
        layout.addWidget(scroll_area)

        for page_num, image in enumerate(self.image_list):
            thumbnail_button = QPushButton()
            thumbnail_button.setIconSize(QSize(100, 100))
            thumbnail_button.setMaximumSize(QSize(100, 100))
            thumbnail_button.setIcon(self.get_thumbnail_icon(image))
            thumbnail_button.clicked.connect(lambda _, page=page_num: self.on_thumbnail_clicked(page))
            thumbnails_layout.addWidget(thumbnail_button)

    def get_current_pixmap(self):
        return self.convert_image_to_pixmap(self.image_list[self.current_page])

    def convert_image_to_pixmap(self, image):
        return QPixmap.fromImage(ImageQt(image))

    def get_thumbnail_icon(self, image):
        pixmap = self.convert_image_to_pixmap(image)
        return pixmap.scaled(QSize(100, 100), Qt.AspectRatioMode.KeepAspectRatio, Qt.FastTransformation)

    def on_thumbnail_clicked(self, page):
        self.current_page = page
        self.label.setPixmap(self.get_current_pixmap().scaledToWidth(800, Qt.FastTransformation))
        self.label.adjustSize()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            if self.current_page > 0:
                self.current_page -= 1
                self.label.setPixmap(self.get_current_pixmap().scaledToWidth(800, Qt.FastTransformation))
                self.label.adjustSize()

        elif event.key() == Qt.Key_Right:
            if self.current_page < len(self.image_list) - 1:
                self.current_page += 1
                self.label.setPixmap(self.get_current_pixmap().scaledToWidth(800, Qt.FastTransformation))
                self.label.adjustSize()

def select_file():
    Tk().withdraw()
    file_path = askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        return file_path
    else:
        print("No file selected.")
        return None

if __name__ == '__main__':
    app = QApplication(sys.argv)

    file_path = select_file()
    if file_path:
        viewer = PDFViewer(file_path)
        viewer.show()

    sys.exit(app.exec_())
