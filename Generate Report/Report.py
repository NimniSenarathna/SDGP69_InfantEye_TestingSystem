from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont, QPalette, QColor, QBrush
from PyQt5.QtCore import Qt

class ReportWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Generated Report')
        self.setGeometry(100, 100, 1800, 900)

        # Set the background color of the main window
        palette = self.palette()
        palette.setBrush(QPalette.Window, QBrush(Qt.white))
        self.setPalette(palette)

        # Add the label for the main topic in top left alignment
        font = QFont()
        font.setPointSize(24)
        font.setUnderline(True)

        label = QLabel(self)
        label.setText('Generated Report')
        label.setFont(font)
        label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        label.setStyleSheet('color: blue;')
        label.setGeometry(20, 20, 500, 50)

if __name__ == '__main__':
    app = QApplication([])
    window = ReportWindow()
    window.show()
    app.exec_()

