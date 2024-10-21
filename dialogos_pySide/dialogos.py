'''
Dialogos: es una ventana que permite interactuar con el usuario, esta ventana dependera de
    una ventana padre, una ventana de dialogo sirve para informar al usuario de una cuestion que se presenta en el sistema
'''
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, QLabel


#Extender de la clase Dialog para crear ventanas de manera mas sencilla
#AL momento de instanciarla vamos a crear una ventana modal, una ventana modal tambien recibe un objeto padre o ventana padre
class VentanaDialogo(QDialog):
    def __init__(self, padre=None):
        #estamos pasando la referencia de un objeto padre (padre)
        super().__init__(padre)
        self.setWindowTitle('Ventana de dialogo')
        #crear boton de aceptar y otro de cancelar
        #usando el simbolo | pay estamos concatenando mas botones
        botones = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        #creamos la variable de botones dialogo
        self.botones_dialogo = QDialogButtonBox(botones)
        #podemos usar la señal y el slot de accept ya que esta definido y el de rejected mas el slot de reject
        self.botones_dialogo.accepted.connect(self.accept)
        self.botones_dialogo.rejected.connect(self.reject)

        #creamos un layout para mostrar los botones
        self.layout = QVBoxLayout()
        mensaje = QLabel('Presiona alguno de los botones')
        #Mostramos o agregamos los widgets
        self.layout.addWidget(mensaje)
        self.layout.addWidget(self.botones_dialogo)
        #publicamos el layout
        self.setLayout(self.layout)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Dialogos en PySide')
        #Agregamos un boton
        boton = QPushButton('Mostrar Dialogo')
        boton.clicked.connect(self.click_boton)

        boton.setCheckable(True)

        #publicamos el boton
        self.setCentralWidget(boton)

    def click_boton(self,s):
        print(f'Click sobre el boton: {s}')
        #creamos el dialogo
        dialogo = VentanaDialogo(self)
        valor_retornado = dialogo.exec()
        print(f'Valor retornado: {valor_retornado}')
        if valor_retornado:
            print('Se presiono Ok')
        else:
            print('Se presiono Cancel')

    #Este codigo estaba asociado al boton click el cual permitia crear el objeto de tipo dialogo,antes de crear la clase VentanaDialogo
#CREAMOS el dialogo, debemos de pasar un objeto padre, de qmainwindow y sea el objeto padre del dialogo
        #dialogo = QDialog(self)
#ESTA ES UNA SUBVENTANA DE LA VENTANA PADRE
        #dialogo.setWindowTitle('Ayuda')
        #Crea un nuevo event loop
        #Se bloquea la ventana padre conocido como ventana modal y asta que cerremos las ventana hija se activa la ventana padre
#Para ejecutar la ventana modal debemos de llamar el evento exec
        #dialogo.exec()


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()




