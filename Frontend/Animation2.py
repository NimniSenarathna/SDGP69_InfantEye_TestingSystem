import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer, Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window size
        self.setGeometry(100, 100, 1800, 900)

        # Create a label to display the image
        self.image_label = QLabel(self)
        self.image_label.setGeometry(0, 0, 200, 200)
        self.image_label.setPixmap(QPixmap("butterfly.jpg").scaled(200, 200))

        # Set the initial position of the object
        self.x = 0
        self.y = 0

        # Create a timer to update the object's position
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_position)

        # Create buttons
        start_button = QPushButton("Start", self)
        start_button.setGeometry(1500, 800, 100, 50)
        start_button.clicked.connect(self.start)

        stop_button = QPushButton("Stop", self)
        stop_button.setGeometry(1610, 800, 100, 50)
        stop_button.clicked.connect(self.stop)

        pause_button = QPushButton("Pause", self)
        pause_button.setGeometry(1720, 800, 100, 50)
        pause_button.clicked.connect(self.pause)

        finish_button = QPushButton("Finish", self)
        finish_button.setGeometry(1500, 860, 320, 30)
        finish_button.clicked.connect(self.finish)

    def start(self):
        # Start the timer
        self.timer.start(20)

    def stop(self):
        # Stop the timer and reset the position of the object
        self.timer.stop()
        self.x = 0
        self.y = 0
        self.image_label.move(self.x, self.y)

    def pause(self):
        # Pause the timer
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start(10)

    def finish(self):
        # Close the window
        self.close()

    def update_position(self):
        # Move the object in a square shape
        if self.x < 1600 and self.y == 0:
            self.x += 5
        elif self.x == 1600 and self.y < 700:
            self.y += 5
        elif self.x > 0 and self.y == 700:
            self.x -= 5
        elif self.x == 0 and self.y > 0:
            self.y -= 5

        # Set the position of the object
        self.image_label.move(self.x, self.y)

        # Print the real-time coordinates to the console
        print("X: {}, Y: {}".format(self.x, self.y))


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Set the layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Add the main window to the layout
        main_window = MainWindow()
        layout.addWidget(main_window)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

