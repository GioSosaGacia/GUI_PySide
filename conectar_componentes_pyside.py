'''
Conectar componentes en PySide
'''

import sys
from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget


class VentanaPricipal(QMainWindow):

    def __init__(self):
    #heredando de la clase qmainwindow para que se inicialice
        super().__init__()
        self.setWindowTitle('Signal and Slots')
        self.setFixedSize(400, 200)
        #definir 2 elemetos onlineEdit, Label
        self.etiqueta = QLabel() #qlabel recibe los datos de la linea de texto
        self.entrada_texto = QLineEdit()#permite crear texto
        #conectar el widget de entrada de texto con la etiqueta label
        #estamos conectando la señal es textChange y el slot setText
        self.entrada_texto.textChanged.connect(self.etiqueta.setText)
        #Layout permite agregar varios componentes a la ventana, puclicar los componetes
        disposicion = QVBoxLayout() #V = vertical
        disposicion.addWidget(self.entrada_texto)
        disposicion.addWidget(self.etiqueta)
        #crear un contenedor para ubicar el layout
        #QWidget es la clase padre en pyside
        contenedor = QWidget()
        contenedor.setLayout(disposicion)
        #publicamos el contenedor
        self.setCentralWidget(contenedor)


#Prueba de la aplicacion
if __name__ == '__main__':
    #creamos el objeto de aplicacion
    app = QApplication([])
    #Creamos una instancia de la clase
    ventana = VentanaPricipal()
    ventana.show()
    sys.exit(app.exec())
