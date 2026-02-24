import os
from PyQt5.QtCore import QObject, pyqtSignal
from backend.usuario import Usuario
from pathlib import Path


class Sistema(QObject):
    senal_inicio_usuario = pyqtSignal(dict)
    senal_envio_datos = pyqtSignal(dict)
    def __init__(self):
        """el backend mantiene registro normal de todas las carpetas y tareas en el diccionario"""
        super().__init__()
        self.Usuario = None
        self.datos = {}

    @property
    def directorio_archivos(self):
        lista_archivos = os.listdir(str(Path(__file__).parent))
        return lista_archivos

    def buscar_crear_usuario(self, nombre_usuario):
        if nombre_usuario + ".json" in self.directorio_archivos:
            self.usuario = Usuario(nombre_usuario)
            datos = self.usuario.cargar_archivo()
        else:
            self.usuario = Usuario(nombre_usuario)
            datos = {}
        self.senal_inicio_usuario.emit(datos)

    def envio_datos(self):
        self.senal_envio_datos.emit(self.datos)

    def guardar_estado(self, datos):
        self.datos = datos
        self.usuario.guardar_archivo(self.datos)





