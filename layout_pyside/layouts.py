'''
Layout en PySide permite agregar varios componentes dentro de nuestra pantalla
ya se de manera vertical yu horizontal

'''
import sys

from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QVBoxLayout, QHBoxLayout


#lo hacemos por colores para identificar los componentes dentro de cada layout, pero no es necessario crear la clase color
#solo se hace para identificar los componentes dentro de cada layout


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
        self.setWindowTitle('Layouts en PySide')
        #CON ESTA LINEA PLICAMOS EL COLOR A NUESTRO LAYOUT
        #componente_color_con_fondo = Color('#C8E6C9')
        #el componente se expande para cubrir el tamaño disponible

#antes de anidar layouts
        #LAYOUT VERTICAL -> QVBoxLayout() Y Horizontal -> QHBoxLayout()
        #layout = QVBoxLayout()
        #ANTES DE ANIDAR LAYOUTS
        #layout.addWidget(Color('#81C784'))#81C784

        #publicamos el layout, necesitamos un componente 'generico' ya que no se puede publicar directamente a setCentralWidget
        #para ello utilizamos el QWidget
        #componente = QWidget()
        #agregamos el layout al componente generico
        #componente.setLayout(layout)


#con layouts anidados
        #Anidar layouts -> un layout dentro de otro layout
        #Creamos primero el layout horizontal t despues el vertical
        layout_horizontal = QHBoxLayout()
        #agregamps espacio al margen horizontal
        layout_horizontal.setContentsMargins(5,10,5,10)
        #AGREGAMOS un espacio entre cada elemento del layout horizontal
        layout_horizontal.setSpacing(10)
        layout_vertical = QVBoxLayout()
        #agregamos espacion entre los layout vertical
        layout_vertical.setContentsMargins(5,10,5,10)
        #agregamos espacio dentro de cada elemento layout vertical
        layout_vertical.setSpacing(20)

        #AGREGAMOS algunos widget al layout vertical
        #agregmos un nuevo componentes de color
        layout_vertical.addWidget(Color('#81C784'))#81C784
        #agregamos mas componentes de tipo layout al vertical
        layout_vertical.addWidget(Color('#C8E6C9'))#C8E6C9
        layout_vertical.addWidget(Color('#E8F5E9'))#E8F5E9

        #agregamos el layout vertical dentro del Horizontal, de manera anidada un layout dentro del otro
        layout_horizontal.addLayout(layout_vertical)
        #agregamos mas elemento al layout  horizontal
        layout_horizontal.addWidget(Color('#B2DFDB'))
        layout_horizontal.addWidget(Color('#B2DFDB'))
        layout_horizontal.addWidget(Color('#B2DFDB'))
        layout_horizontal.addWidget(Color('#B2DFDB'))
        #CREAMOS Un componente generico para poder publicar el layout
        componente = QWidget()
        #agregamos el layout al componente generico y se agregara el layout mas externo
        componente.setLayout(layout_horizontal)

        self.setCentralWidget(componente)

if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()




