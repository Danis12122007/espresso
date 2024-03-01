import sqlite3
import PyQt5
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QWidget
import sys


class Main(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.label.setVisible(False)
        self.pushButton_4.setVisible(False)
        self.pushButton.clicked.connect(self.run_1)
        self.pushButton_2.clicked.connect(self.run_2)
        self.pushButton_3.clicked.connect(self.run_3)
        self.pushButton_4.clicked.connect(self.run_4)

    def run_1(self):
        quary = """
        SELECT * FROM ingredients
        WHERE id=1"""
        db = sqlite3.connect('coffee.sqlite')
        cursor = db.cursor()
        data = cursor.execute(quary).fetchall()
        data = data[0]
        text = str(f'Название: {data[1]};\nСтепень обжарки: {data[2]};\n{data[3]}\nОписание: {data[4]}\
        \nЦена: {data[5]}\nОбъём: {data[6]}')

        self.label.setVisible(True)
        self.pushButton_4.setVisible(True)
        self.pushButton.setVisible(False)
        self.pushButton_2.setVisible(False)
        self.pushButton_3.setVisible(False)
        self.label.setText(text)
        print(text)

    def run_2(self):
        quary = """
        SELECT * FROM ingredients
        WHERE id=2"""
        db = sqlite3.connect('coffee.sqlite')
        cursor = db.cursor()
        data = cursor.execute(quary).fetchall()
        data = data[0]
        text = str(f'Название: {data[1]};\nСтепень обжарки: {data[2]};\n{data[3]}\nОписание: {data[4]}\
                \nЦена: {data[5]}\nОбъём: {data[6]}')
        self.label.setVisible(True)
        self.pushButton_4.setVisible(True)
        self.pushButton.setVisible(False)
        self.pushButton_2.setVisible(False)
        self.pushButton_3.setVisible(False)
        self.label.setText(text)
        print(text)

    def run_3(self):
        quary = """
        SELECT * FROM ingredients
        WHERE id=3"""
        db = sqlite3.connect('coffee.sqlite')
        cursor = db.cursor()
        data = cursor.execute(quary).fetchall()
        data = data[0]
        text = str(f'Название: {data[1]};\nСтепень обжарки: {data[2]};\n{data[3]}\nОписание: {data[4]}\
                \nЦена: {data[5]}\nОбъём: {data[6]}')
        self.label.setVisible(True)
        self.pushButton_4.setVisible(True)
        self.pushButton.setVisible(False)
        self.pushButton_2.setVisible(False)
        self.pushButton_3.setVisible(False)
        self.label.setText(text)
        print(text)

    def run_4(self):
        self.label.setVisible(False)
        self.pushButton_4.setVisible(False)
        self.pushButton.setVisible(True)
        self.pushButton_2.setVisible(True)
        self.pushButton_3.setVisible(True)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
