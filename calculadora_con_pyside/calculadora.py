import sys
from functools import partial
from idlelib.zoomheight import set_window_geometry

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QLineEdit, QGridLayout, QPushButton


class Calculadora(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculadora')
        self.setFixedSize(240,240)
        #agregamos un componente para poder publicar el layout
        self.componente_general = QWidget(self)
        #publicamos el componente general
        self.setCentralWidget(self.componente_general)
        #crearemos el layout el cual va a alojar todos los elementos incluyendo el grid
        self.layout_principal = QVBoxLayout()
        #el componente general llamamos el metodo setLayout y publicamos el layout principal
        self.componente_general.setLayout(self.layout_principal)
        #metodo para crear la parte visual de la calculadora
        self._crear_area_captura()
        self._crear_botones()
        #conectamos las señales con los slots de cada uno de los botones
        self._conectar_botones()

    def _crear_area_captura(self):
        #par capturara la informacion creamos una entrada de tipo lineedit
        self.linea_entrada = QLineEdit()
        #modificamos algunas propiedades como la altura de la linea_entrada
        self.linea_entrada.setFixedHeight(35)
        #alineamos la entrada de datos a la derecha
        self.linea_entrada.setAlignment(Qt.AlignRight)#center, left etc
        #Para que sea de solo lectura esta linea de entrada
        self.linea_entrada.setReadOnly(True)
        #lo agregamos la linea_entrada  al layout principal
        self.layout_principal.addWidget(self.linea_entrada)

    def _crear_botones(self):
        #Utilizaremos un diccionario vacio para crear nuestro botones por un lado la posicion y por el otro el texto
        self.botones = {}
        #contiene el grid
        layout_botones = QGridLayout()
        #texto | posicion en el grid, definicion de los botones
        self.botones = {
            '7':(0,0),
            '8':(0,1),
            '9':(0,2),
            '/':(0,3),
            '4':(1,0),
            '5':(1,1),
            '6':(1,2),
            '*':(1,3),
            '1':(2,0),
            '2':(2,1),
            '3':(2,2),
            '-':(2,3),
            '0':(3,0),
            '.':(3,1),
            'C':(3,2),
            '+':(3,3),
            '=':(3,4)
        }
        #crEAMOS LOS botones y los agregamos al grid layout
        #La posicion es una tupla con dos valores: renglon, columna, texto_boton{llave}, posicion{valor}
        for texto_boton, posicion in self.botones.items():
            self.botones[texto_boton] = QPushButton(texto_boton)
            self.botones[texto_boton].setFixedSize(40,40)
            #publicamos el boton en el grid layout
            layout_botones.addWidget(self.botones[texto_boton],posicion[0], posicion[1])
        #agregamos el layout de botones al layout principal
        self.layout_principal.addLayout(layout_botones)

#necesitaremos unos metodos adicionales
    def _conectar_botones(self):
        #Recorrer cada boton del diccionario (key:value) (texto:PushButton)
        for texto_boton, boton in self.botones.items():
            #solo en 2 casos no queremos asignar el slot en = y C
            if texto_boton not in {'=','C'}:
                #Lambda se manda a llamar asta que se presiona el boton y recoje el utimo dato que seria = de la variable texto_boton
                #boton.clicked.connect(lambda: self._construir_expresion(texto_boton))
        #Cuendo se de clicked en un boton nos conectamos a tal señal
        #_construir_expresion: texto_boton:
        #partial permite asociar la llamada del metodo con el parametro respetivo de manera fija
                boton.clicked.connect(partial(self._construir_expresion, texto_boton))
        #CONECTAMOS EL botonde limpiar texto C -> clear en ingles
            self.botones['C'].clicked.connect(self._limpiar_linea_entrada)
    #se realizara de dos formas 1. si presiona la tecla =, 2. al presionar enter sobre la linea de enetrada con returnPressed
        #conectamos el boton de igual = para evaluar la expresion
            self.botones['='].clicked.connect(self._calcular_resultado)
            self.linea_entrada.returnPressed.connect(self._calcular_resultado)

    def _construir_expresion(self, texto_boton):
        expresion = self.obtener_texto() + texto_boton
        #actualizar la expresion de entrada
        self.actualizar_texto(expresion)

    def obtener_texto(self):
        return self.linea_entrada.text()

    def actualizar_texto(self, texto):
        self.linea_entrada.setText(texto)
        self.linea_entrada.setFocus()

    def _limpiar_linea_entrada(self):
        self.actualizar_texto('')

    def _calcular_resultado(self):
        resultado = self._evaluar_expresion(self.obtener_texto())
        self.actualizar_texto(resultado)

    def _evaluar_expresion(self, expresion):
        try:
            #Utilizamos eval para evaluar la expresion
            resultado = str(eval(expresion))
        except Exception as e:
            resultado = 'Ocurrio un error '
            print(f'Ocurrio un error: {resultado}')
        return resultado



if __name__ == '__main__':
    app = QApplication([])
    calculadora = Calculadora()
    calculadora.show()
    sys.exit(app.exec())
