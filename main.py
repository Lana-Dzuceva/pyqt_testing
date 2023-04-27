from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea, QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow)
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, uic
import sys
import pyqtgraph as pg


def get_list_graphs():
    # linear1
    # wrapper1 = QWidget()
    widget1 = pg.PlotWidget()
    x1 = [1, 2, 3, 4, 5]
    y1 = [1, 3, 2, 4, 5]
    curve1 = widget1.plot(x1, y1)
    # print(curve1 == widget1.getPlotItem())
    curve1.setPen(pg.mkPen(color='r', width=2))

    # linear2
    # wrapper2 = QWidget()
    widget2 = pg.PlotWidget()
    x2 = [1, 2, 3, 4, 5]
    y2 = [5, 4, 2, 3, 1]
    curve2 = widget2.plot(x2, y2)
    curve2.setPen(pg.mkPen(color='g', width=2))

    # bar chart
    # wrapper3 = QWidget()
    widget3 = pg.PlotWidget()
    x3 = [1, 2, 3, 4, 5]
    y3 = [10, 8, 6, 4, 2]
    bar = pg.BarGraphItem(x=x3, height=y3, width=0.9, brush='r')
    widget3.addItem(bar)
    return [widget1, widget2, widget3]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        graphs = get_list_graphs()
        w = QtWidgets.QWidget()
        self.scroll = QScrollArea(w)  # Scroll Area which contains the widgets, set as the centralWidget
        self.widget = QWidget()  # Widget that contains the collection of Vertical Box
        self.vbox = QVBoxLayout()  # The Vertical Box that contains the Horizontal Boxes of  labels and buttons

        for gr in graphs:
            gr.setMaximumWidth(150)
            gr.setMaximumHeight(150)
            # wrapper = QWidget()
            # wrapper.children().append(gr)
            # wrapper.setMinimumSize(150, 150)
            # wrapper.setLayout(QVBoxLayout)
            # wrapper.layout().addWidget(gr)
            self.vbox.addWidget(gr)
        for i in range(1, 20):
            object = QLabel("TextLabel")
            object.setStyleSheet("background-color: red;")
            object.setMaximumWidth(150)
            object.setMinimumHeight(150)
            self.vbox.addWidget(object)

        self.widget.setLayout(self.vbox)

        # Scroll Area Properties
        self.scroll.setStyleSheet("background-color: yellow;")
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)
        self.scroll.setGeometry(0, 0, 200, 900)
        self.setGeometry(600, 100, 1000, 900)
        self.setWindowTitle('Что-то смутное')
        self.setCentralWidget(w)
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())
