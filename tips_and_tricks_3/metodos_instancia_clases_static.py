class MiClase:

    def metodo_instancia(self):
        #sabemos que es de instancia porque lleva la palabra self
        #retornar una tupla de valores,self para que se imprima la inf de este metodo en memoria
        return 'Metodo de instancia ejecutado', self

    @classmethod
    def metodo_clase(cls):
        #retornamos una tupla
        #pueden  acceder al estado de la clase: metodos o atributos
        return 'metodo de clase ejecutado...', cls

    @staticmethod
        # no reciben parametro o argumento
        # no pueden  acceder al estado de la clase: metodos o atributos, solo se asocian con la clase, no pueden modificar el estado
    def metodo_estatico():
        return 'Metodo estatico ejecutado...'

#siempre debemos de pasar la referencia de un objeto
#cAso 1: ejecutamos el metodo de intancia de manera implicita
objeto = MiClase()
print(objeto.metodo_instancia())
#Caso 2: ejecutamos el metodo de instancia de manera explicita
print(MiClase.metodo_instancia(objeto))
#caso 3. ejecutamos el metodo de instancia desde la clase
print(MiClase.metodo_instancia(MiClase))
#caso 4 los metodos de clase y estaticos se asocian a la clase misma
#Utilizando MiClase., por el punto se manda la referencias al metodo de clase que es cls
print(MiClase.metodo_clase())
#caso 5. desde las instancias podemos acceder a los met de clase, con el . en automatico se pasa el argumento ya sea self o cls
print(objeto.metodo_clase())

#caso 6. metodo estatico, no tiene acceso a la inf de los objetos ni de la clase
#son de utileria para generar calculos
print(MiClase.metodo_estatico())
#caso 7 lo ejecutamos desde la instamcia
print(objeto.metodo_estatico())
