'''
El uso del _ Es una indicacion al programador donde los atributos o metodos que lo usen
indica que no se beden de utilizar fuera de nuestra clase aunque si ce pueda
'''
#se recomienda utilizar el import demanera independiente
from mi_modulo import _funcion_protegida
from mi_modulo import  funcion_publica

class Mi_clase():

    def __init__(self):
        self.mi_variable_publica = 10
        #indica que fuera de esta clase no se debe de acceder a estas viaribles o argumnetos, leerlos o modificarlos
        self._mi_variable_protegida = 11




#El guion bajo al final se utiliza para evitar conflictos con los nombres (keywords)
#Ej. class, def, etc
def funcion1(nombre,class_):
    print('funcion que recibe una clase',nombre,class_)



if __name__ == '__main__':
    objecto = Mi_clase()
    print(objecto.mi_variable_publica)
    #no deberiamos acceder a atributos o metodos con un _ al inicio
    print(objecto._mi_variable_protegida)

    #accedemos a las funciones del modulo importado
    funcion_publica()
    #ni siquiera hace referencia, el interprete no la toma como parte de este modulo, solo donde se creo
    #si utilizamos el import * no se podra acceder a funciones con _ al inicio
    _funcion_protegida()

    funcion1('Giovanni',None)
