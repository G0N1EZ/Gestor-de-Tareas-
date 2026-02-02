from PyQt5.QtWidgets import QLabel, QTextEdit, QVBoxLayout, QHBoxLayout, QPushButton, QCheckBox, QWidget, QScrollArea, QComboBox
from parametros import SCREEN_WIDTH, SCREEN_HEIGHT, ORIGIN_X, ORIGIN_Y



class CarpetaTareas(QWidget):
    def __init__(self):
        self.nombre = QLabel(self)
        self.cerrado = True
        self.contenido = QWidget()
        self.boton = QPushButton("Abrir Carpeta", self)
        self.boton_agregar_tareas = QPushButton("Agregar Tareas")

        # layout
        layout_tareas = QVBoxLayout()
        layout_tareas.addItem(self.boton_agregar_tareas)
        self.contenido.setLayout(QVBoxLayout())
        layout_carpeta = QVBoxLayout()
        layout_carpeta.addItem(self.boton)
        layout_carpeta.addItem(self.contenido)
        self.setLayout(layout_carpeta)

        self.boton.clicked.connect(self.mostrar_carpeta)
        self.contenido.setVisible(False)

    def mostrar_carpeta(self):
        if self.cerrado is True:
            self.contenido.setVisible(True)
            self.cerrado = False

    def cerrar_carpeta(self):
        if self.cerrado is False:
            self.contenido.setVisible(False)
            self.cerrado = False

    def crear_carpeta(self, nombre_carpeta: str):
        self.nombre.setText(nombre_carpeta)

    def crear_tarea(self, nombre_tarea:str):
        nueva_tarea = QCheckBox(nombre_tarea)






class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(ORIGIN_X, ORIGIN_Y, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.boton = QPushButton("Agregar Carpeta de Tareas", self)
        # botones

        # Layout
        layout = QHBoxLayout(self)

        # agregar cosas al layout
        layout.addWidget(self.botones)

        self.setLayout(layout)

    def mostrar_ventana(self):
        self.show()