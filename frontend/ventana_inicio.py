from PyQt5.QtWidgets import QLabel, QTextEdit, QVBoxLayout, QHBoxLayout, QPushButton, QCheckBox, QWidget, QScrollArea, QComboBox, QInputDialog, QLineEdit
from PyQt5.QtCore import pyqtSignal
from frontend.parametros import SCREEN_WIDTH, SCREEN_HEIGHT, ORIGIN_X, ORIGIN_Y

class VentanaInicio(QWidget):
    senal_crear_verificar_usuario = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setGeometry(ORIGIN_X, ORIGIN_Y, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.mensaje_inicio = QLabel("Bienvenido a tu Gestor de Tareas", self)
        self.etiqueta_nombre = QLineEdit("Introduce tu nombre de usuario", self)
        self.boton_inicio = QPushButton("Entrar", self)

        # Layout
        layout = QVBoxLayout()
        layout.addStretch()
        layout.addWidget(self.mensaje_inicio)
        layout.addStretch()
        layout.addStretch()
        layout.addWidget(self.etiqueta_nombre)
        layout.addWidget(self.boton_inicio)
        layout.addStretch()
        self.setLayout(layout)

        # conexion
        self.boton_inicio.clicked.connect(self.introducir_nombre())

    def introducir_nombre(self):
        nombre_usuario = self.etiqueta_nombre.text()
        if nombre_usuario != "Introduce tu nombre de usuario":
            self.senal_crear_verificar_usuario.emit(nombre_usuario)



