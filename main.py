from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QGridLayout
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor
from PyQt5.QtCore import Qt
from PyQt5 import uic
from random import randint


class Test(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)

        self.pushButton.clicked.connect(self.circle)

        self.label = QLabel()
        canvas = QPixmap(550, 550)
        self.label.setPixmap(canvas)

        layout = QGridLayout(self.centralwidget)
        layout.addWidget(self.pushButton, 0, 0, alignment=Qt.AlignCenter)
        layout.addWidget(self.label, 1, 0)

    def circle(self):
        x, y = [randint(10, 450) for i in range(2)]
        w, h = [randint(10, 100) for i in range(2)]
        # создаем экземпляр QPainter, передавая холст (self.label.pixmap())
        painter = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor(255, 255, 0))
        painter.setPen(pen)
        painter.drawEllipse(x, y, w, h)
        painter.end()
        self.update()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    w = Test()
    w.show()
    sys.exit(app.exec_())
