from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit

from components import BIG_FONT_SIZE, MINIMUN_WIDTH, TEXT_MARGIN


# Display
class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        margins = [TEXT_MARGIN for _ in range(4)]
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px')
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(MINIMUN_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margins)

# Label com histórico

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel

from components import SMALL_FONT_SIZE


class Info(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f'font-size {SMALL_FONT_SIZE}p')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
