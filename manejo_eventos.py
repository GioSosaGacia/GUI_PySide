'''
Signals: eventos y slots: son los metodos que procesan dichos eventos
'''
import sys

from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication


class VentanaPricipal(QMainWindow):

    def __init__(self):
    #heredando de la clase qmainwindow para que se inicialice
        super().__init__()
        self.setWindowTitle('Signal and Slots')
        #Boton
        boton = QPushButton('Click Here')
    #podemos asociar varios eventos a un slot
    #Conectamos el evento checkeable(por defaul es false), queda activo el boton despues de presionarlo, permite checar el estado del mismo
        boton.setCheckable(True)
    #conectamos otro slot al evento checar
        boton.clicked.connect(self.evento_checar)
        #conectamos el evento(signal) click con el slot(evento click)
        boton.clicked.connect(self.evento_click) #clicked es la señal sin () para monitorear el click sobre el boton, connect para asociarlo al evento deseado
        #Publicamos el button
        self.setCentralWidget(boton)

    def evento_checar(self, checar):
    #en una variable local
        #print('Checado?',checar)
    #tambien se puede asigna a una variable de clase para usarlo en otros metodos con el uso de self
        self.boton_checado = checar
        print('Checado?',self.boton_checado)

        #evento click es el slot
    def evento_click(self):
        print('Has hecho click')
        #accedemos al boton del estado para ver si esta checado o no (checado)
        print('Boton checado desde el evento click', self.boton_checado)


#Prueba de la aplicacion
if __name__ == '__main__':
    #creamos el objeto de aplicacion
    app = QApplication([])
    #Creamos una instancia de la clase
    ventana = VentanaPricipal()
    ventana.show()
    sys.exit(app.exec())



