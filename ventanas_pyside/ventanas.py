'''
Esta creacion de la ventana es aparte de la ventana principal
Una ventana de dialogo bloquea la ventana principal y una ventana no bloquea la ventana principal
'''
from random import randint
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit


#Para crear nuevas ventanas es creando ottra clase e instanciarla usando cualquier clase de pYsIDE que sea un componente
#y con ello crear nuevos objetos de tipo ventana
class NuevaVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Nueva Ventana')
        #saber si creo una nueva instancia, agregamos una etiqueta y mostramos un numero aleatorio
        layout = QVBoxLayout()
        self.etiqueta = QLabel(f'Nueva ventana: {randint(0,100)}') #randint -> genera un numero aleatorio con un rango definido se debe importar
        layout.addWidget(self.etiqueta)
        #publicamos el layout
        self.setLayout(layout)


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        #1. con este codigo se crea y cierra una nueva ventana
        #self.nueva_ventana = None
        #2. Para crear una sola instancia sin eliminar y crear una cada vez que se cierre la ventana
        self.nueva_ventana = NuevaVentana()
        self.setWindowTitle('Ventanas')
        self.boton = QPushButton('Mostrar/Ocultar nueva ventana')
        self.boton.clicked.connect(self.mostrar_nueva_ventana)
#Conexion entre ventanas
        #definimos una entrada de texto
        self.entrada_texto = QLineEdit()
        self.entrada_texto.textChanged.connect(self.nueva_ventana.etiqueta.setText)
        #Creamos el layout para poder publicar la entra de texto
        layout = QVBoxLayout()
        layout.addWidget(self.boton)
        layout.addWidget(self.entrada_texto)
        #creamos el contenedor para poder publicar el layout
        contenedor = QWidget()
        #publicamos el layout en el contenedor
        contenedor.setLayout(layout)
        #publicamos el boton
        self.setCentralWidget(contenedor)

    def mostrar_nueva_ventana(self,estado):
        #con este codigo se crea la ventana y solo la muestra y la esconde pero no crea una nueva instancia como el el siguiente bloque if
        #2. Para crear una sola instancia sin eliminar y crear una cada vez que se cierre la ventana
        if self.nueva_ventana.isVisible():
            self.nueva_ventana.hide()
        else:
            self.nueva_ventana.show()
'''
        #1. con este codigo se crea y cierra una nueva ventana
        #evitar que se cree una nueva ventana al presionar mostrar nueva ventana
        #tambien creamos una variable self.nueva_ventana = None en la ventana principal
        if self.nueva_ventana is None:
            #si no usamos self solo mostrar la ventana al hacer click y se quitara
            #usando self -> lo hacemos una referencia de la clase vetana principal
            self.nueva_ventana = NuevaVentana()
            self.nueva_ventana.show()
        else:
            #con esto garantizamos que se cierre la ventana
            self.nueva_ventana.close()
            #se oculta con None ya queno apunta a ninguna referencia
            self.nueva_ventana = None

'''

if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
