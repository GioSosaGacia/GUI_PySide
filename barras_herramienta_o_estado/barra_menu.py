from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QToolBar, QStatusBar, QCheckBox
from PySide6.QtCore import Qt, QSize


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Barra herramientas en PySide')
        #debemos de publicar un componentes antes de agregar nuestra barra de herramientas
        #Publicamos una etiqueta
        etiqueta = QLabel('Hola')
        etiqueta.setAlignment(Qt.AlignCenter)
        #Publicamos la etiqueta con
        self.setCentralWidget(etiqueta)

#creamos la barra de herramientas
        barra = QToolBar('Mi barra de herramientas')
        #debemos de indicar el tamaño de los iconos ya que serán de 16 px
        barra.setIconSize(QSize(16,16))
#configuracion de barra de herramientas
        #Para ver como se presentaran los iconos usamos, esta se usa por defecto Qt.ToolButtonFollowStyle)
        #barra.setToolButtonStyle(Qt.ToolButtonFollowStyle) con Qt.TextButtonTextOnly = quita los iconos, con Qt.TextButtonIconOnly
        #barra.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)#Muestra el icono mas el texto
        barra.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)#Muestra el texto debajo del icono
        self.addToolBar(barra)


        #agregar elemento a la barra de herramientas o menu con QAction -> permite configurar una vez una accion
        #agregamos un elemento a nuestra barra de herramientas, QAction permite agregar el componente en varias partes
#boton nuevo
        boton_nuevo = QAction(QIcon('nuevo.png'),'Nuevo', self)#nombre del boton, mas el componente donde se agregara que en este caso es la ventana self
        #agregamos el boton a la barra
        barra.addAction(boton_nuevo)


        #Barra de estado es lo que se muestra en la parte inferior de nuestra aplicacion
        self.setStatusBar(QStatusBar(self))

        #Mostramos mensaje del boton de accion
        boton_nuevo.setStatusTip('Nuevo archivo')


        #Para saber si hemos dado click o no lo hacemos checable
        #boton_nuevo.setCheckable(True) #True cuando se presiona, false cuando deja de presionarlo


        #tambien podemos configurar un slot para que al momento de presionar el mismo se muestre alguna informacion
        #Asociamos el evento click, triggered permite se conecta al slot creado
        boton_nuevo.triggered.connect(self.click_boton_nuevo)

#boton guardar
        boton_guardar = QAction(QIcon('guardar.png'),'Guardar', self)
        barra.addAction(boton_guardar)
        boton_guardar.setStatusTip('Guardar Archivo')
        boton_guardar.triggered.connect(self.click_boton_guardar)

#pARA AGREGAR UN SEPARARDOR A LA BARRA
        barra.addSeparator()

#Tambien podemos agregar componentes a la barra de herramientas
        barra.addWidget(QCheckBox())

        #pARA AGREGAR UN SEPARARDOR A LA BARRA
        barra.addSeparator()
        barra.addWidget(QLabel('Salir'))



    def click_boton_nuevo(self,s):#s-> estado
        print(f'Nuevo archivo: {s}')

    def click_boton_guardar(self,s):
        print(f'Guardar archivo: {s} ')


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()




