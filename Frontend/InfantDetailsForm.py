import sys
import mysql.connector
from PyQt6.QtCore import QRect, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QGridLayout, QCheckBox, QPushButton, QDateEdit, QFormLayout, QSizePolicy
from PyQt6.QtGui import QFont, QPixmap


class MyPage(QWidget):
    def __init__(self):
        super().__init__()

        # Create the database and table
        self.create_database_and_table()
        
        # Set the window size as a percentage of the screen size
        screen_size = QApplication.primaryScreen().availableGeometry()
        width_percent = 0.5
        height_percent = 0.6
        self.setGeometry(
            int((1 - width_percent) * screen_size.width() / 2),
            int((1 - height_percent) * screen_size.height() / 2),
            int(width_percent * screen_size.width()),
            int(height_percent * screen_size.height())
        )

        # Set the background color to blue
        self.setStyleSheet("background-color: #D0DAFF;")
        
        self.setWindowTitle("ECTA")

        # Create a white container in the middle of the page
        container = QWidget(self)
        container.setStyleSheet("background-color: white;")
        
        container_layout = QVBoxLayout()

        # Create the heading label and add it to the container layout
        heading_label = QLabel("Infants Details Form", self)
        heading_label.setFont(QFont("Inter", 15, QFont.Weight.Bold))
        heading_label.setStyleSheet("color: #3136AF;")  # Set the text color to blue

        # Set up the blue underline
        underline = QLabel()
        underline.setStyleSheet("background-color: #869EF4;")
        underline.setFixedHeight(2)

        # Get the width of the text and add padding of 20 pixels on each side
        text_width = heading_label.fontMetrics().boundingRect(heading_label.text()).width() + 2
        underline.setFixedWidth(text_width)

        # Create a layout to hold the heading and underline
        heading_layout = QVBoxLayout()
        heading_layout.addWidget(heading_label)
        heading_layout.addWidget(underline)

        # Add the heading layout to the container layout
        container_layout.addLayout(heading_layout)

        # Create the icon widget and add it to the container layout
        icon = QLabel(self)               
        pixmap = QPixmap('ECTALogo.png').scaledToHeight(90) # Set the height of the pixmap to 50 pixels
        pixmap = pixmap.scaled(pixmap.width() // 2, pixmap.height() // 2)
        icon.setPixmap(pixmap)
        icon.setAlignment(Qt.AlignmentFlag.AlignTop) # Align the icon to the top

        # Create a vertical spacer item to push the form elements to the top of the container
        vspacer = QWidget(self)
        vspacer.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # Create a horizontal layout to add the vertical spacer, icon and spacer to the container layout
        hbox = QHBoxLayout()
        hbox.addWidget(heading_label)
        hbox.addWidget(vspacer)
        hbox.addWidget(icon)
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.setSpacing(0)

        # Add the horizontal layout to the container layout
        container_layout.addLayout(hbox)

        # Add a vertical spacer to push the form elements to the top of the container
        container_layout.addStretch(1)

        # Set the layout of the container
        container.setLayout(container_layout)

        # Create the form layout
        form_layout = QFormLayout()

        # Create form elements
        name_label = QLabel("Name*")
        self.first_name_input = QLineEdit()
        self.first_name_input.setFixedSize(200, 30)
        self.first_name_input.setFont(QFont())
        self.surname_input = QLineEdit()
        self.surname_input.setFixedSize(200, 30)
        self.surname_input.setFont(QFont())
        gender_type_label = QLabel("Gender*")
        self.gender_type_female = QCheckBox("Female")
        self.gender_type_male = QCheckBox("Male")
        self.gender_type_layout = QHBoxLayout()
        self.gender_type_layout.addWidget(self.gender_type_female)
        self.gender_type_layout.addWidget(self.gender_type_male)
        self.gender_type_widget = QWidget()
        self.gender_type_widget.setLayout(self.gender_type_layout)
        dob_label = QLabel("Date of Birth*")
        self.dob_input = QDateEdit()
        self.dob_input.setFixedSize(200, 30)
        self.dob_input.setFont(QFont())
        test_id_label = QLabel("Test ID*")
        self.test_id_input = QLineEdit()
        self.test_id_input.setFixedSize(200, 30)
        self.test_id_input.setFont(QFont())
        parent_type_label = QLabel("Parent Type*")
        self.parent_type_mother = QCheckBox("Mother")
        self.parent_type_father = QCheckBox("Father")
        self.parent_type_layout = QHBoxLayout()
        self.parent_type_layout.addWidget(self.parent_type_mother)
        self.parent_type_layout.addWidget(self.parent_type_father)
        self.parent_type_widget = QWidget()
        self.parent_type_widget.setLayout(self.parent_type_layout)
        parent_name_label = QLabel("Parent's Full Name*")
        self.parent_name_input = QLineEdit()
        self.parent_name_input.setFixedSize(200, 30)
        self.parent_name_input.setFont(QFont())
        nic_number_label = QLabel("NIC Number*")
        self.nic_number_input = QLineEdit()
        self.nic_number_input.setFixedSize(200, 30)
        self.nic_number_input.setFont(QFont())
        contact_number_label = QLabel("Contact Number*")
        self.contact_number_input = QLineEdit()
        self.contact_number_input.setFixedSize(200, 30)
        self.contact_number_input.setFont(QFont())
        email_label = QLabel("Email Address*")
        self.email_input = QLineEdit()
        self.email_input.setFixedSize(200, 30)
        self.email_input.setFont(QFont())

        # Create buttons
        self.login_button = QPushButton("Return to LOGINPAGE")
        self.submit_button = QPushButton("Submit & start Testing")
        db_button = QPushButton("Select from existing database")

        # Connect button to function
        self.submit_button.clicked.connect(self.submit_data)

        # Add form elements and buttons to form container
        form_layout = QGridLayout()
        form_layout.addWidget(name_label, 0, 0)
        form_layout.addWidget(self.first_name_input, 0, 1)
        form_layout.addWidget(self.surname_input, 0, 2)
        form_layout.addWidget(gender_type_label, 1, 0)
        form_layout.addWidget(self.gender_type_widget, 1, 1)
        form_layout.addWidget(dob_label, 2, 0)
        form_layout.addWidget(self.dob_input, 2, 1)
        form_layout.addWidget(test_id_label, 3, 0)
        form_layout.addWidget(self.test_id_input, 3, 1)
        form_layout.addWidget(parent_type_label, 4, 0)
        form_layout.addWidget(self.parent_type_widget, 4, 1)
        form_layout.addWidget(parent_name_label, 5, 0)
        form_layout.addWidget(self.parent_name_input, 5, 1)
        form_layout.addWidget(nic_number_label, 6, 0)
        form_layout.addWidget(self.nic_number_input, 6, 1)
        form_layout.addWidget(contact_number_label, 7, 0)
        form_layout.addWidget(self.contact_number_input, 7, 1)
        form_layout.addWidget(email_label, 8, 0)
        form_layout.addWidget(self.email_input, 8, 1)

        # Add buttons to form container
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.login_button)
        button_layout.addWidget(self.submit_button)
        button_layout.addWidget(db_button)
        form_layout.addLayout(button_layout, 9, 1, 1, 2)

        # Add the form layout to the container layout
        container_layout.addLayout(form_layout)

        # Set the layout of the container
        container.setLayout(container_layout)

        # Add the container to the main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(container)
        
        # Set the main layout of the page
        self.setLayout(main_layout)

    def create_database_and_table(self):
        # Connect to MySQL
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )

        # Check if the database exists
        cursor = conn.cursor()
        cursor.execute("SHOW DATABASES")
        databases = [x[0] for x in cursor]
        if "yourdatabase" not in databases:
            # Create the database
            cursor.execute("CREATE DATABASE yourdatabase")
            print("Database created")

        # Use the database
        conn.database = "yourdatabase"

        # Check if the table exists
        cursor.execute("SHOW TABLES")
        tables = [x[0] for x in cursor]
        if "yourtable" not in tables:
            # Create the table
            cursor.execute("""
                CREATE TABLE yourtable (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    gender VARCHAR(255) NOT NULL,
                    dob VARCHAR(255) NOT NULL,
                    test_id VARCHAR(255) NOT NULL,
                    parent_type VARCHAR(255) NOT NULL,
                    parent_name VARCHAR(255) NOT NULL,
                    nic_number VARCHAR(255) NOT NULL,
                    contact_number VARCHAR(255) NOT NULL,
                    email VARCHAR(255) NOT NULL
                )
            """)
            print("Table created")

        # Close the connection
        cursor.close()
        conn.close()

    def submit_data(self):
        # Get the data from the form
        name = self.first_name_input.text() + " " + self.surname_input.text()
        gender = self.gender_type_widget.currentText()
        dob = self.dob_input.text()
        test_id = self.test_id_input.text()
        parent_type = self.parent_type_widget.currentText()
        parent_name = self.parent_name_input.text()
        nic_number = self.nic_number_input.text()
        contact_number = self.contact_number_input.text()
        email = self.email_input.text()

        # Connect to MySQL
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="yourdatabase"
        )

        # Insert the data into the table
        cursor = conn.cursor()
        cursor.execute("INSERT INTO yourtable (name, gender, dob, test_id, parent_type, parent_name, nic_number, contact_number, email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (name, gender, dob, test_id, parent_type, parent_name, nic_number, contact_number, email,))
        conn.commit()
        print("Data inserted")

        # Close the connection
        cursor.close()
        conn.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    page = MyPage()
    page.show()
    sys.exit(app.exec())

