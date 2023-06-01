import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from components import WINDOW_ICON_PATH, setupTheme
from display import Display, Info
from main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # Define um ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('2.0 ^ 10.0 = 1024')
    window.addToVLayout(info)

    # Display
    display = Display()
    display.setPlaceholderText('Digite aqui')
    window.addToVLayout(display)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
