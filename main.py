import sys
from PyQt5.QtWidgets import QApplication
from frontend.ventana_principal import VentanaPrincipal


if __name__ == "__main__":
    def hook(type_, value, traceback):
        """Hook para capturar excepciones no manejadas"""
        print(f"Error tipo: {type_}")
        print(f"Valor: {value}")
        print(f"Traceback: {traceback}")

    sys.__excepthook__ = hook


    app = QApplication(sys.argv)

    ventana_principal = VentanaPrincipal()
    ventana_principal.mostrar_ventana()



    sys.exit(app.exec_())