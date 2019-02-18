from PyQt5 import QtSql,QtCore
from PyQt5.QtWidgets import *

class crud3():

    def dataattendance(self):

        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('atdata.db')

        self.view = QTableView()
        self.view.setToolTip("Change the fields")
        self.view.setWindowTitle("Table Model")

        self.dlg = QDialog()

        self.btn_add = QPushButton("Add a row")
        self.btn_add.clicked.connect(self.add_row)

        self.btn_del = QPushButton("Delete a row")
        self.btn_del.clicked.connect(self.remove_row)

        self.btn_add2 = QPushButton("Add a column")
        self.btn_add2.clicked.connect(self.add_column)

        self.btn_del2 = QPushButton("Delete a column")
        self.btn_del2.clicked.connect(self.remove_column)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.view)
        self.layout.addWidget(self.btn_add)
        self.layout.addWidget(self.btn_del)
        #self.layout.addWidget(self.btn_add2)
        self.layout.addWidget(self.btn_del2)

        self.model = QtSql.QSqlTableModel()
        self.model.setTable('attendance')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.select()
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Roll No")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Total")
        self.view.setModel(self.model)

        self.dlg.setLayout(self.layout)
        self.dlg.setWindowTitle("Attendance DataBase")
        self.dlg.setGeometry(100, 100, 1100, 600)
        self.dlg.exec_()

    def add_row(self):
        self.model.insertRows(self.model.rowCount(), 1)

    def add_column(self):
        self.model.insertColumns(self.model.columnCount(),1)

    def remove_row(self):
        self.model.removeRow(self.view.currentIndex().row())
        self.model.select()

    def remove_column(self):
        self.model.removeColumn(self.view.currentIndex().column())
        self.model.select()