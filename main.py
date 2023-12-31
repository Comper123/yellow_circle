from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.InitUI()
        self.draw = False
    
    def InitUI(self):
        self.button.clicked.connect(self.draw_circle)
        
    def draw_circle(self):
        self.draw = True
        self.update()

    def paintEvent(self, event):
        if self.draw:
            # генерируем размер нужного нам круга
            width = randint(20, 480)
            # Генерируем случайные координаты круга
            x, y = randint(0, 500 - width), randint(0, 500 - width)
            self.painter = QPainter(self)
            self.painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
            self.painter.drawEllipse(x, y, width, width)
            self.painter.end()
            self.draw = False
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MyWidget()
    mw.show()
    sys.exit(app.exec())