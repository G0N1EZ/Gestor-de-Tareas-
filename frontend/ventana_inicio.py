from PyQt5.QtWidgets import QLabel, QFileDialog, QTextEdit, QVBoxLayout, QHBoxLayout, QPushButton, QCheckBox, QWidget, QScrollArea, QComboBox, QInputDialog, QLineEdit
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from frontend.parametros import SCREEN_WIDTH, SCREEN_HEIGHT, ORIGIN_X, ORIGIN_Y, PATH_ARCHIVOS, PATH_ESTILO_VENTANA_PRINCIPAL, WIDTH_BOTON_ENTRAR, HEIGHT_BOTON_ENTRAN, PATH_ICONO

class VentanaInicio(QWidget):
    senal_abrir_ventana_principal = pyqtSignal()
    senal_cargar_datos = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.setGeometry(ORIGIN_X, ORIGIN_Y, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.setStyleSheet(self.ventana_estilo)
        self.setWindowTitle("Gestor de Tareas")
        self.setWindowIcon(QIcon(PATH_ICONO))
        self.mensaje_inicio = QLabel("Bienvenido a tu Gestor de Tareas", self)
        self.boton_recuperado = QPushButton("Cargar Archivo de Tareas", self)
        self.mensaje_datos = QLabel(self)
        self.boton_inicio = QPushButton("Entrar", self)

        # estilo personalizado de las tags
        self.mensaje_inicio.setStyleSheet("""
        font-size: 24px;
        font-weight: bold;
        """)
        self.boton_inicio.setMinimumSize(WIDTH_BOTON_ENTRAR, HEIGHT_BOTON_ENTRAN)

        # Layout
        layout = QVBoxLayout()
        layout.addStretch()
        layout_h_superior = QHBoxLayout()
        layout_h_superior.addStretch()
        layout_h_superior.addWidget(self.mensaje_inicio)
        layout_h_superior.addStretch()
        layout.addLayout(layout_h_superior)
        layout.addStretch()
        layout_h = QHBoxLayout()
        layout_h.addWidget(self.boton_recuperado)
        layout_h.addStretch()
        layout_h.addWidget(self.mensaje_datos)
        layout_h.addStretch()
        layout.addLayout(layout_h)
        layout.addStretch()
        layout_h_final = QHBoxLayout()
        layout_h_final.addStretch()
        layout_h_final.addWidget(self.boton_inicio)
        layout_h_final.addStretch()
        layout.addLayout(layout_h_final)
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

    @property
    def ventana_estilo(self):
        with open(PATH_ESTILO_VENTANA_PRINCIPAL, "r") as archivo_estilo:
            estilo_hoja = archivo_estilo.read()
        return estilo_hoja






