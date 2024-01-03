from PyQt5.QtWidgets import QWidget, QVBoxLayout
from kartu_rumah_sakit import KartuRumahSakit

class ParentWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.kartu_rs = KartuRumahSakit()
        self.kartu_rs.setupUi()

        layout = QVBoxLayout(self)
        layout.addWidget(self.kartu_rs)