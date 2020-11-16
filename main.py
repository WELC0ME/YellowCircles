import sys
from random import randint
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


class MyWidget(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter(self)
            qp.setBrush(QBrush(QColor(255, 255, 0)))
            for i in range(randint(5, 10)):
                radius = randint(5, 25)
                qp.drawEllipse(randint(60, 230), randint(110, 230), radius * 2, radius * 2)
            qp.end()
            self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
