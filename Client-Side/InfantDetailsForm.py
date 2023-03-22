import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QHBoxLayout, QDateEdit, QCheckBox
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtSql import QSqlDatabase, QSqlQuery


class DetailsFormPage(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Infants Details Form")
        #self.setFixedSize(1900, 1000)
        
        # Set window size
        self.setGeometry(100, 100, 800, 600)
        
        # Set the background color of the window to blue
        self.setStyleSheet("background-color: #D0DAFF;")

        # Create a container for the form
        form_container = QWidget()
        
        form_container.setGeometry(QRect(0, 0, 800, 600))
        form_container.setObjectName("form_container")
        
        # Set the background color of the form container
        form_container.setStyleSheet("background-color: white;")
        
        # Set the font size of the input fields and buttons
        font = QFont()
        font.setPointSize(12)

        # Create form elements
        name_label = QLabel("Name*")
        first_name_input = QLineEdit()
        first_name_input.setFixedSize(200, 30)  
        first_name_input.setFont(font) 
        surname_input = QLineEdit()
        surname_input.setFixedSize(200, 30)
        surname_input.setFont(font)
        gender_type_label = QLabel("Gender*")
        gender_type_female = QCheckBox("Female")
        gender_type_male = QCheckBox("Male")
        gender_type_layout = QHBoxLayout()
        gender_type_layout.addWidget(gender_type_female)
        gender_type_layout.addWidget(gender_type_male)
        gender_type_widget = QWidget()
        gender_type_widget.setLayout(gender_type_layout)
        dob_label = QLabel("Date of Birth")
        dob_input = QDateEdit()
        dob_input.setFixedSize(200, 30)
        dob_input.setFont(font)
        test_id_label = QLabel("Test ID")
        test_id_input = QLineEdit()
        test_id_input.setFixedSize(200, 30)
        test_id_input.setFont(font)
        parent_type_label = QLabel("Parent Type*")
        parent_type_mother = QCheckBox("Mother")
        parent_type_father = QCheckBox("Father")
        parent_type_layout = QHBoxLayout()
        parent_type_layout.addWidget(parent_type_mother)
        parent_type_layout.addWidget(parent_type_father)
        parent_type_widget = QWidget()
        parent_type_widget.setLayout(parent_type_layout)
        parent_name_label = QLabel("Parent's Full Name")
        parent_name_input = QLineEdit()
        parent_name_input.setFixedSize(200, 30)
        parent_name_input.setFont(font)
        nic_number_label = QLabel("NIC Number")
        nic_number_input = QLineEdit()
        nic_number_input.setFixedSize(200, 30)
        nic_number_input.setFont(font)
        contact_number_label = QLabel("Contact Number")
        contact_number_input = QLineEdit()
        contact_number_input.setFixedSize(200, 30)
        contact_number_input.setFont(font)
        email_label = QLabel("Email Address")
        email_input = QLineEdit()
        email_input.setFixedSize(200, 30)
        email_input.setFont(font)
        
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
        form_container.setLayout(form_layout)

        # Add buttons to form container
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.login_button)
        button_layout.addWidget(submit_button)
        button_layout.addWidget(db_button)
        form_layout.addLayout(button_layout, 9, 1, 1, 2)

        # Set the central widget to the form container
        self.setCentralWidget(form_container)
        
        # Connect the submit button to the submit_details function
        submit_button.clicked.connect(self.submit_details)

        # Establish a connection to the database
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('infantsdetailsdatabase.db')
        if not self.db.open():
            print('Could not connect to database')
            
    def submit_details(self):
        # Create a QSqlQuery object to insert the user details into the database
        query = QSqlQuery()
        query.prepare('INSERT INTO users (name, surname, gender, dob, test_id, parent_type, parent_name, nic_number, contact_number, email) '
                  'VALUES (:name, :surname, :gender, :dob, :test_id, :parent_type, :parent_name, :nic_number, :contact_number, :email)')
        query.bindValue(':name', self.first_name_input.text())
        query.bindValue(':surname', self.surname_input.text())
        query.bindValue(':gender', self.gender_input.text())
        query.bindValue(':dob', self.dob_input.date().toString('yyyy-MM-dd'))
        query.bindValue(':test_id', self.test_id_input.text())
        query.bindValue(':parent_type', self.parent_type_input.text())
        query.bindValue(':parent_name', self.parent_name_input.text())
        query.bindValue(':nic_number', self.nic_number_input.text())
        query.bindValue(':contact_number', self.contact_number_input.text())
        query.bindValue(':email', self.email_input.text())
        if query.exec_():
           print('User details inserted into database')
        else:
           print('Error inserting user details into database:', query.lastError().text())

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DetailsFormPage()
    window.show()
    sys.exit(app.exec_())


