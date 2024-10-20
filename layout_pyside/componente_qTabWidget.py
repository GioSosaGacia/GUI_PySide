'''
Componentes en ves de usar layout

'''
from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QGridLayout, QStackedLayout, QVBoxLayout, QHBoxLayout, \
    QPushButton, QTabWidget


class Color(QWidget):
    def __init__(self, nuevo_color):
        super().__init__()
        #indicamos que se puede agregar un color de fondo bg
        self.setAutoFillBackground(True)
        #palette crea  una paleta de colore y poder especificar un color
        paletaColores = self.palette()
        #creamos el componente de color de fondo aplicando el nuevo color
        paletaColores.setColor(QPalette.Window, QColor(nuevo_color))
        #aplicamos el nuevo color al componente que se esta creando
        self.setPalette(paletaColores)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tabulador en PySide')

        #creamos el componente de tab
        tabulador = QTabWidget()
        #Posicion de las etiquetas del tabulador
        tabulador.setTabPosition(QTabWidget.North)#podemos manejar los cuatro puntos cardinales
        #Indicamos si queremos que se muevan las etiquetas del tabulador
        tabulador.setMovable(True)
        #Para que se vea similar a MacOS
        tabulador.setDocumentMode(True)

        #Agregamos los colores a cada tabulador
        tabulador.addTab(Color('red'),'Rojo')
        tabulador.addTab(Color('yellow'),'Amarillo')
        tabulador.addTab(Color('green'),'Verde')



        self.setCentralWidget(tabulador)

if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
