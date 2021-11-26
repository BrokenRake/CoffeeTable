import sqlite3
import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
    

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setWindowTitle('CoffeeTable')

        con = sqlite3.connect('coffee.sqlite')
        res = con.cursor().execute("""SELECT * FROM coffee""").fetchall()

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())