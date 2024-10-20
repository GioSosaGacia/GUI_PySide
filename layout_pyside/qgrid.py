from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QGridLayout, QStackedLayout, QVBoxLayout, QHBoxLayout, \
    QPushButton


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


       #Layout Grid
        #layout = QGridLayout()
        #layout.addWidget(Color('#B2DFDB'),0,0)
        #layout.addWidget(Color('#B2DFDB'),0,1)
        #layout.addWidget(Color('#B2DFDB'),3,0)
        #layout.addWidget(Color('#B2DFDB'),1,2)
        #layout.addWidget(Color('#B2DFDB'),2,3)

        #CREAMOS Un componente generico para poder publicar el layout
        #componente = QWidget()
        #agregamos el layout al componente generico y se agregara el layout mas externo
        #componente.setLayout(layout)

        #self.setCentralWidget(componente)




        #otro tipo de layout ->QStackedLayout: permite mostrar un layout encima de otro, Stacked = apilado
        #layout = QStackedLayout()
        #por defaul solo se visualiza el 1er widget agregado
        #layout.addWidget(Color('black'))
        #layout.addWidget(Color('blue'))
        #layout.addWidget(Color('yellow'))
        #NoS permite seleccionar el widget que se desea visualizar, colocando el index del mismo
        #layout.setCurrentIndex(0)



#1: Crear un verticalBox, 2:agregamos dos layouts, dentro de un vertical horizontal agregaremos 3 botones
#4:despues agregaremos un stackedLayout, cada boton seleccionara un stackLayout

#Creamos los layouts
        layout_principal = QVBoxLayout()
        layout_botones = QHBoxLayout()
        #agregamos un layout de tipo stackedLayout, como vamos acceder a el desde otros metodos desde esta misma clase lo agregaremos como atributo
        self.layout_tipo_stack = QStackedLayout()

#Agregamos los layout hijos al layout principal
        layout_principal.addLayout(layout_botones)
        layout_principal.addLayout(self.layout_tipo_stack)

#crear los botones del layout de botones
        boton_verde = QPushButton('Mist')
        #publicar este boton en layout de botones
        layout_botones.addWidget(boton_verde)
        #Publicamos el color rojo al layout de tipo stacked
        self.layout_tipo_stack.addWidget(Color('#90AFC5'))
        #conectamos el evento pressed del boton respectivo
        boton_verde.pressed.connect(lambda:self.activar_tabulador(0))

#creamos el boton azul
        boton_azul = QPushButton('Stone')
        layout_botones.addWidget(boton_azul)
        self.layout_tipo_stack.addWidget(Color('#336b87'))
        boton_azul.pressed.connect(lambda:self.activar_tabulador(1))

 #Creamos el boton amarillo
        boton_amarillo = QPushButton('Shadow')
        layout_botones.addWidget(boton_amarillo)
        self.layout_tipo_stack.addWidget(Color('#2A3132'))
        boton_amarillo.pressed.connect(lambda:self.activar_tabulador(2))


        #antes de conectar los botones al stacked
        #pARA SELECCIONAR el elemento dentor de layout_tipo_stack usamos -> setCurrentIndex(2) + <- el indice desceado
        #self.layout_tipo_stack.setCurrentIndex(2)


        #CREAMOS Un componente generico para poder publicar el layout
        componente = QWidget()
        #agregamos el layout al componente generico y se agregara el layout mas externo
        componente.setLayout(layout_principal)
        self.setCentralWidget(componente)

    def activar_tabulador(self,indice):
        self.layout_tipo_stack.setCurrentIndex(indice)
        print(f'Indice seleccionado: {indice}')


    '''
    Para evetar tantas funciones mejor creamos una funcion lamda
    def activar_color_mist(self):
        self.layout_tipo_stack.setCurrentIndex(0)

    def activar_color_stone(self):
        self.layout_tipo_stack.setCurrentIndex(1)

    def activar_color_shadow(self):
        self.layout_tipo_stack.setCurrentIndex(2)'''

if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
