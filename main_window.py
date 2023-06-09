from PySide6.QtWidgets import QMainWindow, QMessageBox, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Layout Config
        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)

        # Title
        self.setWindowTitle('Calculadora')

    def adjustFixedSize(self):
        # Last thing
        self.adjustSize()
        self.setFixedSize(self.width(), self.height() + 20)

    def addWidgetToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)

    def makeMsgBox(self):
        return QMessageBox(self)
