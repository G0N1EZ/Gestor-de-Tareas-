import os
from PyQt5.QtCore import QObject, pyqtSignal
import json


class Sistema(QObject):
    senal_datos_cargados = pyqtSignal(dict)
    senal_envio_datos_principal = pyqtSignal(dict)
    def __init__(self):
        """el backend mantiene registro normal de todas las carpetas y tareas en el diccionario"""
        super().__init__()
        self.Usuario = None
        self.datos = {}

    def guardar_archivo(self, datos, path):
        with open(path, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

    def cargar_archivo(self, path):
        with open(path, "w", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        self.datos = datos
        self.senal_datos_cargados.emit(datos)

    def enviar_datos_principal(self):
        self.senal_envio_datos_principal.emit(self.datos)








