import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from components import WINDOW_ICON_PATH, setupTheme
from main_window import MainWindow
from parts import Button, ButtonsGrid, Display, Info

if __name__ == '__main__':
    app = QApplication(sys.argv) # type: ignore
    setupTheme()
    window = MainWindow()

    # Define um ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('2.0 ^ 10.0 = 124') # type: ignore
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    display.setPlaceholderText('Digite aqui')
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display) # type: ignore
    window.vLayout.addLayout(buttonsGrid)


    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
