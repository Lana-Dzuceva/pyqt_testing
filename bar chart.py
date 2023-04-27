import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Добавление графика на главное окно
        self.plot_widget = pg.PlotWidget()
        self.setCentralWidget(self.plot_widget)

        # Создание данных для графика
        x = [1, 2, 3, 4, 5]
        y = [10, 8, 6, 4, 2]

        # Создание столбчатой диаграммы
        self.bar = pg.BarGraphItem(x=x, height=y, width=0.5, brush='r')
        self.plot_widget.addItem(self.bar)


if __name__ == '__main__':
    # Создание приложения и главного окна
    app = QApplication(sys.argv)
    window = MainWindow()

    # Отображение главного окна
    window.show()

    # Запуск главного цикла приложения
    sys.exit(app.exec_())
