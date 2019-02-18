import crud_student
from PyQt5 import QtSql
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import smtplib
from smtplib import *
from twilio.rest import Client
import datetime
import crud_attendance

class staffp(crud_student.crud,crud_attendance.crud3):
    'student panel'

    def initUI4(self):
        'staff features'

        self.s=QDialog()

        self.grid=QGridLayout()

        #Mark button h frnds
        self.sbtn1 = QToolButton(self.s)
        self.sbtn1.setText("Manage Students")
        self.sbtn1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.sbtn1.setIcon(QIcon('icons/graduation-cap-solid'))
        self.sbtn1.setStyleSheet("QToolButton{padding:10px; background-color: orange; color:black; border-style: outset; border-width: 2px; border-radius: 22px; border-color: black;}" "QToolButton:hover{background-color: tomato; color:white;}")
        self.sbtn1.setFont(QFont('Arial', 14, weight=QFont.Bold))
        self.sbtn1.setIconSize(QSize(150, 150))
        self.sbtn1.setToolTip("Managing attendance of student in database")
        self.sbtn1.clicked.connect(self.datastudent)

        # FOr updaing passowrd switch
        self.sbtn2 = QToolButton(self.s)
        self.sbtn2.setText("Update Password")
        self.sbtn2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.sbtn2.setIcon(QIcon('icons/key'))
        self.sbtn2.setStyleSheet("QToolButton{padding:10px; background-color: orange; color:black; border-style: outset; border-width: 2px; border-radius: 22px; border-color: black;}" "QToolButton:hover{background-color: tomato; color:white;}")
        self.sbtn2.setFont(QFont('Arial', 14, weight=QFont.Bold))
        self.sbtn2.setIconSize(QSize(150, 150))
        self.sbtn2.setToolTip("Updating password")
        self.sbtn2.clicked.connect(self.updatepasst)

        # See Notice
        self.sbtn3 = QToolButton(self.s)
        self.sbtn3.setText("    View Notice     ")
        self.sbtn3.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.sbtn3.setIcon(QIcon('icons/clipboard-list'))
        self.sbtn3.setStyleSheet("QToolButton{padding:10px; background-color: orange; color:black; border-style: outset; border-width: 2px; border-radius: 22px; border-color: black;}" "QToolButton:hover{background-color: tomato; color:white;}")
        self.sbtn3.setFont(QFont('Arial', 14, weight=QFont.Bold))
        self.sbtn3.setIconSize(QSize(150, 150))
        self.sbtn3.setToolTip("Notice from college")
        self.sbtn3.clicked.connect(self.opennotice1)

        # Count Attendance
        self.sbtn4 = QToolButton(self.s)
        self.sbtn4.setText("Mark Attendance")
        self.sbtn4.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.sbtn4.setIcon(QIcon('icons/user-graduate-solid'))
        self.sbtn4.setStyleSheet("QToolButton{padding:10px; background-color: orange; color:black; border-style: outset; border-width: 2px; border-radius: 22px; border-color: black;}" "QToolButton:hover{background-color: tomato; color:white;}")
        self.sbtn4.setFont(QFont('Arial', 14, weight=QFont.Bold))
        self.sbtn4.setIconSize(QSize(150, 150))
        self.sbtn4.setToolTip("Compiling attendance")
        self.sbtn4.clicked.connect(self.insertdatedb)


        # send notice (import and set reference to admin panel)
        self.sbtn5 = QToolButton(self.s)
        self.sbtn5.setText("Send Notification")
        self.sbtn5.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.sbtn5.setIcon(QIcon('icons/envelope'))
        self.sbtn5.setStyleSheet("QToolButton{padding:10px; background-color: orange; color:black; border-style: outset; border-width: 2px; border-radius: 22px; border-color: black;}" "QToolButton:hover{background-color: tomato; color:white;}")
        self.sbtn5.setFont(QFont('Arial', 14, weight=QFont.Bold))
        self.sbtn5.setIconSize(QSize(150, 150))
        self.sbtn5.setToolTip("Sending notification via mail and sms")
        self.sbtn5.clicked.connect(self.notfi)

        # view button h frnds
        self.sbtn6 = QToolButton(self.s)
        self.sbtn6.setText("View Attendance")
        self.sbtn6.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.sbtn6.setIcon(QIcon('icons/eye'))
        self.sbtn6.setStyleSheet("QToolButton{padding:10px; background-color: orange; color:black; border-style: outset; border-width: 2px; border-radius: 22px; border-color: black;}" "QToolButton:hover{background-color: tomato; color:white;}")
        self.sbtn6.setFont(QFont('Arial', 14, weight=QFont.Bold))
        self.sbtn6.setIconSize(QSize(150, 150))
        self.sbtn6.setToolTip("Managing attendance of student in database")
        self.sbtn6.clicked.connect(self.dataattendance)


        #Layout of buttons
        self.grid.addWidget(self.sbtn1, 1, 1)
        self.grid.addWidget(self.sbtn2, 1, 2)
        self.grid.addWidget(self.sbtn3, 2, 2)
        self.grid.addWidget(self.sbtn4, 2, 1)
        self.grid.addWidget(self.sbtn5, 3, 2)
        self.grid.addWidget(self.sbtn6, 3, 1)

        self.s.setLayout(self.grid)

        self.s.setWindowTitle("Attendance Tracker - Staff Panel")
        self.s.setStyleSheet("background-color:#ffc2ff")
        self.s.setGeometry(100, 100, 800, 600)
        self.s.show()

    def opennotice1(self):
        self.on2 = QDialog()
        self.layout = QFormLayout()

        self.heading1 = QLabel("Notice Board")
        self.onheader1 = QLabel()
        self.onheader1.setStyleSheet("background-color:white;padding:10px;border-style: outset; border-width: 2px; border-radius: 22px; border-color: black;")
        self.heading1.setFont(QFont('Arial', 14, weight=QFont.Bold))
        self.on2.setWindowTitle("Notification Panel")
        self.heading1.setAlignment(Qt.AlignCenter)

        self.omytext1 = open('notice.txt', 'r').read()
        self.onheader1.setText(self.omytext1)
        self.layout.addRow(self.heading1)
        self.layout.addRow(self.onheader1)
        self.on2.setLayout(self.layout)
        self.on2.setGeometry(100, 100, 500, 50)
        self.on2.exec_()


    def updatepasst(self):
        self.sp = QDialog()
        self.layout = QFormLayout()

        self.suserid = QLabel("Enter USER ID:")

        self.suserid.setStyleSheet("QLabel{font-weight:bold}")
        self.suseridtxt = QLineEdit()
        self.suseridtxt.setPlaceholderText("ex- 15EGJCS001")
        self.suppasso = QLabel("Enter old Password:")
        self.suppasso.setStyleSheet("QLabel{font-weight:bold}")
        self.suptxtpasso = QLineEdit()
        self.suptxtpasso.setEchoMode(QLineEdit.Password)
        self.spbtn = QPushButton("Update Password")
        self.suppassn = QLabel("Enter new Password:")

        self.suppassn.setStyleSheet("QLabel{font-weight:bold}")
        self.suptxtpassn = QLineEdit()
        self.suptxtpassn.setEchoMode(QLineEdit.Password)
        self.spbtn.clicked.connect(self.supdatepassdb)

        self.layout.addRow(self.suserid, self.suseridtxt)
        self.layout.addRow(self.suppasso, self.suptxtpasso)
        self.layout.addRow(self.suppassn, self.suptxtpassn)
        self.layout.addRow(self.spbtn)
        self.sp.setLayout(self.layout)
        self.sp.setWindowTitle("Update Password Panel")
        self.sp.setGeometry(100, 100, 500, 50)
        self.sp.exec_()

    def insertdatedb(self):
        self.sid = QDialog()
        self.layout = QFormLayout()

        self.sdate = QLabel("Enter Date:")
        self.sdate.setStyleSheet("QLabel{font-weight:bold}")
        self.stxtdate = QLineEdit()
        self.stxtdate.setPlaceholderText("DD-MM-YYYY")
        self.stxtdatebtn=QPushButton("Get input date")
        self.stxtdatebtn.clicked.connect(self.manualdate)
        self.sdate1=QLabel("OR")
        self.scurdate=QPushButton("Get Current Date")
        self.scurdate.clicked.connect(self.currdate)
        self.callcal=QPushButton("Open Calendar")
        self.callcal.clicked.connect(self.book_date)

        self.layout.addRow(self.sdate, self.stxtdate)
        self.layout.addRow(self.stxtdatebtn)
        self.layout.addRow(self.sdate1)
        self.layout.addRow(self.scurdate)
        self.layout.addRow(self.callcal)
        self.sid.setLayout(self.layout)
        self.sid.setWindowTitle("Attendance Marking Panel")
        self.sid.setGeometry(100, 100, 500, 50)
        self.sid.exec_()


    def manualdate(self):
        if (self.stxtdate.text()==""):
            QMessageBox.warning(self.s, "Warning", "Invalid Input", QMessageBox.Ok, QMessageBox.Ok)

        else:
            print(self.stxtdate.text())
            db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName('atdata.db')

            if not db.open():
                QMessageBox.critical(None, qApp.tr("connect open database"), qApp.tr("Unable to establish a DB"),
                                 QMessageBox.Cancel)

                return False

            query = QtSql.QSqlQuery()
            sql = "alter table attendance add COLUMN '%s' INTEGER NOT NULL DEFAULT 0" % (self.stxtdate.text())
            query.exec_(sql)
            print("done")
            return True


        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Continue")
        msg.setInformativeText("Date is added in DB")
        msg.setWindowTitle("Prompt to Database")
        #msg.setDetailedText("The details are as follows:")
        msg.buttonClicked.connect(self.dataattendance)
        msg.show()
        msg.exec_()


    def currdate(self):
        today = datetime.date.today().strftime("%d-%m-%Y")
        print(today)

        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('atdata.db')

        if not db.open():
            QMessageBox.critical(None, qApp.tr("connect open database"), qApp.tr("Unable to establish a DB"),
                                 QMessageBox.Cancel)

            return False

        query = QtSql.QSqlQuery()
        sql = "alter table attendance add COLUMN '%s' INTEGER NOT NULL DEFAULT 0" % (today)
        query.exec_(sql)
        print("done")

        msg2 = QMessageBox()
        msg2.setIcon(QMessageBox.Information)
        msg2.setText("Continue")
        msg2.setInformativeText("Date is added in DB")
        msg2.setWindowTitle("Prompt to Database")
        # msg2.setDetailedText("The details are as follows:")
        msg2.buttonClicked.connect(self.dataattendance)
        msg2.show()
        msg2.exec_()

        return True


    def book_date(self):
        self.c = QDialog()
        cal = QCalendarWidget(self.c)
        cal.setGridVisible(True)
        cal.move(20, 20)
        cal.clicked[QDate].connect(self.showDate)

        self.c.setGeometry(100, 100, 450, 400)
        self.c.setWindowTitle('Calendar')
        self.c.exec_()

    def showDate(self, date):
        self.datestr = date.toString()
        print(self.datestr)

    def supdatepassdb(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('atdata.db')

        if not db.open():
            QMessageBox.critical(None, qApp.tr("connect open database"), qApp.tr("Unable to establish a DB"),
                                 QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()

        sql = "select spassword from staff where semail='%s' " % (self.suseridtxt.text())
        query.exec_(sql)
        row = []
        while query.next():
            row += [[query.value(index) for index in range(1)]]

            if row[0][0] == self.suptxtpasso.text():
                sql1 = "update student set spassword='%s' where semail='%s'" % (self.suptxtpassn.text(), self.suseridtxt.text())
                query.exec_(sql1)
                print("done")
        return True


    def notfi(self):
        self.sn = QDialog()
        self.layout = QFormLayout()

        self.header = QLabel("Enter your roll number")
        self.header.setStyleSheet("QLabel {font: 30pt Comic Sans MS;font-style:italic;text-decoration:underline;font-weight:bold;color:skyblue}")
        self.inroll = QLabel("Enter Roll N0:")
        self.inroll.setStyleSheet("QLabel{font-weight:bold}")
        self.txtinroll = QLineEdit()
        self.insubmite= QPushButton("Send Email")
        self.insubmite.clicked.connect(self.informsemail1)
        self.insubmits = QPushButton("Send SMS")
        self.insubmits.clicked.connect(self.informsms1)

        self.layout.addRow(self.inroll, self.txtinroll)
        self.layout.addRow(self.insubmite,self.insubmits)
        self.sn.setLayout(self.layout)
        self.sn.setGeometry(200, 300, 400, 50)
        self.sn.exec_()



    def informsemail1(self):

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
        gmail_user = 'abcd@gmail.com'  # email address
        gmail_pwd = '1234'  # your password

        header = 'To:' + to + '\n' + 'From:' + gmail_user + '\n' + 'Subject: aUTOMATED Mail regarding attendance of your Peer\n'
        print(header)

        msg = header + '\nThis is an automatic response regarding Attendance of your peer: ' + to + ' And we found out that its attendance is less than 60%. Kindly attend class or you will be debarded'

        try:
            smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.login(gmail_user, gmail_pwd)
            smtpObj.sendmail(gmail_user, to, msg)
            print("Sent Sucessfully sent mail")
        except SMTPException as e:
            print("Enable to send email", e)
        smtpObj.close()

        return True
    def informsms1(self):

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
        account_sid = '1111' # your twilio accound
        auth_token = '111111' #your twilio token
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body='Your peer have attendance less than 60%',
            from_='+12532014435',
            to=x)

        print(message.sid)

        print("Sent successfully")

