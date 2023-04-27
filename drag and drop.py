# 1. Включить поддержку Drag and Drop в родительском виджете:
self.setAcceptDrops(True)


# 2. Определить метод dragEnterEvent() для обработки события начала перетаскивания:
def dragEnterEvent(self, event):
    event.accept()

# 3. Определить метод dragMoveEvent() для обработки события движения объекта во время перетаскивания:
def dragMoveEvent(self, event):
    event.accept()


# 4. Определить метод dropEvent() для обработки события окончания перетаскивания:
def dropEvent(self, event):
    mimeData = event.mimeData()
    if mimeData.hasText():
        # Обработка перетаскивания текста
        event.accept()
    elif mimeData.hasUrls():
        # Обработка перетаскивания файлов
        event.accept()
    else:
        event.ignore()


# 5. Определить метод mousePressEvent() для начала перетаскивания:
def mousePressEvent(self, event):
    if event.button() == Qt.LeftButton:
        drag = QDrag(self)
        mimeData = QMimeData()
        mimeData.setText("Перетаскиваемый текст")
        drag.setMimeData(mimeData)
        drag.exec_()
