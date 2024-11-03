'''
ABC -> Abstract Base Class
Las clases abstractas no se pueden instanciar, sirve para definir una gerarquia de clases
#pERMITE asgeurarnos que las clases que heredan implementen los metodos de la clase padre


Las clases abstractas en Python son clases que no pueden ser instanciadas directamente y están
 diseñadas para servir como plantillas para otras clases.

 Sirve para que nuestro codigo sea mas claro
'''

#ABC permite escribir una jerarquia de clases mas robusta y escribir codigo mas mantenible
from abc import ABCMeta, abstractmethod


#sin usar ABC y los posibles problemas, si instanciamos directamente en esta clase podria marcar error
class ClaseBase1:
    def metodo_1(self):
        #Indica que no se ha implimentado tal metodo
        raise NotImplementedError

    def metodo_2(self):
        raise NotImplementedError

class ClaseConcreta1(ClaseBase1):
    #Implementacin de la clase padre
    def metodo_1(self):
        print('Metodo implementado')

    #El meodo 2 no se va a implementar
    #Esto ya es un problema porque no se reporta la falta de implementacion

#Hay un problema, se puede instanciar la clase padre, pero podria arrojar un error
clase_base = ClaseBase1()
#clase_base.metodo_1()

#Esto funciona segun los esperado
clase_concreta1 = ClaseConcreta1()
clase_concreta1.metodo_1()
#El metodo 2 no ha sido definida por la clase hija, si se manda a llamar el metodo de la clase padre arrojara error
#clase_concreta1.metodo_2()


#clase abstractas parte 2
#Vamos a resolver los detalles anteriores usando ABC
class ClaseBase2(metaclass=ABCMeta):
    #No tenemos que agregar la implementacion al ser un metodo abstracto, tambien lo importamos
    @abstractmethod
    def metodo_1(self):
        pass

    @abstractmethod
    def metodo_2(self):
        pass

class ClaseConcreta2(ClaseBase2):
    def metodo_1(self):
        print('Metodo 1 implementado')

    #dejamos sin implementar el metodo 2
    def metodo_2(self):
        print('Metodo 2 implementado')

#Intentamos crear un objeto de la clase base y esto no es posible, marca error tampoco podemos usar los metodos abstractos
#clase_base = ClaseBase2()

#Instanciamos la clase concreta 2, se deben de implementar todos los metodos de la clase Base o padre, si no marcara error
clase_concreta = ClaseConcreta2()
clase_concreta.metodo_1()
clase_concreta.metodo_2()



