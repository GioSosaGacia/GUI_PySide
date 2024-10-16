'''
Para empezar a desarrollar una aplicación debemos de utilizar el objeto de
 → QAplication: permite procesar los eventos de la aplicación, click,
  arrastar un boton, etc.
'''
import sys

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

'''
# QAplication: permite procesar los eventos de la aplicación (event loop), click,arrastar un boton, etc.
#Clase base de Qt que es de paga y la gratuita es PySide, si sabes qt sabs pyside ya que es lo mismo
app = QApplication()

#la aplicacion por lo menos debe de tener un objeto de tipo ventana
#crear objeto ventana
#ventana = QWidget()

#Cualquier componente puede ser utilizado como un objeto de tipo ventana en pyside siempre y cuando sea el principal
#ventana = QPushButton('Boton de PySide')#crear botones

#como crear objetos de tipo ventana, indica que es la ventana principal
#cada widget tiene sus caracteristicas
#Qt has QMainWindow and its related classes for main window management.
# QMainWindow has its own layout to which you can add QToolBars,
# QDockWidgets, a QMenuBar, and a QStatusBar. The layout has a center
# area that can be occupied by any kind of widget.
ventana = QMainWindow()

#Cambiar el titulo
ventana.setWindowTitle('Hola mundo con PySide')

#modificar el tamaño de la ventana
ventana.resize(600, 400)

#Mostrar la ventana
ventana.show()

#Se ejecuta la aplicacion y para cerrarla con sys.exit()
sys.exit(app.exec())
'''

#Mejora aplicando OOP en PySide
import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PySide6.QtCore import  QSize
#tambien podemos heredar de
class VentanaPySide(QMainWindow):

    def __init__(self):
        #llamamos el metodo init de la clase padre
        super().__init__()
        self.setWindowTitle('POO con Pyside')
        #self.resize(600, 400)
        #QSize establece valores de la ventana fijos, se debe de importar QSize
        self.setFixedSize(QSize(600, 400))
        #creaion de componentes
        self._agregar_componentes()

    def _agregar_componentes(self):
        #crear un menu con menuBar()
        menu = self.menuBar()
        menu_archivo = menu.addMenu('Archivo')#addMenu agrega un submeno al menu principal
        #agregamos algunas opciones al menu,QAction = permite agregar una nueva opcion al menu de archivo
        #se debe de importar el QAction
        accion_nuevo = QAction('Nuevo', self)
        menu_archivo.addAction(accion_nuevo)
        #agregamos texto a la barra de estado con statusTip
        accion_nuevo.setStatusTip('Nuevo archivo')
        #agregamos mensaje en la barra de estado que es la parte inferior, indica el estado actual
        self.statusBar().showMessage('Informacion de la barra de estado')
        #agregamos un componente de boton
        boton = QPushButton('Nuevo Boton ')
        #para que se vizualice lo publicamos en la ventana con
        self.setCentralWidget(boton)



if __name__ == '__main__':
    #creamos un objeto de tipo qapplication para la gestion de eventos
    app = QApplication([])
    #creamos el objeto de tipo ventana
    ventana = VentanaPySide()
    ventana.show()
    #ejecutamos la ventana
    sys.exit(app.exec())

