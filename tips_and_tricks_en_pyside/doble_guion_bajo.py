'''
Con doble guion bajo no solo es una convencion
si no que afecta la forma en la que se acceden los atributos y metodos

 técnica utilizada para resolver diversos problemas causados ​​ por
 la necesidad de tener nombres únicos para las entidades de programación
 en muchos lenguajes de programación modernos.
'''

class Padre():
    def __init__(self):
        self.variable_publica = 1
        self._variable_protegida = 2 # no se puede acceder de manera direccta
        self.__variable_privada = 3 #no se puede acceder de manera directa por la clase o subclases #name mangling = __

    #Uso de doble __ bajo, dentro de la clase se puede acceder y fuera debemos de utilizar name mangling
    def get_variable_privada(self):
        return self.__variable_privada

#metodos con doble guion bajo:
    def __metodo_privado(self):
        print('Accediendo metodo privado desde la clase padre')

#uso de doble gion __ en subclases
class Hijo(Padre):
    def __init__(self):
        super().__init__()
        self.variable_publica = 'Sobreescrita 1'
        self._variable_protegida = 'Sobreescrita 2'
        self.__variable_privada = 'Sobreescrita 3'

    def __metodo_privado(self):
        print('Accediendo metodo privado desde la clase hija')

#prueba usando una variable global
_Prueba__varable_global = 10

class Prueba():
    def obtener_variable(self):
        return _Prueba__varable_global





if __name__ == '__main__':
    padre = Padre()
    #dir nos muestra todo lo que contiene un objeto relacionado o la clase
    print(dir(padre))
    #accedemos a los atributos de la clase
    print(f'Variable publica: {padre.variable_publica}')
    print(f'Variable protegida: {padre._variable_protegida}')
    #print(f'Variable privada manda error: {padre.__variable_privada}')
    print(f'Variable privada usando name_mangling: {padre._Padre__variable_privada}')

    #Name manglin es transparente para el programador
    print(f'Accedo por medio del metodo get: {padre.get_variable_privada()}')
    print(' ')

    #pRUEBA DE LA CLASE HIJO
    hijo = Hijo()
    print(dir(Hijo))
    print(f'Acceso desde la clase hijo: {hijo.variable_publica}')
    print(f'Acceso desde la clase hijo: {hijo._variable_protegida}')
    #print(f'Acceso desde la clase hijo: {hijo.__variable_privada}') no podemos acceder desde la clase hijo
    #para acceder utilizamos name mangling desde la clase hija
    print(f'Acceso privado desde la clase hijo con name mangling: {hijo._Hijo__variable_privada}')
    print(f'Acceso privado desde hijo a la clase padre: {hijo._Padre__variable_privada}')

    print(' ')
    #tambien podemos usar metodos con doble guion __
    #padre.__metodo_privado() marca error
    #utilizando name mangling
    padre._Padre__metodo_privado()
    hijo._Hijo__metodo_privado()

    #accediendo a la variable global
    print(' ')
    print(f'Accediendo a la variable global: {_Prueba__varable_global}')


    #clase Prueba, en automatico se aplica nema mangling
    print(' ')
    prueba = Prueba()
    print(f'Accediendo variable global desde una clase: {prueba.obtener_variable()}')
