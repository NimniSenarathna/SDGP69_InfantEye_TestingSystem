import sys

from PyQt6.QtCore import QDate
from PyQt6.QtGui import QIcon, QPixmap, QIntValidator
from PyQt6.QtSql import QSqlQuery, QSqlDatabase
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QStackedWidget, QLabel, \
    QLineEdit, QSizePolicy, QGridLayout, QDateEdit, QComboBox


class Login(QWidget):  ########Login Page##############
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Login')
        self.setWindowIcon(QIcon(''))
        self.window_width, self.window_height = 600, 350
        self.setFixedSize(self.window_width, self.window_height)

        layout = QGridLayout()          ##Layout##
        fulllayout = QHBoxLayout()
        self.setLayout(fulllayout)

        imglabel = QLabel(self)       ##image##
        pixmap = QPixmap('baby.jpg')
        imglabel.setPixmap(pixmap)
        fulllayout.addWidget(imglabel)
        fulllayout.addLayout(layout)

        imglabel1 = QLabel(self)                ##Logo##
        pixmap = QPixmap('logoMINI.JPG')
        imglabel1.setPixmap(pixmap)
        imglabel1.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        layout.addWidget(imglabel1, 0, 2)

        labels = {}                       ########Labels and Input fields####
        self.lineEdits = {}

        labels['Login'] = QLabel('Login')
        labels['Login'].setStyleSheet('font-size: 25px; color: blue;')
        labels['Username'] = QLabel('Username')
        labels['Password'] = QLabel('Password')
        labels['register'] = QLabel("Don't have an account? Signup")
        labels['register'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        labels['Login'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        labels['Username'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        labels['Password'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.lineEdits['Username'] = QLineEdit()
        self.lineEdits['Username'].setPlaceholderText("Username")
        self.lineEdits['Password'] = QLineEdit()
        self.lineEdits['Password'].setPlaceholderText("Password")
        self.lineEdits['Password'].setEchoMode(QLineEdit.EchoMode.Password)

        layout.addWidget(labels['Login'], 0, 0, 1, 1)

        layout.addWidget(labels['Username'], 2, 0, 1, 1)
        layout.addWidget(self.lineEdits['Username'], 2, 1, 1, 2)

        layout.addWidget(labels['Password'], 3, 0, 1, 1)
        layout.addWidget(self.lineEdits['Password'], 3, 1, 1, 2)

        layout.addWidget(labels['register'], 6, 0, 1, 2)

        button_login = QPushButton('&Log In', clicked=self.checkcredential)            ####Login Button Click ######
        layout.addWidget(button_login, 4, 2, 1, 1)
        button_register = QPushButton('&Signup', clicked=self.open_second_gui)              ####Signup page button#####
        layout.addWidget(button_register, 6, 2, 1, 1)

        self.status = QLabel('')                                       #########Validate Error Message##########
        self.status.setStyleSheet('font-size: 13px; color: red;')
        layout.addWidget(self.status, 4, 0, 1, 1)

        self.connectToDB()

    def connectToDB(self):                                     ######Connecting to DataBase########
        # https://doc.qt.io/qt-5/sql-driver.html
        db = QSqlDatabase.addDatabase('QMYSQL')
        db.setDatabaseName('mysql+pymysql://root:localhost:3306/users')

        if not db.open():
            self.status.setText('Connection failed')

    def checkcredential(self):                                           ##########Validate inputs##########
        username = self.lineEdits['Username'].text()
        password = self.lineEdits['Password'].text()

        query = QSqlQuery()
        query.prepare('SELECT * FROM Users WHERE Username=:username')
        query.bindValue(':username', username)
        query.exec()
        if len(username):
            if len(password):
                if query.first():
                    if query.value('Password') == password:
                        print("works")
                    else:
                        self.status.setText('Password is incorrect')
                else:
                    self.status.setText('User not found')
            else:
                self.status.setText('enter password')
        else:
            self.status.setText('enter username')

    def open_second_gui(self):                      #######Signup page open function#######
        stacked_widget.setCurrentIndex(1)


class Signup(QWidget):             ########Signup Page#########
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Signup')
        self.setWindowIcon(QIcon(''))
        self.window_width, self.window_height = 600, 400
        self.setFixedSize(self.window_width, self.window_height)

        layout = QGridLayout()                             #####Layout#####
        self.setLayout(layout)

        labels = {}                                          ##########Labels and Input fields############
        self.lineEdits = {}

        labels['details'] = QLabel('details')
        labels['details'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        labels['Signup'] = QLabel('Signup')
        labels['Signup'].setStyleSheet('font-size: 25px; color: blue;')
        labels['Signup'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        labels['name'] = QLabel('name')
        labels['name'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        labels['username'] = QLabel('username')
        labels['username'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        labels['gender'] = QLabel('gender')
        labels['dateofbirth'] = QLabel('dateofbirth')
        labels['gender'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        labels['dateofbirth'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        labels['nic'] = QLabel('nic')
        labels['mobile'] = QLabel('mobile')
        labels['nic'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        labels['mobile'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        labels['npassword'] = QLabel('npassword')
        labels['cpassword'] = QLabel('cpassword')
        labels['npassword'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        labels['cpassword'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.lineEdits['details'] = QLineEdit()
        self.lineEdits['details'].setPlaceholderText("Your details")
        self.lineEdits['firstname'] = QLineEdit()
        self.lineEdits['firstname'].setPlaceholderText("First name")
        self.lineEdits['lastname'] = QLineEdit()
        self.lineEdits['lastname'].setPlaceholderText("Last name")
        self.lineEdits['username'] = QLineEdit()
        self.lineEdits['username'].setPlaceholderText("Username")

        self.lineEdits['gender'] = QLineEdit()
        self.lineEdits['gender'].setPlaceholderText("Male/Female/Prefer not to say")
        self.lineEdits['dateofbirth'] = QLineEdit()
        self.lineEdits['dateofbirth'].setPlaceholderText("YYYY-MM-DD")

        validator = QIntValidator()                 ########Integer Validator########

        self.lineEdits['nic'] = QLineEdit()
        self.lineEdits['nic'].setPlaceholderText("Nic number")
        self.lineEdits['mobile'] = QLineEdit()
        self.lineEdits['mobile'].setValidator(validator)
        self.lineEdits['mobile'].setPlaceholderText("Mobile number")
        self.lineEdits['npassword'] = QLineEdit()
        self.lineEdits['npassword'].setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEdits['npassword'].setPlaceholderText("New password")
        self.lineEdits['cpassword'] = QLineEdit()
        self.lineEdits['cpassword'].setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEdits['cpassword'].setPlaceholderText("Confirm Password")

        imglabel1 = QLabel(self)                                   #######Logo#######
        pixmap = QPixmap('logoMINI.JPG')
        imglabel1.setPixmap(pixmap)
        imglabel1.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        layout.addWidget(imglabel1, 0, 4, 2, 1)

        layout.addWidget(labels['Signup'], 0, 0, 2, 1)
        layout.addWidget(labels['details'], 2, 0, 1, 1)
        layout.addWidget(self.lineEdits['details'], 3, 0, 1, 5)
        layout.addWidget(labels['name'], 4, 0, 1, 1)
        layout.addWidget(self.lineEdits['firstname'], 4, 1, 1, 2)
        layout.addWidget(self.lineEdits['lastname'], 4, 3, 1, 2)
        layout.addWidget(labels['username'], 5, 0, 1, 1)
        layout.addWidget(self.lineEdits['username'], 5, 1, 1, 2)

        layout.addWidget(labels['gender'], 6, 0, 1, 1)
        layout.addWidget(self.lineEdits['gender'], 6, 1, 1, 2)
        layout.addWidget(labels['dateofbirth'], 7, 0, 1, 1)
        layout.addWidget(self.lineEdits['dateofbirth'], 7, 1, 1, 2)

        layout.addWidget(labels['nic'], 8, 0, 1, 1)
        layout.addWidget(self.lineEdits['nic'], 8, 1, 1, 2)
        layout.addWidget(labels['mobile'], 9, 0, 1, 1)
        layout.addWidget(self.lineEdits['mobile'], 9, 1, 1, 2)
        layout.addWidget(labels['npassword'], 10, 0, 1, 1)
        layout.addWidget(self.lineEdits['npassword'], 10, 1, 1, 2)
        layout.addWidget(labels['cpassword'], 11, 0, 1, 1)
        layout.addWidget(self.lineEdits['cpassword'], 11, 1, 1, 2)

        button_Signup = QPushButton('&Signup', clicked=self.checkcredential)        ########Button to Signup######
        layout.addWidget(button_Signup, 12, 4, 1, 1)

        button_Register = QPushButton('&Return login', clicked=self.go_back)         #######Button to first page########
        layout.addWidget(button_Register, 12, 3, 1, 1)

        self.status = QLabel('')                              ########Validate Error Message#######
        self.status.setStyleSheet('font-size: 13px; color: red;')
        layout.addWidget(self.status, 13, 0, 1, 2)

    def checkcredential(self):                                       ########Validate Inputs########
        details = self.lineEdits['details'].text()
        firstname = self.lineEdits['firstname'].text()
        lastname = self.lineEdits['lastname'].text()
        username = self.lineEdits['username'].text()
        gender = self.lineEdits['gender'].text()
        dateofbirth = self.lineEdits['dateofbirth'].text().strip()
        date = QDate.fromString(dateofbirth, "yyyy-MM-dd")
        nic = self.lineEdits['nic'].text()
        mobile = self.lineEdits['mobile'].text()
        npassword = self.lineEdits['npassword'].text()
        cpassword = self.lineEdits['cpassword'].text()

        if len(details) > 0:
            if len(firstname) > 0:
                if len(lastname) > 0:
                    if len(username) > 0:
                        if len(gender) > 0:
                            if gender.lower() == 'male' or gender.lower() == 'female' or gender.lower() == 'prefer not to say':
                                if len(dateofbirth) > 0:
                                    if date.isValid():
                                        if len(nic) > 0:
                                            if len(mobile) > 0:
                                                if len(npassword) > 0:
                                                    if len(npassword) >= 4:
                                                        if len(cpassword) > 0:
                                                            if npassword == cpassword:
                                                                self.status.setText('all ok')
                                                            else:
                                                                self.status.setText("confirm password dosn't match")
                                                        else:
                                                            self.status.setText('confirm password')
                                                    else:
                                                        self.status.setText('password must be more than 4 digits')
                                                else:
                                                    self.status.setText('enter new password')
                                            else:
                                                self.status.setText('enter mobile number')
                                        else:
                                            self.status.setText('enter nic')
                                    else:
                                        self.status.setText('invalid date')
                                else:
                                    self.status.setText('enter date')
                            else:
                                self.status.setText('not valid')
                        else:
                            self.status.setText('enter gender')
                    else:
                        self.status.setText('enter username')
                else:
                    self.status.setText('enter lastname')
            else:
                self.status.setText('enter firstname')
        else:
            self.status.setText('enter details')

    def go_back(self):                             ###########Function to previous page############
        stacked_widget.setCurrentIndex(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    stacked_widget = QStackedWidget()

    first_gui = Login()
    second_gui = Signup()

    stacked_widget.addWidget(first_gui)
    stacked_widget.addWidget(second_gui)

    stacked_widget.show()

    sys.exit(app.exec())
