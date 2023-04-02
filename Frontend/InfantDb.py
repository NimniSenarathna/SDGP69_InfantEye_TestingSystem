import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from mysql.connector import connect


class TablePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Table Page")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #D0DAFF;")

        container = QTableWidget(self)
        container.setGeometry(50, 50, 700, 500)
        container.setStyleSheet("background-color: white;")

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
                    item.setFlags(item.flags() ^ ~Qt.ItemIsEnabled)
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


