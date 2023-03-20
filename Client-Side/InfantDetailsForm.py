import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QHBoxLayout, QDateEdit
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QIcon


class DetailsFormPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Infants Details Form")
        self.setFixedSize(1900, 1000)
        
        # Set the background color of the window to blue
        self.setStyleSheet("background-color: blue;")


        # Create a container for the form
        form_container = QWidget()
        form_container.setGeometry(QRect(0, 0, 800, 600))
        form_container.setObjectName("form_container")
        
        
        
        # Set the background color of the form container
        form_container.setStyleSheet("background-color: white;")

        # Create form elements
        name_label = QLabel("Name*")
        first_name_input = QLineEdit()
        surname_input = QLineEdit()
        gender_label = QLabel("Gender")
        gender_input = QLineEdit()
        dob_label = QLabel("Date of Birth")
        dob_input = QDateEdit()
        test_id_label = QLabel("Test ID")
        test_id_input = QLineEdit()
        parent_type_label = QLabel("Parent Type")
        parent_type_input = QLineEdit()
        parent_name_label = QLabel("Parent's Full Name")
        parent_name_input = QLineEdit()
        nic_number_label = QLabel("NIC Number")
        nic_number_input = QLineEdit()
        contact_number_label = QLabel("Contact Number")
        contact_number_input = QLineEdit()
        email_label = QLabel("Email Address")
        email_input = QLineEdit()

        # Create buttons
        submit_button = QPushButton("Submit")
        clear_button = QPushButton("Clear")
        cancel_button = QPushButton("Cancel")

        # Add form elements and buttons to form container
        form_layout = QGridLayout()
        form_layout.addWidget(name_label, 0, 0)
        form_layout.addWidget(first_name_input, 0, 1)
        form_layout.addWidget(surname_input, 0, 2)
        form_layout.addWidget(gender_label, 1, 0)
        form_layout.addWidget(gender_input, 1, 1)
        form_layout.addWidget(dob_label, 2, 0)
        form_layout.addWidget(dob_input, 2, 1)
        form_layout.addWidget(test_id_label, 3, 0)
        form_layout.addWidget(test_id_input, 3, 1)
        form_layout.addWidget(parent_type_label, 4, 0)
        form_layout.addWidget(parent_type_input, 4, 1)
        form_layout.addWidget(parent_name_label, 5, 0)
        form_layout.addWidget(parent_name_input, 5, 1)
        form_layout.addWidget(nic_number_label, 6, 0)
        form_layout.addWidget(nic_number_input, 6, 1)
        form_layout.addWidget(contact_number_label, 7, 0)
        form_layout.addWidget(contact_number_input, 7, 1)
        form_layout.addWidget(email_label, 8, 0)
        form_layout.addWidget(email_input, 8, 1)
        form_container.setLayout(form_layout)

        # Add buttons to form container
        button_layout = QHBoxLayout()
        button_layout.addWidget(submit_button)
        button_layout.addWidget(clear_button)
        button_layout.addWidget(cancel_button)
        form_layout.addLayout(button_layout, 9, 1, 1, 2)

        # Set the central widget to the form container
        self.setCentralWidget(form_container)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DetailsFormPage()
    window.show()
    sys.exit(app.exec_())


