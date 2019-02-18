import sys
from PyQt5 import QtSql,QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import smtplib
from smtplib import *
from twilio.rest import Client
import crud_staff
import crud_student
import crud_attendance



class adminp(crud_student.crud,crud_staff.crud2,crud_attendance.crud3):
    'admin ka panel'



    def initUI2(self):
        'admin ka pura saaman'

        self.a=QDialog()

        self.grid=QGridLayout()

        #Managing student button h frnds
        self.abtn1=QToolButton(self.a)
        self.abtn1.setText("Update Student")
        self.abtn1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.abtn1.setIcon(QIcon('icons/graduation-cap-solid'))
        self.abtn1.setStyleSheet("QToolButton{padding:10px; background-color: orange; color:black; border-style: outset; border-width: 2px; border-radius: 22px; border-color: black;}" "QToolButton:hover{background-color: tomato; color:white;}")
        self.abtn1.setFont(QFont('Arial', 14, weight=QFont.Bold))
        self.abtn1.setIconSize(QSize(150, 150))
        self.abtn1.setFixedSize(200, 200)
        self.abtn1.setToolTip("Updating students in database")
        self.abtn1.clicked.connect(self.datastudent)

        #Managing Staff button h frnds
        self.abtn2=QToolButton(self.a)
        self.abtn2.setText("Update Staff")
        self.abtn2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.abtn2.setIcon(QIcon('icons/chalkboard-teacher-solid'))
        self.abtn2.setStyleSheet("QToolButton{padding:10px; background-color: orange; color:black; border-style: outset; border-width: 2px; border-radius: 22px; border-color: black;}" "QToolButton:hover{background-color: tomato; color:white;}")
        self.abtn2.setFont(QFont('Arial', 14, weight=QFont.Bold))
        self.abtn2.setIconSize(QSize(150, 150))
        self.abtn2.setFixedSize(200, 200)
        self.abtn2.setToolTip("Updating staff in database")
        self.abtn2.clicked.connect(self.datastaff)

        #Manage attendance ka button
        self.abtn3=QToolButton(self.a)
        self.abtn3.setText("Attendance")
        self.abtn3.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.abtn3.setIcon(QIcon('icons/user-graduate-solid.svg'))
        self.abtn3.setStyleSheet("QToolButton{padding:10px; background-color: orange; color:black; border-style: outset; border-width: 2px; border-radius: 22px; border-color: black;}" "QToolButton:hover{background-color: tomato; color:white;}")
        self.abtn3.setFont(QFont('Arial', 14, weight=QFont.Bold))
        self.abtn3.setFixedSize(200, 200)
        self.abtn3.setIconSize(QSize(150, 150))
        self.abtn3.setToolTip("Managing attendance of students")
        self.abtn3.clicked.connect(self.dataattendance)

        #Information button h frnds
        self.abtn4=QToolButton(self.a)
        self.abtn4.setText("Publish Notice")
        self.abtn4.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.abtn4.setIcon(QIcon('icons/bullhorn-solid'))
        self.abtn4.setFont(QFont('Arial', 14, weight=QFont.Bold))
        self.abtn4.setStyleSheet("QToolButton{padding:10px; background-color: orange; color:black; border-style: outset; border-width: 2px; border-radius: 22px; border-color: black;}" "QToolButton:hover{background-color: tomato; color:white;}")
        self.abtn4.setIconSize(QSize(150, 150))
        self.abtn4.setFixedSize(200, 200)
        self.abtn4.setToolTip("Send a notice to students")
        self.abtn4.clicked.connect(self.notice)

        # Mail/SMS button h frnds
        self.abtn5= QToolButton(self.a)
        self.abtn5.setText("Inform student")
        self.abtn5.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.abtn5.setIcon(QIcon('icons/envelope'))
        self.abtn5.setFont(QFont('Arial', 14, weight=QFont.Bold))
        self.abtn5.setStyleSheet("QToolButton{padding:10px; background-color: orange; color:black; border-style: outset; border-width: 2px; border-radius: 22px; border-color: black;}" "QToolButton:hover{background-color: tomato; color:white;}")
        self.abtn5.setIconSize(QSize(150, 150))
        self.abtn5.setFixedSize(200, 200)
        self.abtn5.setToolTip("Send a notification via SMS and email")
        self.abtn5.clicked.connect(self.notfi)

        # Manage Password button h frnds
        self.abtn6 = QToolButton(self.a)
        self.abtn6.setText("Student Pass")
        self.abtn6.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.abtn6.setIcon(QIcon('icons/keycdn'))
        self.abtn6.setFont(QFont('Arial', 14, weight=QFont.Bold))
        self.abtn6.setStyleSheet("QToolButton{padding:10px; background-color: orange; color:black; border-style: outset; border-width: 2px; border-radius: 22px; border-color: black;}" "QToolButton:hover{background-color: tomato; color:white;}")
        self.abtn6.setIconSize(QSize(150, 150))
        self.abtn6.setFixedSize(200, 200)
        self.abtn6.setToolTip("Managing student password")
        self.abtn6.clicked.connect(self.manaspass)


        #Layout of buttons
        self.grid.addWidget(self.abtn1,1,1)
        self.grid.addWidget(self.abtn2,1,2)
        self.grid.addWidget(self.abtn3,2,1)
        self.grid.addWidget(self.abtn4,2,2)
        self.grid.addWidget(self.abtn5,3,1)
        self.grid.addWidget(self.abtn6,3,2)

        self.a.setLayout(self.grid)

        self.a.setWindowTitle("Attendance Tracker - Administrator Panel")
        self.a.setStyleSheet("background-color:#ebffec")
        self.a.setGeometry(100, 100, 1000, 700)
        self.a.show()

    def notice(self):
        self.anb = QDialog()
        self.layout = QFormLayout()

        self.anheader=QLabel("Enter your notice here")
        self.anheader.setStyleSheet("QLabel{font-weight:bold}")
        self.noticetxt = QTextEdit()
        self.anbtn = QPushButton("Publish Notice")
        self.anbtn.clicked.connect(self.storenotice)

        self.layout.addRow(self.anheader)
        self.layout.addRow(self.noticetxt)
        self.layout.addRow(self.anbtn)
        self.anb.setLayout(self.layout)
        self.anb.setWindowTitle("Publish Notice")
        self.anb.setGeometry(100, 100, 500, 50)
        self.anb.exec_()

    def storenotice(self):
        with open('notice.txt', 'w') as f:
            my_text = self.noticetxt.toPlainText()
            f.write(my_text)
            if my_text!=0:
                QMessageBox.information(self.a, "Info", "Operation Done Successfully", QMessageBox.Ok, QMessageBox.Ok)

    def manaspass(self):
        self.amp = QDialog()
        self.layout = QFormLayout()

        self.inrollu = QLabel("Enter Student ID:")
        self.inrollu.setStyleSheet("QLabel{font-weight:bold}")
        self.txtinrollu = QLineEdit()
        self.txtinrollu.setPlaceholderText("ex- 15EGJCS001")
        self.inpassu = QLabel("Enter Password:")
        self.inpassu.setStyleSheet("QLabel{font-weight:bold}")
        self.txtinpassu = QLineEdit()
        self.txtinpassu.setEchoMode(QLineEdit.Password)
        self.ampbtn = QPushButton("Generate password")
        self.ampbtn.clicked.connect(self.manaspassdb)

        self.layout.addRow(self.inrollu,self.txtinrollu)
        self.layout.addRow(self.inpassu,self.txtinpassu)
        self.layout.addRow(self.ampbtn)
        self.amp.setLayout(self.layout)
        self.amp.setWindowTitle("Generate Password")
        self.amp.setGeometry(100, 100, 500, 200)
        self.amp.exec_()

    def notfi(self):
        self.an = QDialog()
        self.layout = QFormLayout()

        self.header = QLabel("Enter your roll number")
        self.header.setStyleSheet("QLabel {font: 30pt Comic Sans MS;font-style:italic;text-decoration:underline;font-weight:bold;color:skyblue}")
        self.inroll = QLabel("Enter Roll N0:")
        self.inroll.setStyleSheet("QLabel{font-weight:bold}")
        self.txtinroll = QLineEdit()
        self.txtinroll.setPlaceholderText("ex- 15EGJCS001")
        self.insubmite= QPushButton("Send Email")
        self.insubmite.clicked.connect(self.informsemail)
        self.insubmits = QPushButton("Send SMS")
        self.insubmits.clicked.connect(self.informsms)

        self.layout.addRow(self.inroll, self.txtinroll)
        self.layout.addRow(self.insubmite)
        self.layout.addRow(self.insubmits)
        self.an.setLayout(self.layout)
        self.an.setWindowTitle("Send Notification")
        self.an.setGeometry(200, 300, 400, 50)
        self.an.exec_()


    def informsemail(self):

        print(self.txtinroll.text())
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('atdata.db')

        if not db.open():
            QMessageBox.critical(None, qApp.tr("connect open database"), qApp.tr("Unable to establish a DB"),
                                 QMessageBox.Cancel)

            return False

        query = QtSql.QSqlQuery()
        query.exec_("select email from student where roll='%s' " % (self.txtinroll.text()))
        row = []
        while query.next():
            row += [[query.value(index) for index in range(1)]]
            y=row[0][0]
        print(y)

        to = y
        gmail_user = ''  # hospital ka email address
        gmail_pwd = ''  # apna password

        header = 'To:' + to + '\n' + 'From:' + gmail_user + '\n' + 'Subject: Automated Mail regarding attendance of your Peer\n'
        print(header)

        msg = header + '\nThis is an automatic response regarding Attendance of your peer: ' + to + ' And we found out that its attendance is less than 60%. Kindly attend class or you will be debarded'

        try:
            smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.login(gmail_user, gmail_pwd)
            smtpObj.sendmail(gmail_user, to, msg)
            print("Sent Sucessfully sent mail")
            QMessageBox.information(self.a, "Info", "Operation Done Successfully", QMessageBox.Ok, QMessageBox.Ok)
        except SMTPException as e:
            print("Enable to send email", e)
        smtpObj.close()


        return True


    def informsms(self):

        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('atdata.db')

        if not db.open():
            QMessageBox.critical(None, qApp.tr("connect open database"), qApp.tr("Unable to establish a DB"),
                                 QMessageBox.Cancel)

            return False

        query = QtSql.QSqlQuery()
        query.exec_("select phone from student where roll='%s' " % (self.txtinroll.text()))
        row = []
        while query.next():
            row += [[query.value(index) for index in range(1)]]
            x = row[0][0]
        x='+91'+str(x)
        print(x)
        # Your Account Sid and Auth Token from twilio.com/console
        account_sid = 'AC5d36f6854a4287109d24cc0581e1f1d6436a'
        auth_token = 'b8a5bf7cf5f5beb745274b8611b5e363630d1'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body='Your peer have attendance less than 60%',
            from_='+1253203463614553',
            to=x)

        print(message.sid)

        print("Sent successfully")
        if message.sid!=0:
            QMessageBox.information(self.a, "Info", "Operation Done Successfully", QMessageBox.Ok, QMessageBox.Ok)

    def manaspassdb(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('atdata.db')

        if not db.open():
            QMessageBox.critical(None, qApp.tr("connect open database"), qApp.tr("Unable to establish a DB"),
                                 QMessageBox.Cancel)

            return False

        query = QtSql.QSqlQuery()
        sql="insert into student_pass(roll,pass)values('%s','%s')" % (self.txtinrollu.text(),self.txtinpassu.text())
        query.exec_(sql)

        if sql!=0:
            QMessageBox.information(self.a, "Info", "Operation Done Successfully", QMessageBox.Ok, QMessageBox.Ok)