import sys
from PyQt5 import QtSql,QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import admin
import userpanel
import staffpanel


class login(admin.adminp,userpanel.userp,staffpanel.staffp):
    'Login ka page'

    def __init__(self):
        #admin.adminp, userpanel.userp, staffpanel.staffp.__init__(self)

        self.initUI1()

    def initUI1(self):
        'Login ka main basic Page'

        self.l=QWidget()

        #label aur text id ke liye
        self.usernamel = QLineEdit(self.l)
        self.usernamel.setFrame(False)
        self.usernamel.setPlaceholderText("Enter Username")
        self.usernamel.setStyleSheet("QLineEdit{padding: 1px;border-radius: 8px;color:black;background:white}")
        self.usernamel.move(290, 300)
        self.usernamel.resize(225, 40)

        #label and text password ke liye
        self.passwordl=QLineEdit(self.l)
        self.passwordl.setFrame(False)
        self.passwordl.setPlaceholderText("Enter Password")
        self.passwordl.setEchoMode(QLineEdit.Password)
        self.passwordl.setStyleSheet("QLineEdit{padding: 1px;border-radius: 8px;background:white;color:black}")
        self.passwordl.move(290, 370)
        self.passwordl.resize(225, 40)

        #staff login ka khatka
        self.lbtn1 = QToolButton(self.l)
        self.lbtn1.setText(" Staff Login ")
        self.lbtn1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.lbtn1.setFont(QFont('Arial', 12,weight=QFont.Bold))
        self.lbtn1.setStyleSheet("QToolButton{padding:10px; background-color: orange; color:black; border-style: outset; border-width: 2px; border-radius: 22px; border-color: black;}" "QToolButton:hover{background-color: tomato; color:white;}")
        self.lbtn1.setToolTip("This is login for Administrator, Faculities & Management Members")
        self.lbtn1.setIcon(QIcon('icons/user-tie-solid.svg'))
        self.lbtn1.setIconSize(QSize(150,150))
        self.lbtn1.clicked.connect(self.adminl)
        self.lbtn1.move(75, 250)

        #student login ka khatka
        self.lbtn2 = QToolButton(self.l)
        self.lbtn2.setText("Student Login")
        self.lbtn2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.lbtn2.setFont(QFont('Arial',12,weight=QFont.Bold))
        self.lbtn2.setStyleSheet("QToolButton{padding:10px; background-color: orange; color:black; border-style: outset; border-width: 2px; border-radius: 22px; border-color: black;}" "QToolButton:hover{background-color: tomato; color:white;}")
        self.lbtn2.setToolTip("This is login for Students")
        self.lbtn2.setIcon(QIcon('icons/user-graduate-solid.svg'))
        self.lbtn2.setIconSize(QSize(150, 150))
        self.lbtn2.clicked.connect(self.userl)
        self.lbtn2.move(550,250)

        # About ka button
        self.lbtn3 = QPushButton("About Us", self.l)
        self.lbtn3.setStyleSheet("QPushButton{padding:10px; background-color: orange; color:black; border-style: outset; border-width: 2px; border-radius: 22px; border-color: black;}" "QPushButton:hover{background-color: tomato; color:white;}")
        self.lbtn3.setIcon(QIcon('icons/info-circle-solid.svg'))
        self.lbtn3.setToolTip("Shows Developer Information")
        self.lbtn3.clicked.connect(self.about)
        self.lbtn3.move(350, 500)

        #Heading of the code
        self.llabel=QLabel("Attendance Tracker",self.l)
        self.llabel.setAlignment(Qt.AlignCenter)
        self.llabel.setFont(QFont('Times New Roman',34,weight=QFont.Bold))
        self.llabel.move(170,30)

       #GIT ka logo
        self.clogo = QLabel(self.l)
        pixmap = QPixmap('images/latest')
        self.clogo.setPixmap(pixmap)
        self.clogo.move(340,125)

        self.l.setWindowTitle("Attendance Tracker - Login Page")
        self.l.setStyleSheet("* {background: qconicalgradient(cx:0.5, cy:0.5, angle:180,stop:0 #EE7752, stop:0.25 #E73C7E, stop:0.5 #23A6D5, stop:1 #23D5AB)}")
        self.l.setGeometry(100, 100, 800, 600)
        self.l.show()

    def about(self):
        QMessageBox.information(self.l, "About Developer", "Prerit Mathur\nmathur.prerit@gmail.com\n+919166793396", QMessageBox.Ok,QMessageBox.Ok)

    #Login ke admin panel ke liye
    def adminl(self):

        if self.usernamel.text() == 'admin':
            if self.passwordl.text() == '12345678':

                self.initUI2()
            else:
                QMessageBox.warning(self.l, "Warning", "Enter Correct Password", QMessageBox.Ok, QMessageBox.Ok)

        else:

            db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName('atdata.db')

            if not db.open():
                QMessageBox.critical(None, qApp.tr("connect open database"), qApp.tr("Unable to establish a DB"),QMessageBox.Cancel)

                return False

            query = QtSql.QSqlQuery()

            sql = "select spassword from staff where semail='%s' " % (self.usernamel.text())
            query.exec_(sql)
            row = []
            while query.next():
                row += [[query.value(index) for index in range(1)]]

            if row[0][0] == self.passwordl.text():
                self.initUI4()
            else:
                QMessageBox.warning(self.l, "Caution", "Enter Correct Password", QMessageBox.Ok,QMessageBox.Ok)

    #Login ke user panel ke liye
    def userl(self):

        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('atdata.db')

        if not db.open():
            QMessageBox.critical(None, qApp.tr("connect open database"), qApp.tr("Unable to establish a DB"),QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()

        sql1= "select pass from student_pass where roll='%s' " % (self.usernamel.text())
        query.exec_(sql1)
        row = []
        while query.next():
            row += [[query.value(index) for index in range(1)]]

            if row[0][0] == self.passwordl.text():
                self.initUI3()
            else:
                QMessageBox.warning(self.l, "Caution", "Enter Correct Password", QMessageBox.Ok,QMessageBox.Ok)

def main():
    app = QApplication(sys.argv)
    ex = login()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()