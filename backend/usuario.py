import os
import json
from pathlib import Path


class Usuario:
    def __init__(self, nombre):
        self.nombre_usuario = nombre
        self.path = Path(__file__).parent / f"{self.nombre_usuario}.json"

    def cargar_archivo(self):
        with open(f"{self.path}", "w", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        return datos

    def guardar_archivo(self, datos):
        with open(f"{self.path}", "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)



