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

#Ventana con dialogo personalizada
    def click_boton(self,s):
        print(f'Click sobre el boton: {s}')
        #metodo cuestion nos pide un objeto padre, titulo, text, botones
        #Creamos el dialogo personalizado
        dialogo = QMessageBox.critical(self, 'Problema critico','Ventana con problema critico',
                                       buttons=QMessageBox.Discard |
                                       QMessageBox.NoToAll |
                                       QMessageBox.Ignore,
                                       defaultButton=QMessageBox.Discard)#default hace que el boton este marcado en azul o resaltado
        if dialogo == QMessageBox.Discard:
            print('Regreso el valor Discard')
        elif dialogo == QMessageBox.NoToAll:
            print('Regreso el valor NoToAll')
        else:
            print('Se presiono el boton de ignorar')


#Ventana de dialogo con pregunta simplificada, en esta ventana no requiere del uso del metodo exec()
    #def click_boton(self,s):
     #   print(f'Click sobre el boton: {s}')
        #dialogo de tipo question
        #metodo cuestion nos pide un objeto padre, titulo, text, botones
      #  dialogo = QMessageBox.question(self, 'Pregunta', 'Ventana con pregunta')

       # if dialogo == QMessageBox.Yes:
            #print('Regreso el valor Yes(Si)')
        #else:
         #   print('Regreso el valor de No')


'''    
# QMessageBox con dos botones
    def click_boton(self,s):
        print(f'Click sobre el boton: {s}')
        #creamos el dialogo usando la clase QMessage
        dialogo = QMessageBox(self) #tambien le debemos de pasar un objeto padre
        dialogo.setWindowTitle('Dialogo con pregunta')
        dialogo.setText('Ventana de Dialogo con Pregunta')
        #agregamos los botones de la respuesta a la pregunta
        dialogo.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        #agregamos icono a la ventana de dialogo
        dialogo.setIcon(QMessageBox.Question)#tambien existe Question, Information, Warning and Critical
        valor_retornado = dialogo.exec()
        #Imprimir el valor retornado, siempre retorna 1 = True o 1024 en este caso
        print(f'Valor retornado: {valor_retornado}')
        if valor_retornado == QMessageBox.Yes: #usamos una de las constantes de QMessageBox -> Ok es una de ellas
            print('Regreso el valor Yes(Si)')
        else:
            print('Regreso el valor de No')'''


'''con un boton de ok
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
'''

if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
