import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import pyqtgraph as pg


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Добавление графика на главное окно
        self.plot_widget = pg.PlotWidget()
        self.setCentralWidget(self.plot_widget)

        # Создание данных для графика
        x = [1, 2, 3, 4, 5]
        y = [10, 8, 6, 4, 2]
        z = [1, 3, 5, 7, 9]

        # Создание точечной диаграммы
        self.scatter = pg.ScatterPlotItem(x=x, y=y, size=z, pen=pg.mkPen('w'), brush=pg.mkBrush(255, 255, 255, 120))
        self.plot_widget.addItem(self.scatter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
