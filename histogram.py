# import sys
#
# import pyqtgraph as pg
# from PyQt5.QtWidgets import QApplication
# from pyqtgraph.Qt import QtCore, QtGui
#
# win = pg.GraphicsView()
# win.resize(800, 350)
# win.setWindowTitle('pyqtgraph example: Histogram')
# plt1 = win.addPlot()
#
# x = [1, 2, 3, 4, 5, 6, 7]
# y = [1, 0.2, 3, 45, 5, 6]
#
# plt1.plot(x, y, stepMode=True, fillLevel=0, brush=(0, 0, 255, 150))
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     # Отображение главного окна
#     win.show()
#     # Запуск главного цикла приложения
#     sys.exit(app.exec_())

"""
In this example we draw two different kinds of histogram.
"""

import numpy as np

import pyqtgraph as pg

win = pg.GraphicsLayoutWidget(show=True)
win.resize(800, 480)
win.setWindowTitle('pyqtgraph example: Histogram')
plt1 = win.addPlot()

## make interesting distribution of values
vals = np.hstack([np.random.normal(size=500), np.random.normal(size=260, loc=4)])

## compute standard histogram
y, x = np.histogram(vals, bins=np.linspace(-3, 8, 40))

## Using stepMode="center" causes the plot to draw two lines for each sample.
## notice that len(x) == len(y)+1
plt1.plot(x, y, stepMode="center", fillLevel=0, fillOutline=True, brush=(0, 0, 255, 150))

# draw histogram using BarGraphItem
win.nextRow()
plt3 = win.addPlot()
bgi = pg.BarGraphItem(x0=x[:-1], x1=x[1:], height=y, pen='w', brush=(0, 0, 255, 150))
plt3.addItem(bgi)

if __name__ == '__main__':
    pg.exec()
