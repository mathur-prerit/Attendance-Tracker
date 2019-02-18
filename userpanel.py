from PyQt5 import QtSql
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class userp():
    'user panel'

    def initUI3(self):
        'user details'

        self.u=QDialog()

        self.grid=QGridLayout()

        #View attendance
        self.ubtn1 = QToolButton(self.u)
        self.ubtn1.setText("View Attendance")
        self.ubtn1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.ubtn1.setIcon(QIcon('icons/eye'))
        self.ubtn1.setStyleSheet("QToolButton{padding:10px; background-color: orange; color:black; border-style: outset; border-width: 2px; border-radius: 22px; border-color: black;}" "QToolButton:hover{background-color: tomato; color:white;}")
        self.ubtn1.setFont(QFont('Arial', 14, weight=QFont.Bold))
        self.ubtn1.setIconSize(QSize(150, 150))
        #self.ubtn1.setFixedSize(200, 200)
        self.ubtn1.setToolTip("Updating students in database")
        self.ubtn1.clicked.connect(self.myattend)

        #Update Password
        self.ubtn2 = QToolButton(self.u)
        self.ubtn2.setText("Update Password")
        self.ubtn2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.ubtn2.setIcon(QIcon('icons/key'))
        self.ubtn2.setStyleSheet("QToolButton{padding:10px; background-color: orange; color:black; border-style: outset; border-width: 2px; border-radius: 22px; border-color: black;}" "QToolButton:hover{background-color: tomato; color:white;}")
        self.ubtn2.setFont(QFont('Arial', 14, weight=QFont.Bold))
        self.ubtn2.setIconSize(QSize(150, 150))
        #self.ubtn2.setFixedSize(200, 200)
        self.ubtn2.setToolTip("Updating Password from database")
        self.ubtn2.clicked.connect(self.updatepass)

        #See Notice
        self.ubtn3 = QToolButton(self.u)
        self.ubtn3.setText("View Notice")
        self.ubtn3.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.ubtn3.setIcon(QIcon('icons/clipboard-list'))
        self.ubtn3.setStyleSheet("QToolButton{padding:10px; background-color: orange; color:black; border-style: outset; border-width: 2px; border-radius: 22px; border-color: black;}" "QToolButton:hover{background-color: tomato; color:white;}")
        self.ubtn3.setFont(QFont('Arial', 14, weight=QFont.Bold))
        self.ubtn3.setIconSize(QSize(150, 150))
        #self.ubtn3.setFixedSize(200, 200)
        self.ubtn3.setToolTip("Notice from college")
        self.ubtn3.clicked.connect(self.opennotice)

        #Layout of buttons
        self.grid.addWidget(self.ubtn1,1,0)
        self.grid.addWidget(self.ubtn2, 1, 3)
        self.grid.addWidget(self.ubtn3,1,2)
        self.u.setLayout(self.grid)

        self.u.setWindowTitle("Attendance Tracker - Student Panel")
        self.u.setStyleSheet("background-color:#ebffec")
        self.u.setGeometry(100, 100, 800, 600)
        self.u.show()

    def myattend(self):
        self.ma = QDialog()
        self.layout = QFormLayout()

        self.ma.setWindowTitle("Attendance Panel- Fill Details")
        self.mauserid = QLabel("Enter User ID:")
        self.mauserid.setStyleSheet("QLabel{font-weight:bold}")
        self.mauseridtxt = QLineEdit()
        self.mauseridtxt.setPlaceholderText("ex- 15EGJCS001")
        self.mapass = QLabel("Enter Password:")
        self.mapass.setStyleSheet("QLabel{font-weight:bold}")
        self.matxtpass = QLineEdit()
        self.mabtn = QPushButton("Submit")
        self.mabtn.clicked.connect(self.viewattend)
        self.layout.addRow(self.mauserid,self.mauseridtxt)
        self.layout.addRow(self.mapass,self.matxtpass)
        self.layout.addRow(self.mabtn)
        self.ma.setLayout(self.layout)
        self.ma.setGeometry(100, 100, 500, 50)
        self.ma.exec_()

    def viewattend(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('atdata.db')

        if not db.open():
            QMessageBox.critical(None, qApp.tr("connect open database"), qApp.tr("Unable to establish a DB"),
                                 QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()

        sql = "select pass from student_pass where roll='%s' " % (self.mauseridtxt.text())
        query.exec_(sql)
        row = []
        while query.next():
            row += [[query.value(index) for index in range(1)]]

            if row[0][0] == self.matxtpass.text():
                self.vaattend()


    def vaattend(self):

        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('atdata.db')

        if not db.open():
            QMessageBox.critical(None, qApp.tr("connect open database"), qApp.tr("Unable to establish a DB"),
                                 QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()

        sql1 = "SELECT total from attendance where roll='%s'" % (self.mauseridtxt.text())
        query.exec_(sql1)
        row = []
        while query.next():
            row += [[query.value(index) for index in range(1)]]
            tottally = row[0][0]
        print(tottally)
        x=(str(tottally))


        self.va = QDialog()
        self.layout = QFormLayout()
        self.va.setWindowTitle("Attendance Panel")
        self.vaheading = QLabel("Your Attendance")
        self.vaheader = QLabel()
        self.vaheader.setStyleSheet("background-color:white;padding:10px;border-style: outset; border-width: 2px; border-radius: 22px; border-color: black;")
        self.vaheader.setFont(QFont('Arial', 14, weight=QFont.Bold))
        self.vaheader.setText(x)
        self.layout.addRow(self.vaheading)
        self.layout.addRow(self.vaheader)
        self.va.setLayout(self.layout)
        self.va.setGeometry(100, 100, 500, 50)
        self.va.exec_()
        return True

    def opennotice(self):
        self.on1=QDialog()
        self.layout = QFormLayout()

        self.heading=QLabel("Notice Board")
        self.onheader = QLabel()
        self.heading.setAlignment(Qt.AlignCenter)
        self.onheader.setStyleSheet("background-color:white;padding:10px;border-style: outset; border-width: 2px; border-radius: 22px; border-color: black;")
        self.heading.setFont(QFont('Arial', 14, weight=QFont.Bold))
        self.on1.setWindowTitle("Notification Panel")
        self.omytext = open('notice.txt','r').read()
        self.onheader.setText(self.omytext)
        self.layout.addRow(self.heading)
        self.layout.addRow(self.onheader)
        self.on1.setLayout(self.layout)
        self.on1.setGeometry(100, 100, 500, 50)
        self.on1.exec_()

    def updatepass(self):
        self.up = QDialog()
        self.layout = QFormLayout()

        self.userid = QLabel("Enter USER ID:")
        self.userid.setStyleSheet("QLabel{font-weight:bold}")
        self.useridtxt = QLineEdit()
        self.useridtxt.setPlaceholderText("ex- 15EGJCS001")
        self.uuppasso = QLabel("Enter old Password:")
        self.uuppasso.setStyleSheet("QLabel{font-weight:bold}")
        self.uuptxtpasso = QLineEdit()
        self.upbtn = QPushButton("Update Password")
        self.uuppassn = QLabel("Enter new Password:")
        self.uuppassn.setStyleSheet("QLabel{font-weight:bold}")
        self.uuptxtpassn = QLineEdit()
        self.upbtn.clicked.connect(self.updatepassdb)

        self.layout.addRow(self.userid, self.useridtxt)
        self.layout.addRow(self.uuppasso, self.uuptxtpasso)
        self.layout.addRow(self.uuppassn, self.uuptxtpassn)
        self.layout.addRow(self.upbtn)
        self.up.setLayout(self.layout)
        self.up.setWindowTitle("Update Password Panel")
        self.up.setGeometry(100, 100, 500, 50)
        self.up.exec_()


    def updatepassdb(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('atdata.db')

        if not db.open():
            QMessageBox.critical(None, qApp.tr("connect open database"), qApp.tr("Unable to establish a DB"),
                                 QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()

        sql = "select pass from student_pass where roll='%s' " % (self.useridtxt.text())
        query.exec_(sql)
        row = []
        while query.next():
            row += [[query.value(index) for index in range(1)]]

            if row[0][0] == self.uuptxtpasso.text():
                sql1 = "update student_pass set pass='%s' where roll='%s'" %(self.uuptxtpassn.text(),self.useridtxt.text())
                query.exec_(sql1)
                print("done")
        return True