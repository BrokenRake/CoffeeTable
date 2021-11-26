import sqlite3
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(111, 78, 55); color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(5)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("background-color:rgb(189, 149, 121); color: rgb(0, 0, 0);\n"
"\n"
"    border: 2px solid #6F4E37;\n"
"    \n"
"\n"
"\n"
"    min-width: 20ex;\n"
"\n"
"")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Button_recording = QtWidgets.QPushButton(self.centralwidget)
        self.Button_recording.setMinimumSize(QtCore.QSize(80, 20))
        self.Button_recording.setStyleSheet("background-color:rgb(189, 149, 121); color: rgb(0, 0, 0);\n"
" border: 2px solid rgb(255, 255, 255);\n"
"    border-radius: 6px;\n"
"")
        self.Button_recording.setObjectName("Button_recording")
        self.horizontalLayout.addWidget(self.Button_recording)
        self.Button_change = QtWidgets.QPushButton(self.centralwidget)
        self.Button_change.setMinimumSize(QtCore.QSize(80, 20))
        self.Button_change.setStyleSheet("background-color:rgb(189, 149, 121); color: rgb(0, 0, 0);\n"
" border: 2px solid rgb(255, 255, 255);\n"
"    border-radius: 6px;\n"
"")
        self.Button_change.setObjectName("Button_change")
        self.horizontalLayout.addWidget(self.Button_change)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Column"))
        self.Button_recording.setText(_translate("MainWindow", "Запись"))
        self.Button_change.setText(_translate("MainWindow", "Измениние"))


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(497, 348)
        Dialog.setStyleSheet("background-color: rgb(111, 78, 55); color: rgb(255, 255, 255);")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_id = QtWidgets.QLabel(Dialog)
        self.label_id.setMinimumSize(QtCore.QSize(100, 0))
        self.label_id.setObjectName("label_id")
        self.horizontalLayout_7.addWidget(self.label_id)
        self.id_edit = QtWidgets.QLineEdit(Dialog)
        self.id_edit.setObjectName("id_edit")
        self.horizontalLayout_7.addWidget(self.id_edit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMinimumSize(QtCore.QSize(100, 0))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.name_edit = QtWidgets.QLineEdit(Dialog)
        self.name_edit.setObjectName("name_edit")
        self.horizontalLayout.addWidget(self.name_edit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setMinimumSize(QtCore.QSize(100, 0))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.RoastDegree_edit = QtWidgets.QLineEdit(Dialog)
        self.RoastDegree_edit.setObjectName("RoastDegree_edit")
        self.horizontalLayout_2.addWidget(self.RoastDegree_edit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setMinimumSize(QtCore.QSize(100, 0))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.GroundOrBeans_edit = QtWidgets.QLineEdit(Dialog)
        self.GroundOrBeans_edit.setObjectName("GroundOrBeans_edit")
        self.horizontalLayout_3.addWidget(self.GroundOrBeans_edit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setMinimumSize(QtCore.QSize(100, 0))
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Description_Edit = QtWidgets.QTextEdit(Dialog)
        self.Description_Edit.setObjectName("Description_Edit")
        self.verticalLayout_4.addWidget(self.Description_Edit)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setMinimumSize(QtCore.QSize(100, 0))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.price_edit = QtWidgets.QLineEdit(Dialog)
        self.price_edit.setObjectName("price_edit")
        self.horizontalLayout_5.addWidget(self.price_edit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setMinimumSize(QtCore.QSize(100, 0))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.volume_edit = QtWidgets.QLineEdit(Dialog)
        self.volume_edit.setObjectName("volume_edit")
        self.horizontalLayout_6.addWidget(self.volume_edit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setStyleSheet("background-color:rgb(189, 149, 121); color: rgb(0, 0, 0);\n"
" border: 2px solid rgb(255, 255, 255);\n"
"    border-radius: 6px;")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.msg = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.msg.setFont(font)
        self.msg.setText("")
        self.msg.setObjectName("msg")
        self.horizontalLayout_9.addWidget(self.msg)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_id.setText(_translate("Dialog", "ID"))
        self.label.setText(_translate("Dialog", "Название сорта"))
        self.label_2.setText(_translate("Dialog", "Степень обжарки"))
        self.label_3.setText(_translate("Dialog", "Молотый/в зернах"))
        self.label_4.setText(_translate("Dialog", "Описание вкуса"))
        self.label_5.setText(_translate("Dialog", "Цена"))
        self.label_6.setText(_translate("Dialog", "Объем упаковки"))
        self.pushButton.setText(_translate("Dialog", "Изменить"))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('CoffeeTable')

        update = self.output()

        self.Button_recording.clicked.connect(self.recording)
        self.Button_change.clicked.connect(self.change)

    def output(self):
        con = sqlite3.connect('data/coffee.sqlite')
        res = con.cursor().execute("""SELECT * FROM coffee""").fetchall()
        con.close()

        self.TableTitle = ['ID', 'название сорта', 'степень обжарки,', 'молотый/в зернах',
                           'описание вкуса', 'цена', ' объем упаковки']
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(len(self.TableTitle))
        self.tableWidget.setHorizontalHeaderLabels(self.TableTitle)
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QtWidgets.QTableWidgetItem(str(elem)))

    def recording(self):
        recording = Recording()
        recording.exec_()
        update = self.output()

    def change(self):
        change = Change()
        change.exec_()
        update = self.output()


class Recording(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Recording')
        self.pushButton.setText('Добавить')

        self.id_edit.hide()
        self.label_id.hide()

        self.pushButton.clicked.connect(self.run)

    def run(self):
        VarietyName, RoastDegree, GroundOrBeans, FlavorDescription, \
        price, volume = self.name_edit.text(), self.RoastDegree_edit.text(), \
                        self.GroundOrBeans_edit.text(), self.Description_Edit.toPlainText(), \
                        self.price_edit.text(), self.volume_edit.text()

        con = sqlite3.connect('data/coffee.sqlite')
        res = con.cursor().execute("""INSERT INTO coffee(VarietyName, RoastDegree, GroundOrBeans,
                                                            FlavorDescription, price, volume)
                                    VALUES(?, ?, ?, ?, ?, ?)""", (VarietyName, RoastDegree, GroundOrBeans,
                                                                  FlavorDescription, price, volume))
        con.commit()
        con.close()
        self.msg.setText('Добавлено')


class Change(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Change')
        self.pushButton.setText('Изменить')

        self.pushButton.clicked.connect(self.run)

    def run(self):
        ID, VarietyName, RoastDegree, GroundOrBeans, FlavorDescription, \
        price, volume = self.id_edit.text(), self.name_edit.text(), self.RoastDegree_edit.text(), \
                        self.GroundOrBeans_edit.text(), self.Description_Edit.toPlainText(), \
                        self.price_edit.text(), self.volume_edit.text()

        con = sqlite3.connect('data/coffee.sqlite')
        res = con.cursor().execute("""UPDATE coffee
                                    SET VarietyName = ?,RoastDegree = ?, GroundOrBeans = ?, 
                                    FlavorDescription = ?, price = ?, volume = ?
                                    WHERE id = {}""".format(ID),
                                   (VarietyName, RoastDegree, GroundOrBeans,
                                    FlavorDescription, price, volume))
        con.commit()
        con.close()
        self.msg.setText('Изменино')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
