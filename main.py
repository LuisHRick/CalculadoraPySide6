import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QLabel

from main_window import MainWindow
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    # Define um ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    label1 = QLabel('Texto Válido')
    label1.setStyleSheet('font-size: 50px;')
    window.addWidgetToVLayout(label1)
    window.adjustFixedSize()

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()