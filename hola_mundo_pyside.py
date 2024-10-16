'''
Para empezar a desarrollar una aplicación debemos de utilizar el objeto de
 → QAplication: permite procesar los eventos de la aplicación, click,
  arrastar un boton, etc.
'''
import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

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


