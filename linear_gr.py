import sys
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Линейный график')

        # Создание виджета pyqtgraph и добавление его в основное окно
        widget = pg.PlotWidget()
        self.setCentralWidget(widget)

        # Создание набора данных для построения графика
        x = [1, 2, 3, 4, 5]
        y = [1, 3, 2, 4, 5]

        # Добавление кривой линии на график
        curve = widget.plot(x, y)

        # Настройка параметров кривой линии
        curve.setPen(pg.mkPen(color='r', width=2))

        # Отображение окна
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())