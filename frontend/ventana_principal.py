from PyQt5.QtWidgets import QLabel, QTextEdit, QVBoxLayout, QHBoxLayout, QPushButton, QCheckBox, QWidget
from parametros import SCREEN_WIDTH, SCREEN_HEIGHT, ORIGIN_X, ORIGIN_Y

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(ORIGIN_X, ORIGIN_Y, SCREEN_WIDTH, SCREEN_HEIGHT)

        # botones
        self.botones = QCheckBox("Tarea 1", self)

        # Layout
        layout = QHBoxLayout(self)

        # agregar cosas al layout
        layout.addWidget(self.botones)

        self.setLayout(layout)

    def mostrar_ventana(self):
        self.show()