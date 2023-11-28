import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem


class Coffee(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect("coffee.sqlite")
        self.setWindowTitle('таблица кофе')

        self.button.clicked.connect(self.table)

    def table(self):
        cur = self.con.cursor()
        result = cur.execute('SELECT * FROM coffees').fetchall()
        self.coffee.setRowCount(len(result))
        self.coffee.setColumnCount(len(result[0]))

        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.coffee.setItem(i, j, QTableWidgetItem(str(val)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex2 = Coffee()
    ex2.show()
    sys.exit(app.exec_())
