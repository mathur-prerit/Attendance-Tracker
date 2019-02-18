from PyQt5 import QtSql, QtCore
from PyQt5.QtWidgets import *


class crud2():

    def datastaff(self):
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('atdata.db')

        self.view = QTableView()
        self.view.setToolTip("Change the fields")
        self.view.setWindowTitle("Table Model")

        self.dlg = QDialog()

        self.btn_add = QPushButton("Add a staff")
        self.btn_add.clicked.connect(self.add_row)

        self.btn_del = QPushButton("Delete a staff")
        self.btn_del.clicked.connect(self.remove_row)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.view)
        self.layout.addWidget(self.btn_add)
        self.layout.addWidget(self.btn_del)

        self.model = QtSql.QSqlTableModel()
        self.model.setTable('staff')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.select()
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Teacher ID")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Name")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Email")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Mobile")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Department")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Password")
        self.view.setModel(self.model)

        self.dlg.setLayout(self.layout)
        self.dlg.setWindowTitle("Staff Database")
        self.dlg.setGeometry(100, 100, 1100, 600)
        self.dlg.exec_()

    def add_row(self):
        self.model.insertRows(self.model.rowCount(), 1)

    def remove_row(self):
        self.model.removeRow(self.view.currentIndex().row())
        self.model.select()