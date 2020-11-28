from sys import argv, exit
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget
from random import choice, randint


class Main(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)

    def paintEvent(self, event):
        a = randint(10, 90)
        x = randint(a, self.width() - a)
        y = randint(a, self.height() - a)
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor('Yellow'))
        qp.drawEllipse(x - a // 2, y - a // 2, a, a)
        qp.end()

    def run(self):
        self.update()


if __name__ == '__main__':
    app = QApplication(argv)
    ex = Main()
    ex.show()
    exit(app.exec())