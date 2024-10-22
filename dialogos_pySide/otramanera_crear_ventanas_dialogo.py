'''
Existen mas formas o clases para facilitar la creacion de ventanas de dialogos la cual ya incluye boton de ok
'''
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox


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
        #creamos el dialogo usando la clase QMessage
        dialogo = QMessageBox(self) #tambien le debemos de pasar un objeto padre
        dialogo.setWindowTitle('Dialogo simple')
        dialogo.setText('Ventana de Dialogo Simple')
        valor_retornado = dialogo.exec()
        #Imprimir el valor retornado, siempre retorna 1 = True o 1024 en este caso
        print(f'Valor retornado: {valor_retornado}')
        if valor_retornado == QMessageBox.Ok: #usamos una de las constantes de QMessageBox -> Ok es una de ellas
            print('Regreso el valor Ok')
        else:
            print('Regreso distinto a Ok')



if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
