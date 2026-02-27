import sys
from PyQt5.QtWidgets import QApplication
from backend.sistema import Sistema
from frontend.ventana_principal import VentanaPrincipal
from frontend.ventana_inicio import VentanaInicio


if __name__ == "__main__":
    def hook(type_, value, traceback):
        """Hook para capturar excepciones no manejadas"""
        print(f"Error tipo: {type_}")
        print(f"Valor: {value}")
        print(f"Traceback: {traceback}")

    sys.__excepthook__ = hook


    app = QApplication(sys.argv)

    sistema = Sistema()
    ventana_inicio = VentanaInicio()
    ventana_principal = VentanaPrincipal()

    ventana_principal.senal_guardad_estado.connect(sistema.guardar_archivo)
    ventana_inicio.senal_abrir_ventana_principal.connect(ventana_principal.show)
    ventana_inicio.senal_cargar_datos.connect(sistema.cargar_archivo)
    sistema.senal_datos_cargados.connect(ventana_inicio.carga_json)
    ventana_inicio.senal_abrir_ventana_principal.connect(sistema.enviar_datos_principal)
    sistema.senal_envio_datos_principal.connect(ventana_principal.mostrar_ventana)

    ventana_inicio.show()



    sys.exit(app.exec_())