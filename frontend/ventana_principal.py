from PyQt5.QtWidgets import QLabel, QTextEdit, QVBoxLayout, QHBoxLayout, QPushButton, QCheckBox, QWidget, QScrollArea, QComboBox, QInputDialog
from frontend.parametros import SCREEN_WIDTH, SCREEN_HEIGHT, ORIGIN_X, ORIGIN_Y



class CarpetaTareas(QWidget):
    def __init__(self, nombre: str):
        super().__init__()
        self.nombre = QLabel(nombre, self)
        self.cerrado = True
        self.contenido = QWidget()
        self.boton = QPushButton("Abrir Carpeta", self)
        self.boton_agregar_tareas = QPushButton("Agregar Tareas")

        # layout
        self.layout_tareas = QVBoxLayout()
        self.layout_tareas.addWidget(self.boton_agregar_tareas)
        self.contenido.setLayout(self.layout_tareas)
        layout_carpeta = QVBoxLayout()
        layout_carpeta.addWidget(self.boton)
        layout_carpeta.addWidget(self.contenido)
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

    def crear_tarea(self, nombre_tarea: str):
        nueva_tarea = QCheckBox(nombre_tarea, self.contenido)
        self.layout_tareas.addWidget(nueva_tarea)


class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(ORIGIN_X, ORIGIN_Y, SCREEN_WIDTH, SCREEN_HEIGHT)
        boton_agregar_carpeta = QPushButton("Agregar Carpeta de Tareas")
        # botones
        boton_agregar_carpeta.clicked.connect(self.crear_carpeta)

        # Layout
        self.layout_pagina = QHBoxLayout()
        self.layout_pagina.addWidget(boton_agregar_carpeta)

        # agregar cosas al layout
        self.setLayout(self.layout_pagina)

    def mostrar_ventana(self):
        self.show()

    def crear_carpeta(self):
        nombre_carpeta, ok = QInputDialog.getText(self, "Nueva carpeta", "Nombre de Carpeta")
        if ok and nombre_carpeta.strip():
            nueva_carpeta = CarpetaTareas(nombre=nombre_carpeta)
            self.layout_pagina.addWidget(nueva_carpeta)

