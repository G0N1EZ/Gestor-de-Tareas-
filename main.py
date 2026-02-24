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

    ventana_inicio.senal_crear_verificar_usuario.connect(sistema.buscar_crear_usuario)
    sistema.senal_inicio_usuario.connect(ventana_inicio.datos_recuperados)
    ventana_inicio.senal_abrir_ventana.connect(sistema.envio_datos)
    sistema.senal_envio_datos.connect(ventana_principal.mostrar_ventana)
    ventana_principal.senal_guardad_estado.connect(sistema.guardar_estado)

    ventana_inicio.show()



    sys.exit(app.exec_())