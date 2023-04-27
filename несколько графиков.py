import sys
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('2 графика')

        widget1 = pg.PlotWidget()
        layout = QVBoxLayout()
        layout.addWidget(widget1)

        x1 = [1, 2, 3, 4, 5]
        y1 = [1, 3, 2, 4, 5]

        # Добавление кривой линии на первый график
        curve1 = widget1.plot(x1, y1)

        # Настройка параметров кривой линии
        curve1.setPen(pg.mkPen(color='r', width=2))

        widget2 = pg.PlotWidget()
        layout.addWidget(widget2)

        x2 = [1, 2, 3, 4, 5]
        y2 = [5, 4, 2, 3, 1]

        curve2 = widget2.plot(x2, y2)
        curve2.setPen(pg.mkPen(color='g', width=2))
        main_widget = QWidget(self)
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
