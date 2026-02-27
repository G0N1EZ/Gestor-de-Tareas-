from PyQt5.QtWidgets import QLabel, QMessageBox, QFileDialog, QTextEdit, QVBoxLayout, QHBoxLayout, QPushButton, QCheckBox, QWidget, QScrollArea, QComboBox, QInputDialog
from frontend.parametros import SCREEN_WIDTH, SCREEN_HEIGHT, ORIGIN_X, ORIGIN_Y, PATH_ARCHIVOS
from PyQt5.QtCore import pyqtSignal



class CarpetaTareas(QWidget):
    def __init__(self, nombre: str, lista_tareas=None):
        super().__init__()
        self.tareas = []
        self.nombre = QLabel(nombre, self)
        self.contenido = QWidget()
        self.boton = QPushButton("Abrir Carpeta", self)
        self.boton_agregar_tareas = QPushButton("Agregar Tareas")

        # layout
        self.layout_tareas = QVBoxLayout()
        self.layout_tareas.addWidget(self.boton)
        self.layout_tareas.addWidget(self.boton_agregar_tareas)
        self.contenido.setLayout(self.layout_tareas)
        layout_carpeta = QVBoxLayout()
        layout_carpeta.addWidget(self.nombre)
        layout_carpeta.addWidget(self.boton)
        layout_carpeta.addWidget(self.contenido)
        self.setLayout(layout_carpeta)

        #coneccion de botones
        self.boton.clicked.connect(self.mostrar_cerrar_carpeta)
        self.boton_agregar_tareas.clicked.connect(self.nombre_tarea)

        self.contenido.setVisible(False)

    def mostrar_cerrar_carpeta(self):
        if not self.contenido.isVisible():
            self.boton.setText("Cerrar Carpeta")
            self.contenido.setVisible(True)
        else:
            self.boton.setText("Abrir Carpeta")
            self.contenido.setVisible(False)

    def nombre_tarea(self):
        nombre_tarea, ok = QInputDialog.getText(self, "Nueva tarea", "Nombre de Tarea")
        if ok and nombre_tarea.strip():
            self.crear_tarea(nombre_tarea=nombre_tarea)

    def crear_tarea(self, nombre_tarea: str):
        nueva_tarea = QCheckBox(nombre_tarea, self.contenido)
        self.layout_tareas.addWidget(nueva_tarea)
        self.tareas.append(nueva_tarea)


class VentanaPrincipal(QWidget):
    senal_volver_inicial = pyqtSignal()
    senal_guardad_estado = pyqtSignal(dict, str)
    def __init__(self):
        super().__init__()
        self.sesion_actual = {}
        self.setGeometry(ORIGIN_X, ORIGIN_Y, SCREEN_WIDTH, SCREEN_HEIGHT)
        boton_agregar_carpeta = QPushButton("Agregar Carpeta de Tareas")
        boton_guardado = QPushButton("Guardar Seción")
        boton_atras = QPushButton("Terminar Seción")

        # botones
        boton_agregar_carpeta.clicked.connect(self.crear_carpeta)
        boton_guardado.clicked.connect(self.guardar_estado)
        boton_atras.clicked.connect(self.volver_ventana_inicial)

        # Layout
        self.layout_pagina = QHBoxLayout()
        self.layout_superior = QVBoxLayout()
        self.layout_inferior = QHBoxLayout()

        self.layout_inferior.addWidget(boton_atras)
        self.layout_pagina.addWidget(boton_agregar_carpeta)
        self.layout_superior.addWidget(boton_guardado)
        self.layout_superior.addLayout(self.layout_pagina)
        self.layout_superior.addLayout(self.layout_inferior)

        # agregar cosas al layout
        self.setLayout(self.layout_superior)

    def crear_carpeta(self):
        nombre_carpeta, ok = QInputDialog.getText(self, "Nueva carpeta", "Nombre de Carpeta")
        if ok and nombre_carpeta.strip():
            nueva_carpeta = CarpetaTareas(nombre=nombre_carpeta)
            self.layout_pagina.addWidget(nueva_carpeta)
            self.sesion_actual[nombre_carpeta] = nueva_carpeta.tareas

    def mostrar_ventana(self, datos: dict):
        for carpeta, tareas in datos.items():
            carpeta_recuperada = CarpetaTareas(carpeta, tareas)
            for tarea in tareas:
                tarea_recuperada = QCheckBox(tarea[0], carpeta_recuperada.contenido)
                if tarea[1]:
                    tarea_recuperada.setChecked(True)
                carpeta_recuperada.layout_tareas.addWidget(tarea_recuperada)
            self.layout_pagina.addWidget(carpeta_recuperada)
            self.sesion_actual[carpeta] = tareas
        self.show()

    def guardar_estado(self):
        sesion_guardada = {}
        for carpeta, lista_objetos in self.sesion_actual.items():
            lista_tareas_guardadas = []
            for objeto_tarea in lista_objetos:
                nombre_tarea = objeto_tarea.text()
                estado_tarea = objeto_tarea.isChecked()
                lista_tareas_guardadas.append((nombre_tarea, estado_tarea))
            sesion_guardada[carpeta] = lista_tareas_guardadas

        path_archivo, _ = QFileDialog.getSaveFileName(self, "Guardar Estado Actual", PATH_ARCHIVOS, "JSON (*.json)")
        if path_archivo:
            if not path_archivo.endswith(".json"):
                path_archivo += ".json"
            self.senal_guardad_estado.emit(sesion_guardada, path_archivo)
            QMessageBox.information(self, "Notificación", "Guardado Exitoso")

    def volver_ventana_inicial(self):
        respuesta = QMessageBox.question(self, "Alerta", "Quiere Guardar antes de Volver, sino los cambios se perderán", QMessageBox.Yes | QMessageBox.No)
        if respuesta == QMessageBox.Yes:
            self.guardar_estado()

        self.sesion_actual = {}
        self.hide()
        self.senal_volver_inicial.emit()













