'''Eventos: relacionados con el mouse y sus botones
Click, Boton de maouse, si movemos el cursor

Qwidget es la clase padre de QMainWindow es donde estan definidos los eventos:
    de mouseMoveEvent, mousePressEvent,
'''

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Eventos')
        self.etiqueta = QLabel('Dar click en esta ventana')
        #publicar la etiqueta
        self.setCentralWidget(self.etiqueta)

#si se mueve el cursor sobre la etiqueta
    #def mouseMoveEvent(self, evento):
     #   self.etiqueta.setText('Evento: MouseMoveEvent detectado')

#presionamos
    def mousePressEvent(self, event):
        #antes de los eventos left, right and middle
        self.etiqueta.setText('Evento: MousePressEvent detectado')

#Se puede usar los mismos eventos para cada una de las funciones

#tambien podemos detectar si se presiono el boton izquierdo o derecho del mouse,
#tal inf esta relacionada a la variable evento
        #preguntamos por el boton del mouse que lanzo el evento
        if event.button() == Qt.LeftButton:
            self.etiqueta.setText('MousePressEvent Boton Izquierdo')
        elif event.button() == Qt.MiddleButton:
            self.etiqueta.setText('MousePressEvent Boton central')
        elif event.button() == Qt.RightButton:
            self.etiqueta.setText('MousePressEvent Boton derecho..')
#liberamos
    def mouseReleaseEvent(self, event):
        #self.etiqueta.setText('Evento: mouseReleasedEvent detectado')

        if event.button() == Qt.LeftButton:
            self.etiqueta.setText('mouseReleasedEvent: Boton Izquierdo')

#doble click
    def mouseDoubleClickEvent(self, event):
        self.etiqueta.setText('Evento: mouseDoubleClickEvent detectado')

        if event.button() == Qt.LeftButton:
            self.etiqueta.setText('mouseDoubleClickEvent Boton Izquierdo')
        elif event.button() == Qt.MiddleButton:
            self.etiqueta.setText('mouseDoubleClickEvent Boton central')
        elif event.button() == Qt.RightButton:
            self.etiqueta.setText('mouseDoubleClickEvent Boton derecho..')



if __name__ == '__main__':
    app = QApplication()
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
