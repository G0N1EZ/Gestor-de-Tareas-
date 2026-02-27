from PyQt5.QtWidgets import QLabel, QFileDialog, QTextEdit, QVBoxLayout, QHBoxLayout, QPushButton, QCheckBox, QWidget, QScrollArea, QComboBox, QInputDialog, QLineEdit
from PyQt5.QtCore import pyqtSignal
from frontend.parametros import SCREEN_WIDTH, SCREEN_HEIGHT, ORIGIN_X, ORIGIN_Y, PATH_ARCHIVOS

class VentanaInicio(QWidget):
    senal_abrir_ventana_principal = pyqtSignal()
    senal_cargar_datos = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.setGeometry(ORIGIN_X, ORIGIN_Y, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.mensaje_inicio = QLabel("Bienvenido a tu Gestor de Tareas", self)
        self.boton_recuperado = QPushButton("Cargar Archivo de Tareas", self)
        self.mensaje_datos = QLabel(self)
        self.boton_inicio = QPushButton("Entrar", self)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.mensaje_inicio)
        layout.addStretch()
        layout.addStretch()
        layout_h = QHBoxLayout()
        layout_h.addWidget(self.boton_recuperado)
        layout_h.addWidget(self.mensaje_datos)
        layout.addLayout(layout_h)
        layout.addStretch()
        layout.addWidget(self.boton_inicio)
        layout.addStretch()

        self.setLayout(layout)


        #etiqueta de datos
        self.mensaje_datos.setVisible(False)

        # conexion
        self.boton_recuperado.clicked.connect(self.datos_recuperados)
        self.boton_inicio.clicked.connect(self.iniciar_sesion)

    def datos_recuperados(self):
        ruta_archivo, _ = QFileDialog.getOpenFileName(self, "Cargar Archivo de Yareas", PATH_ARCHIVOS)
        if ruta_archivo[-5:] == ".json":
            self.senal_cargar_datos.emit(ruta_archivo)

    def carga_json(self, datos):
        if datos != {}:
            self.mensaje_datos.setText("Las Tareas del Usuario fueron Recuperadas")
            self.mensaje_datos.setVisible(True)
        else:
            self.mensaje_datos.setText("No se pudieron cargar datos, selecciona nuevo archivo o entra para nueva sesion automatica")
            self.mensaje_datos.setVisible(True)

    def iniciar_sesion(self):
        self.hide()
        self.senal_abrir_ventana_principal.emit()






