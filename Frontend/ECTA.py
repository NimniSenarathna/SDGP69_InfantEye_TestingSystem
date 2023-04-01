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

        uic.loadUi('main.ui', self)

        self.vector = np.zeros(9)
        self.x = 550
        self.y = 275

        self.pushButtonStart.clicked.connect(self.start)
        self.pushButtonStop.clicked.connect(self.stop)
        self.pushButtonPause.clicked.connect(self.pause)

        self.Image_label = QLabel(self)
        self.Image_label.setGeometry(self.x, self.y, 100, 100)
        self.Image_label.setPixmap(QPixmap("butterfly.png").scaled(100, 100))

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_position)

        self.thread_process = process_thread()
        self.thread_process.position_vector_signal.connect(self.get_information)

        self.result_left = result("left")
        self.result_right = result("right")

    def start(self):
        self.thread_process.start_process()
        self.result_left.start_get_result()
        self.result_right.start_get_result()
        s_time = time()
        while time() - s_time < 8:
            continue
        self.x = 0
        self.y = 0
        self.timer.start(100)

    def stop(self):
        self.timer.stop()
        self.x = 550
        self.y = 275
        self.Image_label.move(self.x, self.y)
        self.thread_process.stop_process()
        self.result_left.cal_result()
        self.result_right.cal_result()
        # self.result_left.stop_get_result()
        # self.result_right.stop_get_result()
        print("stop")

    def pause(self):
        # Pause the timer
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start(10)

    def update_position(self):
        # Move the object in a square shape
        if self.x < 1150 and self.y == 0:
            self.x += 5
        elif self.x == 1150 and self.y < 570:
            self.y += 5
        elif self.x > 0 and self.y == 570:
            self.x -= 5
        elif self.x == 0 and self.y > 0:
            self.y -= 5

        # Set the position of the object
        self.Image_label.move(self.x, self.y)
        center = (550, 275, 275)
        self.vector = filter_current_position((self.x, self.y, 275), center)

    def get_information(self, left_vector, right_vector):
        self.result_left.process(left_vector, self.vector)
        self.result_right.process(right_vector, self.vector)
