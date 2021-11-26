import sqlite3
import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
    

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setWindowTitle('CoffeeTable')

        update = self.output()

        self.Button_recording.clicked.connect(self.recording)
        self.Button_change.clicked.connect(self.change)

    def output(self):
        con = sqlite3.connect('coffee.sqlite')
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


class Recording(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
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

        con = sqlite3.connect('coffee.sqlite')
        res = con.cursor().execute("""INSERT INTO coffee(VarietyName, RoastDegree, GroundOrBeans,
                                                            FlavorDescription, price, volume)
                                    VALUES(?, ?, ?, ?, ?, ?)""", (VarietyName, RoastDegree, GroundOrBeans,
                                                                  FlavorDescription, price, volume))
        con.commit()
        con.close()
        self.msg.setText('Добавлено')


class Change(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.setWindowTitle('Change')
        self.pushButton.setText('Изменить')

        self.pushButton.clicked.connect(self.run)

    def run(self):
        ID, VarietyName, RoastDegree, GroundOrBeans, FlavorDescription, \
        price, volume = self.id_edit.text(), self.name_edit.text(), self.RoastDegree_edit.text(), \
                        self.GroundOrBeans_edit.text(), self.Description_Edit.toPlainText(), \
                        self.price_edit.text(), self.volume_edit.text()

        con = sqlite3.connect('coffee.sqlite')
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
