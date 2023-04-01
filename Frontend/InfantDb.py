from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, QLabel, QHBoxLayout, QPushButton
from PyQt6.QtGui import QColor, QBrush, QPixmap
from PyQt6.QtSql import QSqlDatabase, QSqlQuery
from PyQt6.QtCore import Qt

class DisplayPage(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window title
        self.setWindowTitle('Infant Database')

        # Set window size
        self.setGeometry(100, 100, 800, 600)

        # Set the background color of the window to blue
        self.setStyleSheet("background-color: #D0DAFF;")

        # Create main widget and set layout
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(50, 50, 50, 50)  # Add margins to the layout
        main_widget.setLayout(main_layout)

        # Create container widget and set background color to white
        container_widget = QWidget()
        container_widget.setStyleSheet("background-color: white;")
        container_layout = QVBoxLayout(container_widget)
        
        # Create label for heading
        heading_label = QLabel("ECTA Infant Database")
        heading_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        container_layout.addWidget(heading_label)
        
        # Add horizontal layout for the icon and spacer
        icon_layout = QHBoxLayout()
        icon_layout.addStretch()
        icon_label = QLabel()
        icon_label.setPixmap(QPixmap("ECTALogo.png").scaled(50, 50))
        icon_layout.addWidget(icon_label)
        container_layout.addLayout(icon_layout)

        # Create table widget and add to layout
        table_widget = QTableWidget()
        table_widget.setShowGrid(True)  # Show grid lines for the table
        table_widget.setStyleSheet("QTableView {gridline-color: black}") # Set grid color to black
        table_widget.setAlternatingRowColors(True)  # Set alternate row colors
        table_widget.verticalHeader().setVisible(False)  # Hide vertical header
        table_widget.verticalHeader().setDefaultSectionSize(20)


        container_layout.addWidget(table_widget)

        # Connect to database and retrieve data
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('database.db')
        db.open()

        query = QSqlQuery()
        query.exec_("SELECT * FROM infantsdetails")

        # Set table headers
        table_widget.setColumnCount(10)
        table_widget.setHorizontalHeaderLabels(['Test ID', 'Name', 'Surname', 'Gender', 'DOB', 'Parent name', 'Parent NIC no', 'Contact no', 'Email', 'Reg date'])

        # Set grid style and width for the table widget
        table_widget.setGridStyle(Qt.SolidLine)
        table_widget.setLineWidth(1)

        # Populate table with data from database
        row = 15
        while query.next():
            table_widget.insertRow(row)
            table_widget.setItem(row, 0, QTableWidgetItem(str(query.value(0))))
            table_widget.setItem(row, 1, QTableWidgetItem(query.value(1)))
            table_widget.setItem(row, 2, QTableWidgetItem(query.value(2)))
            table_widget.setItem(row, 3, QTableWidgetItem(query.value(3)))
            table_widget.setItem(row, 4, QTableWidgetItem(str(query.value(4))))
            table_widget.setItem(row, 5, QTableWidgetItem(query.value(5)))
            table_widget.setItem(row, 6, QTableWidgetItem(str(query.value(6))))
            table_widget.setItem(row, 7, QTableWidgetItem(str(query.value(7))))
            table_widget.setItem(row, 8, QTableWidgetItem(query.value(8)))
            table_widget.setItem(row, 9, QTableWidgetItem(str(query.value(9))))
            row += 1

        # Center-align the table contents
        header = table_widget.horizontalHeader()
        for i in range(header.count()):
            header.setSectionResizeMode(i, QHeaderView.Stretch)
        header.setStyleSheet("text-align:center;")
        header.setStretchLastSection(True)
    
        # Add container widget to the main layout
        main_layout.addWidget(container_widget)

        # Set main widget
        self.setCentralWidget(main_widget)
        
        # Create a horizontal layout for the buttons
        button_layout = QHBoxLayout()

        # Create the first button
        button1 = QPushButton("Return to LOGINPAGE")
        button1.setMaximumWidth(100)  # Set maximum width for the button
        button_layout.addWidget(button1)
        button1.setStyleSheet("background-color: #D9D9D9; color: black;")

        # Create the second button
        button2 = QPushButton("SELECT & START TESTING")
        button2.setMaximumWidth(100)  # Set maximum width for the button
        button_layout.addWidget(button2)
        button2.setStyleSheet("background-color: #D0DAFF; color: black;")
        
        # Create the third button
        button3 = QPushButton("RETURN TO HOME PAGE")
        button3.setMaximumWidth(100)  # Set maximum width for the button
        button_layout.addWidget(button3)
        button3.setStyleSheet("background-color: #D0DAFF; color: black;")

        # Add stretch to push the buttons to the right corner
        button_layout.addStretch()

        # Add the button layout to the container layout
        container_layout.addLayout(button_layout)

        # Add the container widget to the main layout
        main_layout.addWidget(container_widget)


if __name__ == '__main__':
    # Create application instance
    app = QApplication([])

    # Create and show main window
    window = DisplayPage()
    window.show()

    # Run event loop
    app.exec()



