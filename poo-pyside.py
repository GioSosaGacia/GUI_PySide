import sys

from PySide6.QtWidgets import QMainWindow, QApplication


class VentanaPySide():
    def __init__(self):
        self.ventana = QMainWindow()
        self.ventana.setWindowTitle('POO con PySide')
        self.ventana.resize(600, 400)



if __name__ == '__main__':
    #necesitamos un objeto de esta clase para procesar los eventos de la aplicacion
    #podemos recivir argumentos desde la linesa de comandos con sys.argv dentro de () sin los []
    app = QApplication([])#si no vamos a recibir arg pasamos una lista vacia[]
    #creamos un objeto de tipo ventana
    ventana1 = VentanaPySide()#VentanaPySide no contiene el metodo show
    #el objeto creado con ventana pyside lo ligamos a qmain para mostrar la ventana y usar el evento show() de qmain
    ventana1.ventana.show()
    #ejecutamos la ventana, dentro de exit para que se termine de ejecutar la aplicacion
    sys.exit(app.exec())
