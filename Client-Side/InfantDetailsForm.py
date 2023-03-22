import sys
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QGridLayout, QCheckBox, QPushButton, QDateEdit, QDesktopWidget
from PyQt5.QtGui import QFont

class MyPage(QWidget):
    def __init__(self):
        super().__init__()
        
         # Set the window size as a percentage of the screen size
        screen_size = QDesktopWidget().screenGeometry(-1)
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
        
        self.setWindowTitle("Infants Details Form")

        # Create a white container in the middle of the page
        container = QWidget(self)
        container.setStyleSheet("background-color: white;")

        # Create the form layout
        form_layout = QVBoxLayout()

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
        
        # Define a custom method to validate the parent type checkboxes
        def validate_gender_type(state):
            sender = app.sender()
            if sender == gender_type_female and state == Qt.Checked:
                gender_type_male.setChecked(False)
            elif sender == gender_type_male and state == Qt.Checked:
               gender_type_female.setChecked(False)

        # Connect the stateChanged signal of the parent type checkboxes to the validate_parent_type method
        gender_type_female.stateChanged.connect(validate_gender_type)
        gender_type_male.stateChanged.connect(validate_gender_type)
        
        # Define a custom method to validate the parent type checkboxes
        def validate_parent_type(state):
            sender = app.sender()
            if sender == parent_type_mother and state == Qt.Checked:
                parent_type_father.setChecked(False)
            elif sender == parent_type_father and state == Qt.Checked:
               parent_type_mother.setChecked(False)

        # Connect the stateChanged signal of the parent type checkboxes to the validate_parent_type method
        parent_type_mother.stateChanged.connect(validate_parent_type)
        parent_type_father.stateChanged.connect(validate_parent_type)
        
        # Create buttons
        self.login_button = QPushButton("Return to LOGINPAGE")
        submit_button = QPushButton("Submit & start Testing")
        db_button = QPushButton("Select from existing database")
        
        # Change the color of the login button
        self.login_button.setStyleSheet("background-color: #235FF9; color: white;")

        # Change the color of the submit button
        submit_button.setStyleSheet("background-color: #235FF9; color: white;")

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
        button_layout.addWidget(submit_button)
        button_layout.addWidget(db_button)
        form_layout.addLayout(button_layout, 9, 1, 1, 2)

        # Set the layout of the container
        container.setLayout(form_layout)

        # Add the container to the main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(container)

        # Set the main layout of the page
        self.setLayout(main_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    page = MyPage()
    page.show()
    sys.exit(app.exec_())


