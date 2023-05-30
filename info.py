from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel

from variables import SMALL_FONT_SIZE


class Info(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f'font-size {SMALL_FONT_SIZE}p')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
