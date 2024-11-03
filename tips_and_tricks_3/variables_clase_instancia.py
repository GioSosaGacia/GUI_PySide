'''
Diferencia entre variables de clase y variables de instancia es decir las variables que se asocian a objetos
'''

class Perro:
    no_patas = 4 #<- Variable de clase, se comparte para todos los objetos

    def __init__(self,nombre):
        self.nombre = nombre #<- variable de insancia

#definimos algunos objetos
layla = Perro('Layla')
venus = Perro('Venus')

#Cada objeto tiene su propio atributo de nombre
print(layla.nombre, venus.nombre)

#La variable de clase se puede acceder con el nombre de la clase o con los objetos
print(layla.no_patas, venus.no_patas, Perro.no_patas)

#si tratamos de acceder la variable de instancia desde la clase no es posible, solo de los objetos creados desde la misma clase
#print(Perro.nombre)

#si queremos modificar la no_patas para todos los perros
Perro.no_patas = 5


#si queremos modificar el numero de patas a un solo perro
venus.no_patas = 6 #Aqui ocurre un detalle, se crea la variable de instancia pero se oculta la variable de clase
print(layla.no_patas, venus.no_patas, Perro.no_patas)

#imprimimos el valor de la variable de instancia y ademas la varible de clase
print(' ')
print(venus.no_patas, venus.__class__.no_patas)


#si creamos una variable desde la clase
#ya se variable o clase, siempre utilizaran la variable mas cercana a ellos, como en este caso que Perro usa nombre que es la variable de la clase
#y no la variable nombre creada en la instancia
Perro.nombre = 'Clase perro'
print(layla.nombre, venus.nombre, Perro.nombre)


#Si definimos una variable de clase que no esta en los objetos
#en esta ocacion los objetos si pueden acceder a las variables de clase
Perro.no_orejas = 2
print(layla.no_orejas, venus.no_orejas, Perro.no_orejas)



#Contador de objetos de una clase
#Implementación erronea
#las variables de instancia ocultan a las variables de clase
class ContadorObjetosErronea:
    no_instancias = 0

    def __init__(self):
        self.no_instancias += 1

print('Contador de instancias Erroneo'.center(60,'-'))
print(ContadorObjetosErronea.no_instancias)
#esta variable es la de instancia y no de la clase ya que la de instancia la oculta
print(ContadorObjetosErronea().no_instancias)
print(ContadorObjetosErronea().no_instancias)


#Implementacion correcta
class ContadorObjetos:
    no_instancias = 0

    def __init__(self):
        #incrementamos la variable de clase, para acceder a ella es con .__class__ o usando el nombre de clase.no_instancia
        #self.ContadorObjetos.no_instancias += 1
        self.__class__.no_instancias += 1

print('Contador instancias')
#accedemos al valor de la variable de clase
print(ContadorObjetos.no_instancias)
#Creamos un nuevo objeto ()
print(ContadorObjetos().no_instancias)
print(ContadorObjetos().no_instancias)
print(ContadorObjetos().no_instancias)

