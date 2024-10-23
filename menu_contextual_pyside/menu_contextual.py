'''
Menu tipo contextual es el que aparece al presionar click derecho del mouse
sobre una ventana, existen dos manera de crearlo:

1. Con la clase QWidget
2.
'''
from PySide6.QtGui import QAction, QIcon, Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QMenu


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Menu contextual')
#2da forma para crear el menu contextual
        #mostramos y conectamos el menu contextual
        self.show()
        #nos conectamos a las señal de CustomContextMenuRequested
        #antes agregamos esta linea para indicar que vamos a personalizar un menu contextual
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        #necesitamos conectarnos a una señal customContextMenuRequested
        self.customContextMenuRequested.connect(self.mostrar_menu_contexto)

#segunda forma
    def mostrar_menu_contexto(self,posicion):
        #Menu contextual sobreescribiendo el metodo heredado de la clase qwidget
    #1er. forma usando -> def contextMenuEvent(self, evento):
    #Parte del 2do. 1.0
        #usamos qmenu para crearlo y nos pide donde publicarlo, usamos self ya que sera en la ventana principal
        menu_contextual = QMenu(self)
        boton_nuevo = QAction(QIcon('nuevo.png'),'Nuevo',self)
        boton_guardar = QAction(QIcon('guardar.png'),'Guardar',self)
        boton_salir = QAction(QIcon('salir.png'),'Salir',self)

    #1er. ejemplo sin iconos, yo agrege los iconos
        #una vez creado podemos agregar acciones en lugar de widgets, creamos la accion nuevo,guardar y salir
        #el parametro padre -> self es parte de la accion
        #menu_contextual.addAction(QAction(QIcon('nuevo.png'),'Nuevo',self))
        #menu_contextual.addAction(QAction(QIcon('guardar.png'),'Guardar',self,))
        #menu_contextual.addAction(QAction(QIcon('salir.png'),'Salir',self))

    #2do. Conectamos con la opcion triggerd.connect(), señales y slots
        boton_nuevo.triggered.connect(self.click_boton_nuevo)
        boton_guardar.triggered.connect(self.click_boton_guardar)
        boton_salir.triggered.connect(self.click_boton_salir)

    #2do. Agregando iconos al menucontextual mas una funcion o slot 1.1
        menu_contextual.addAction(boton_nuevo)
        menu_contextual.addAction(boton_guardar)
        menu_contextual.addAction(boton_salir)

         #se debe de publicar en una ventana padre, para hacerlo usaremos la variable evento
        #recuperamos la posicion del cursor como posicion global de la ventana padre
        #globalPos() recupera la posicion donde se dio click para desplegar el menu contextuañ
        #EJECUTAMOS el menu contextual
        #1rra forma menu_contextual.exec(evento.globalPos())

        #2da forma, con mapToGlobal -> la utilizamos para desplegar ests tipos de menus
        menu_contextual.exec(self.mapToGlobal(posicion))

    def click_boton_nuevo(self,s):
        print('Opcion nuevo...')

    def click_boton_guardar(self,s):
        print('Opcion guardar...')

    def click_boton_salir(self,s):
        print('Opcion salir...')


if __name__ =='__main__':
    app = QApplication()
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
