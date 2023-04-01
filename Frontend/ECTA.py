<<<<<<< HEAD
import math
import sys
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsRectItem, \
    QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer, QPointF, QRectF, Qt
=======
from PyQt5.QtCore import QThread, pyqtSignal, QTimer
from PyQt5 import uic
import numpy as np
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
import mediapipe as mp
import cv2 as cv
import json
import math
from time import time, sleep

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
>>>>>>> b96fd3dbf52c2e121f57e8f4491865cbabae8341

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the graphics view and scene
        self.view = QGraphicsView()
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)

        # Set up the square item
        self.square = QGraphicsRectItem(QRectF(0, 0, 50, 50))
        self.square.setBrush(Qt.red)
        self.scene.addItem(self.square)

        # Set up the timer and angle
        self.timer = QTimer()
        self.timer.timeout.connect(self.animate)
        self.angle = 0

        # Set up the buttons
        self.start_button = QPushButton('Start')
        self.start_button.clicked.connect(self.start_animation)
        self.pause_button = QPushButton('Pause')
        self.pause_button.clicked.connect(self.pause_animation)
        self.stop_button = QPushButton('Stop')
        self.stop_button.clicked.connect(self.stop_animation)

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.view)
        layout.addWidget(self.start_button)
        layout.addWidget(self.pause_button)
        layout.addWidget(self.stop_button)
        self.setLayout(layout)

    def start_animation(self):
        self.timer.start(20)

    def pause_animation(self):
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start(20)

    def stop_animation(self):
        self.timer.stop()
        self.square.setPos(QPointF(0, 0))
        self.angle = 0

    def animate(self):
        # Calculate the new position of the square
        x = 100 * (1 - pow(self.angle / 360, 2)) * pow(math.sin(math.radians(self.angle)), 3)
        y = 100 * (1 - pow(self.angle / 360, 2)) * pow(math.cos(math.radians(self.angle)), 3)
        self.square.setPos(QPointF(x, y))

        # Update the angle
        self.angle += 2

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
