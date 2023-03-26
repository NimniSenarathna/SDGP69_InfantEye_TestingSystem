import sys
import traceback
import mysql.connector
from PyQt6.QtCore import QRect, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QGridLayout, QCheckBox, QPushButton, QDateEdit, QFormLayout, QSizePolicy
from PyQt6.QtGui import QFont, QPixmap


class MyPage(QWidget):
    def __init__(self):
        super().__init__()
        
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
        first_name_input = QLineEdit()
        first_name_input.setFixedSize(200, 30)  
        first_name_input.setFont(QFont()) 
        surname_input = QLineEdit()
        surname_input.setFixedSize(200, 30)
        surname_input.setFont(QFont())
        gender_type_label = QLabel("Gender*")
        gender_type_female = QCheckBox("Female")
        gender_type_male = QCheckBox("Male")
        gender_type_layout = QHBoxLayout()
        gender_type_layout.addWidget(gender_type_female)
        gender_type_layout.addWidget(gender_type_male)
        gender_type_widget = QWidget()
        gender_type_widget.setLayout(gender_type_layout)
        dob_label = QLabel("Date of Birth*")
        dob_input = QDateEdit()
        dob_input.setFixedSize(200, 30)
        dob_input.setFont(QFont())
        test_id_label = QLabel("Test ID*")
        test_id_input = QLineEdit()
        test_id_input.setFixedSize(200, 30)
        test_id_input.setFont(QFont())
        parent_type_label = QLabel("Parent Type*")
        parent_type_mother = QCheckBox("Mother")
        parent_type_father = QCheckBox("Father")
        parent_type_layout = QHBoxLayout()
        parent_type_layout.addWidget(parent_type_mother)
        parent_type_layout.addWidget(parent_type_father)
        parent_type_widget = QWidget()
        parent_type_widget.setLayout(parent_type_layout)
        parent_name_label = QLabel("Parent's Full Name*")
        parent_name_input = QLineEdit()
        parent_name_input.setFixedSize(200, 30)
        parent_name_input.setFont(QFont())
        nic_number_label = QLabel("NIC Number*")
        nic_number_input = QLineEdit()
        nic_number_input.setFixedSize(200, 30)
        nic_number_input.setFont(QFont())
        contact_number_label = QLabel("Contact Number*")
        contact_number_input = QLineEdit()
        contact_number_input.setFixedSize(200, 30)
        contact_number_input.setFont(QFont())
        email_label = QLabel("Email Address*")
        email_input = QLineEdit()
        email_input.setFixedSize(200, 30)
        email_input.setFont(QFont())
        
        # Create buttons
        self.login_button = QPushButton("Return to LOGINPAGE")
        self.submit_button = QPushButton("Submit & start Testing")
        db_button = QPushButton("Select from existing database")
        
        # Connect the submit button's clicked signal to the submit_details slot
        self.submit_button.clicked.connect(self.submit_details)
        print("Submit button connected.")
        
        # Change the color of the login button
        self.login_button.setStyleSheet("background-color: #235FF9; color: white;")

        # Change the color of the submit button
        self.submit_button.setStyleSheet("background-color: #235FF9; color: white;")

        # Change the color of the db button
        db_button.setStyleSheet("background-color: #65C8FF; color: white;")
        
        # Add form elements and buttons to form container
        form_layout = QGridLayout()
        form_layout.addWidget(name_label, 0, 0)
        form_layout.addWidget(first_name_input, 0, 1)
        form_layout.addWidget(surname_input, 0, 2)
        form_layout.addWidget(gender_type_label, 1, 0)
        form_layout.addWidget(gender_type_widget, 1, 1)
        form_layout.addWidget(dob_label, 2, 0)
        form_layout.addWidget(dob_input, 2, 1)
        form_layout.addWidget(test_id_label, 3, 0)
        form_layout.addWidget(test_id_input, 3, 1)
        form_layout.addWidget(parent_type_label, 4, 0)
        form_layout.addWidget(parent_type_widget, 4, 1)
        form_layout.addWidget(parent_name_label, 5, 0)
        form_layout.addWidget(parent_name_input, 5, 1)
        form_layout.addWidget(nic_number_label, 6, 0)
        form_layout.addWidget(nic_number_input, 6, 1)
        form_layout.addWidget(contact_number_label, 7, 0)
        form_layout.addWidget(contact_number_input, 7, 1)
        form_layout.addWidget(email_label, 8, 0)
        form_layout.addWidget(email_input, 8, 1)
        
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
        
        # Connect to the database
        try:
           self.db = mysql.connector.connect(
           host="localhost",
           user="root",
           password="Mikan_211702",
           db="infant_database"
           )
           
           print("Database connection successful!")
        except mysql.connector.Error as error:
           print("Error while connecting to MySQL database: ", error)

    # Insert data into the table when the submit button is clicked
    def submit_details(self):
        print("Submitting details.")
        first_name = self.first_name_input.text()
        print("First name:", first_name)
        surname = self.surname_input.text()
        print("Surname:", surname)
        gender = self.gender_input.currentText()
        print("Gender:", gender)
        dob = self.dob_input.date().toString("yyyy-MM-dd")
        print("Date of birth:", dob)
        test_id = self.test_id_input.text()
        print("Test ID:", test_id)
        parent_type = self.parent_type_input.currentText()
        print("Parent type:", parent_type)
        parent_name = self.parent_name_input.text()
        print("Parent name:", parent_name)
        nic_number = self.nic_number_input.text()
        print("NIC number:", nic_number)
        contact_number = self.contact_number_input.text()
        print("Contact number:", contact_number)
        email = self.email_input.text()
        print("Email:", email)
        
        print("Before try-except block") # Add this line to check if the code is being executed properly
            
        try:
           cursor = self.db.cursor()
           query = "INSERT INTO infants (first_name, surname, gender, dob, test_id, parent_type, parent_name, nic_number, contact_number, email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
           values = (first_name, surname, gender, dob, test_id, parent_type, parent_name, nic_number, contact_number, email)
           print("Executing query:", query)
           print("Values to be inserted:", values)
           cursor.execute(query, values)
           print("Query executed successfully")
           self.db.commit()
           print(cursor.rowcount, "record inserted.")
           print("Insert successful.")
        except Exception as e:
           print(f"Error: {e}")
           print(traceback.format_exc())
           
        finally:
           if 'cursor' in locals() and cursor is not None:
              cursor.close()
              print("Cursor connection closed.")
           if 'self.db' in locals() and self.db is not None:
              self.db.close()
              print("Database connection closed.")


            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    page = MyPage()
    page.show()
    sys.exit(app.exec())



