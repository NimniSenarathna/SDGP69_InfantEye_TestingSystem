from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QLabel
from PyQt6.QtCore import Qt
import mysql.connector

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize UI
        self.initUI()

    def initUI(self):
        # Create main layout
        layout = QVBoxLayout()
        layout.setContentsMargins(0,0,0,0)

        # Set background color of main widget to blue
        self.setStyleSheet("background-color: blue;")

        # Create container widget
        container_widget = QWidget()

        # Set background color of container widget and table widget to white
        container_widget.setStyleSheet("background-color: white;")
        table_widget = QTableWidget()
        table_widget.setStyleSheet("background-color: white;")

        # Connect to database and populate table
        try:
            connection = mysql.connector.connect(
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

            table_widget.setRowCount(num_rows)
            table_widget.setColumnCount(10)
            table_widget.setHorizontalHeaderLabels(["id", "name", "gender", "dob", "test_id", "parent_type", "parent_name", "nic_number", "contact_number", "email"])

            for i, row in enumerate(rows):
                for j, value in enumerate(row):
                    item = QTableWidgetItem(str(value))
                    table_widget.setItem(i, j, item)

        except Exception as e:
            print("Database connection failed:", e)

        finally:
            if connection:
                connection.close()

        # Create heading label
        heading_label = QLabel("Ecta Infant Database")
        heading_label.setStyleSheet("font-size: 20px; font-weight: bold; margin-top: 10px; margin-bottom: 10px;")

        # Create button layout
        button_layout = QHBoxLayout()

        # Create buttons
        login_button = QPushButton("Return to LOGINPAGE")
        testing_button = QPushButton("SELECT & START TESTING")
        home_button = QPushButton("RETURN TO HOME PAGE")

        # Set background color of buttons to gray
        login_button.setStyleSheet("background-color: #D9D9D9;")
        testing_button.setStyleSheet("background-color: #D9D9D9;")
        home_button.setStyleSheet("background-color: #D9D9D9;")

        # Add buttons to button layout
        button_layout.addWidget(login_button)
        button_layout.addWidget(testing_button)
        button_layout.addWidget(home_button)

        # Add heading label, table widget, and button layout to container widget
        container_layout = QVBoxLayout()
        container_layout.addWidget(heading_label)
        container_layout.addWidget(table_widget)
        container_layout.addLayout(button_layout)
        container_widget.setLayout(container_layout)

        # Add container widget to main layout
        layout.addWidget(container_widget)

        # Set main layout for widget
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication([])
    ex = MyWidget()
    ex.show()
    app.exec()
