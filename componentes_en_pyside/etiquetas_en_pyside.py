'''
Etiquetas en pyside, componentes
Un COMPOnentes es un elemento que se mostrara en la GUI
Tipos de componentes: Checkbox, combobox,fecha, fecha y hora, marcador o dial
slide, radiobutton, etc

QMainWindow es la clase padre
'''
import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QCheckBox, QComboBox, QListWidget, QLineEdit

'''
#etiquetas
class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        #creamos un componente de tipo etiqueta(Label)
        etiqueta = QLabel('Hola')
        #modificamos el valor inicial, settext permite modificar el valor de la etiqueta
        etiqueta.setText('Saludos ')
        #modificar el tipo de fuente, primero recuperamos el tipo de fuente
        fuente = etiqueta.font()
        fuente.setPointSize(24)#modifica el tamaño de la fuente
        etiqueta.setFont(fuente)#corremos el cambio de fuente
        #modificar la alineacionde la etiqueta
        #etiqueta.setAlignment(Qt.AlignCenter)
        #Otra forma de alinear de manera Horizontal y Vertical
        etiqueta.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter )

        #publicamos el componente
        self.setCentralWidget(etiqueta)

'''

#mANEJO DE una imagen en una etiqueta
'''
class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        self.setFixedSize(500, 600)
        #creamos un componente de tipo etiqueta(Label)
        etiqueta = QLabel('Hola')
        #setPixmap nos permite publicar una imagen cuando trabajamos con una etiqueta
        #se envuelve en la clase QPixmap = mapa de pixeles
        etiqueta.setPixmap(QPixmap('layla.jpg'))
        #setScaledContents escala el contenido segun el tamaño de la ventana
        etiqueta.setScaledContents(True)

        #publicamos el componente
        self.setCentralWidget(etiqueta)'''


#Componente checkbox
'''
class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        #creamos un nuevo componente de checkbox
        checkbox = QCheckBox('Este es un checkbox')
        #activamos el tercer estado con True y dos on False
        checkbox.setTristate(False)
        #conectar la señal de cambio de componente
        checkbox.stateChanged.connect(self.mostrar_estado)

        #publicamos el componente
        self.setCentralWidget(checkbox)

    def mostrar_estado(self, estado):
        print('Estado checkbox:', estado)
        #Trabajamos con las constantes
        if estado == Qt.CheckState.Checked:
            print('Checkbox encendido - 2')
        elif estado == Qt.PartiallyChecked:
            print('Checkbox parcialemte checado -1')
        elif estado == Qt.CheckState.Unchecked:
            print('Checkbox apagado  - 0')
        else:
            print('Checkbox con estado invalido')
'''

#Combo box
'''
class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        #creamos un nuevo componente combobox-> (drop down list)
        combobox = QComboBox()
        #agregamos los elementos
        combobox.addItem('Uno')
        combobox.addItems(['Dos','Tres','Cuatro'])
        #señales del combobox, monitoriamos el cambio de elemento seleccionado tanto en indice como elemento
        combobox.currentIndexChanged.connect(self.cambio_indice)
        #monitoriall el cambio de texto
        combobox.currentTextChanged.connect(self.cambio_texto)
        #hacemos editable el combobox con setEditable
        combobox.setEditable(True)
        #especificamos la politica de insertion, ahi varios tipos de politicas, "noinsert" no permite modificar
        #combobox.setInsertPolicy(QComboBox.NoInsert)
        #Agregar al inicio del ComboBox y lo setea al aplicar enter
        #combobox.setInsertPolicy(QComboBox.InsertAtTop)
        #Modifica el elemento actual y lo setea al aplicar enter
        #combobox.setInsertPolicy(QComboBox.InsertAtCurrent)
        #Insertar al final del combo box
        #combobox.setInsertPolicy(QComboBox.InsertAtBottom)
        #Insertar antes del elemento actual
        #combobox.setInsertPolicy(QComboBox.InsertBeforeCurrent)
        #Insertar despues del elemento actual o seleccionado
        #combobox.setInsertPolicy(QComboBox.InsertAfterCurrent)
        #insertar alfabeticamnete
        combobox.setInsertPolicy(QComboBox.InsertAlphabetically)

        #podemos limitar la cantidad de elemento a agregar el combobox
        combobox.setMaxCount(6)


        #publicamos el componente
        self.setCentralWidget(combobox)

    def cambio_indice(self,nuevo_indice):
        print('Nuevo indice seleccionado', nuevo_indice)

    def cambio_texto(self,nuevo_texto):
        print('Nuevo texto seleccionado', nuevo_texto)
'''

#Componente QListWidget,
# es como un combobox solo que en este se pueden seleccionar varios elementos
#Tambien despliega todos los elemento de una vez y seleccionar uno o varios al mismo tiempo,
# no se puede hacer editable y no tiene politicas de insercion
'''
class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        #creamos nuestro QListWidget se parece al combobox
        lista = QListWidget()
        #agregamos los elementos
        lista.addItem('Uno')
        lista.addItems(['dos','tres'])
        #monitoriamos el cambio del elemento seleccionado, señales contiene 2, retorna el elemento con el texto
        lista.currentItemChanged.connect(self.cambio_elemento)
        lista.currentTextChanged.connect(self.cambio_texto)



    #publicamos el componente
        self.setCentralWidget(lista)

    def cambio_elemento(self,cambio_elemento):
        print('Nuevo elemento seleccionado', cambio_elemento.text())#en vez de que retorne el objeto, usamos text para que retorne la etiqueta de text

    def cambio_texto(self,nuevo_texto):
        print('Nuevo texto seleccionado', nuevo_texto)

'''

#QlineEdit permite capturar informacion que escriba el usuario
#linea de edicion de texto
class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        #componente qlineedit
        linea_texto = QLineEdit()
        #Una vez creado podemos establecer varias propiedades
        #Maximo de carecteres a captuar
        linea_texto.setMaxLength(15)
        #especificar algun texto de ayuda para especificar que es lo que debe de capturar el usuario, conocido como placeholder
        linea_texto.setPlaceholderText('Introduce tu nombre: ')
        #Colocarlo en modo lecture
        #validacion aplicando una mascara
        linea_texto.setInputMask('00-0000-0000') #0 indica que capturaremos digitos
        #linea_texto.setReadOnly(True)
        #monitoriar eventos: enter(),cambio seleccion de texto(se lanza cuando seleccionamos el texto), cambio de texto(al cambiar texto de la caja)
        linea_texto.returnPressed.connect(self.enter_presionado)
        #cambio de seleccion
        linea_texto.selectionChanged.connect(self.cambio_seleccion)
        #Cuando cambiamos el texto
        linea_texto.textChanged.connect(self.cambio_texto)


     #publicamos el componente
        self.setCentralWidget(linea_texto)

    def enter_presionado(self):
        print('Se presionó el enter')
        #con esta forma podemos acceder al componente y con setText podemos cambiar el texto
        self.centralWidget().setText('00-0000-0000')

#este metodo se activa al seleccionar alguna palabra
    def cambio_seleccion(self):
        print('Cambio seleccion texto')
        #acceder a lo que selecciona el usuario
        print(self.centralWidget().selectedText())

    def cambio_texto(self, cambio_texto):
        print('Cambio de texto')
        print(cambio_texto)

if __name__ == '__main__':
    #Creamos el objeto de la aplicacion
    app = QApplication([])
    #Creamos una instancia de la clase
    ventana = Componentes()
    ventana.show()
    sys.exit(app.exec())
