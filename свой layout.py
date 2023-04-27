from PyQt5.QtCore import QSize, Qt, QRect
from PyQt5.QtWidgets import QLayout, QSizePolicy, QWidget
from PyQt5.QtWidgets import QApplication, QLabel
import sys


class VerticalLayout(QLayout):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._item_list = []

    def addItem(self, item: QWidget):
        self._item_list.append(item)

    def sizeHint(self):
        return QSize(0, sum([item.sizeHint().height() for item in self._item_list]))

    def setGeometry(self, rect):
        x = rect.x()
        y = rect.y()
        for item in self._item_list:
            height = item.sizeHint().height()
            # item.setGeometry(QRect(item.pos()))
            item.setGeometry(x, y, rect.width(), height)
            y += height
        pass

    def count(self):
        return len(self._item_list)

    def itemAt(self, index):
        if 0 <= index < len(self._item_list):
            return self._item_list[index]
        return None

    def takeAt(self, index):
        if 0 <= index < len(self._item_list):
            return self._item_list.pop(index)
        return None


app = QApplication(sys.argv)
window = QWidget()

layout = VerticalLayout()
temp = QLabel("Text 1")
temp.setGeometry(10, 10, 10, 10)
layout.addWidget(QLabel("Text 1"))
layout.addWidget(QLabel("Text 2"))
layout.addWidget(QLabel("Text 3"))
window.setLayout(layout)

window.show()
sys.exit(app.exec_())
