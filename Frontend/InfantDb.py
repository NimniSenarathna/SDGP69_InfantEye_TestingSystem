import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QWidget, QHBoxLayout, QPushButton
from mysql.connector import connect


class TablePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Table Page")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #D0DAFF;")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        container = QTableWidget(central_widget)
        container.setGeometry(50, 50, 700, 500)
        container.setStyleSheet("background-color: white;")

        button_container = QWidget(central_widget)
        button_container.setGeometry(50, 550, 700, 50)

        login_button = QPushButton("Return to LOGINPAGE", button_container)
        login_button.setGeometry(0, 0, 200, 50)
        login_button.setStyleSheet("background-color: #D9D9D9; color: #000000;")

        start_button = QPushButton("SELECT & START TESTING", button_container)
        start_button.setGeometry(250, 0, 200, 50)
        start_button.setStyleSheet("background-color: #D9D9D9; color: #000000;")

        home_button = QPushButton("RETURN TO HOMEPAGE", button_container)
        home_button.setGeometry(500, 0, 200, 50)
        home_button.setStyleSheet("background-color: #D9D9D9; color: #000000;")

        try:
            connection = connect(
                host="localhost",
                user="root",
                password="",
                database="InfantsDatabase"
            )
            print("Database connection successful!")
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM InfantsTable")
            rows = cursor.fetchall()
            num_rows = len(rows)

            print("Number of rows returned:", num_rows)

            container.setRowCount(num_rows)
            container.setColumnCount(10)
            container.setHorizontalHeaderLabels(["id", "name", "gender", "dob", "test_id", "parent_type", "parent_name", "nic_number", "contact_number", "email"])

            for i, row in enumerate(rows):
                for j, value in enumerate(row):
                    item = QTableWidgetItem(str(value))
                    if j in [0, 1, 9]:
                        item.setFlags(item.flags() & ~Qt.ItemIsSelectable)
                        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                    container.setItem(i, j, item)

        except Exception as e:
            print("Database connection failed:", e)

        finally:
            if connection:
                connection.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    page = TablePage()
    page.show()
    sys.exit(app.exec())

