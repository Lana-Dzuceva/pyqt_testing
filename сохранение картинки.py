def f3():
    """
    сохраняем картинку с виджета
    :return:
    """
    from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog
    from PyQt5.QtGui import QPixmap


    class MyWidget(QWidget):
        def __init__(self):
            super().__init__()
            self.button = QPushButton('Save Image', self)
            self.button.clicked.connect(self.save_image)

        def save_image(self):
            # Получаем изображение виджета в QPixmap
            pixmap = self.grab()
            # Открываем диалоговое окно выбора файла
            file_path, _ = QFileDialog.getSaveFileName(self, 'Save Image', '', 'Image Files (*.png *.jpg *.bmp)')
            # Если файл был выбран, сохраняем изображение
            if file_path:
                pixmap.save(file_path)


    if __name__ == '__main__':
        app = QApplication([])
        widget = MyWidget()
        widget.show()
        app.exec_()


