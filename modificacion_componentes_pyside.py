'''
Modificacion de componentes
Cada componente tiene sus propias señales
'''
import sys

from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication


class VentanaPricipal(QMainWindow):

    def __init__(self):
    #heredando de la clase qmainwindow para que se inicialice
        super().__init__()
        self.setWindowTitle('Signal and Slots')
        #Boton, con self lo convertimos a un atributo de nuestra clase
        self.boton = QPushButton('Click Here')
    #asocimos la señal de click al slot evento_click
        self.boton.clicked.connect(self.evento_click)
    #Conectar a la señal de cambio de titulo
        self.windowTitleChanged.connect(self.cambio_titulo_aplicacion)
        #Publicamos el button
        self.setCentralWidget(self.boton)


    def evento_click(self):
        #cambiar el texto del boton y titulo de la ventana
        self.boton.setText('Nuevo texto Boton ')
        self.boton.setEnabled(False)#setenabled deshabilita el boton(False), lo habilita(True)
        self.setWindowTitle('Nuevo titulo de la aplicacion')
        print('evento_click')

    def cambio_titulo_aplicacion(self,nuevo_titulo):
        print(f'Nuevo titulo de la aplicacion, {nuevo_titulo}')

#Prueba de la aplicacion
if __name__ == '__main__':
    #creamos el objeto de aplicacion
    app = QApplication([])
    #Creamos una instancia de la clase
    ventana = VentanaPricipal()
    ventana.show()
    sys.exit(app.exec())
