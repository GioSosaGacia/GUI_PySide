'''
Funciones: son ciudadanos de primera clase, lo que indica que podemos declarar una funcion en cualquier
parte de nuestro archivo.py y la podemos tratar como un objeto,
no podemos mandar a llamar una funcion sin antes definirla
'''

def mayusculas(texto):
    return texto.upper()

#Uso normal de una funcion
print(mayusculas('hola'))

#Uso de la funcion como un objeto
#Podemos asignar la referencia de una funcion a una variable sin usar los parentesis
variable_funcion = mayusculas
#ambas apuntan al mismo objeto en memoria
print(f'Variable: {variable_funcion}')
print(f'Funcion mayusculas: {mayusculas}')


#Utilizamos la variable funcion en cualquier momento
print(f'Variable: {variable_funcion("Nuevo Texto")}')

#podemos demostrar que son objetos eliminando la referencia original de la variable
#del mayusculas

#Aun asi podemos utilizar la funcion con la variable funcion
print(variable_funcion('Saludos...'))

#marca error por que la funcion ya se ha eliminado
#print(mayusculas('Ya se elimino'))

#Para saber el nombre por default que se le asigna a una funcion
print(f'Nombre por default de la funcion: {variable_funcion.__name__}')
print(f'Nombre por default: {mayusculas("Nombre default")}')
print(f'Nombre original de la funcion: {mayusculas.__name__}')




print(' ')
print('Pasar funciones a otras funciones'.center(50,'-'))
print('Como almacenar una funcion en una estructura de datos'.center(70,'-'))

#como almecenar una funcion en una estrucrura de datos
lista_funciones = [mayusculas, variable_funcion, str.upper]
print(lista_funciones)
print(' ')

#acceder a cada una de las funciones
for funcion in lista_funciones:
    print(funcion, funcion('Saludos desde la funcion'))


#Tambien podemos acceder directamente a las funciones almacenadas en nuestra lista
print(lista_funciones[1]('Saludos desde variable_funcion'))






print('Pasar funciones a otras funciones'.center(50,'-'))
#podemos pasar funciones a otras funciones
#se le conoce como higher-order-funtions
def saludar(arguemnto_funcion):
    #usamos la funcion que recivimos como argumento y devolvemos la referencia de esta funcion
    referencia_funcion_retornada = arguemnto_funcion('Hola!! saludos, desde mi funcion')
    print(referencia_funcion_retornada)

#Llamamos la funcion saludar, pasamos la referencia de una funcion como argumento
saludar(mayusculas)

#Podemos pasar una nueva implementacion de la funcion que pasamos como argumentos
def minusculas(texto):
    return texto.lower()

saludar(minusculas)

#El clasico ejemplo de higher order funtion is the funtion map
#Esta funcion toma una funcion como referencia, y un iterable, llama a la funcion base
#y la plica an cada elememnto del iterable proporcionado

#map nos permite aplicar una función sobre los elementos
# de un objeto iterable (lista,tupla, etc...).
print(list(map(mayusculas,['Texto1','Texto2','Texto3'])))
print(list(map(minusculas,['Texto1','Texto2','Texto3'])))





print('Funciones anidadas'.center(50,'-'))
#Funciones anidadas, son funciones dentro de otra funcion
def mostrar(texto):
    #definicion de la funcion interna o anidada
    def convertir_minusculas(t):
        return t.lower()
    #Una vez definica la funcion interna la mandamos llamar
    return convertir_minusculas(texto)


#cada vez que se llama la funcion mostrar se crea la funcion interna convertir_minusculas
print(mostrar('Giovanni Desde Funcion Anidada...'))
#no podemos utilizar la funcion interna desde la funcion externa



##retornar la funcion anidada
#observar que  en ningun momento se manda a llamar la funcion anidada desde la funcion externa
def hablar(volumen):
    def minusculas(texto):
        return texto.lower()
    def mayusculas(texto):
        return texto.upper()
    if volumen > 0.5:
        return mayusculas
    else:
        return minusculas

#utilizamos la funcion
print(hablar(0.6)('Hablo fuerte...!!'))
print(hablar(0.3)('Hablo suave...!!'))

variable_minusculas = hablar(0.1)
print(variable_minusculas('ES LO MAS BAJO QUE PUEDO HABLAR'))



print('Funciones closure'.center(50,'-'))
#funciones closure: son funciones internas que utilizan los argumentos de funcion externa
#las funciones internas pueden capturar y guardar el estado de la funcion externa o padre
#por estado nos referimos a las variables que almacena la funcion mas externa
def hablar(texto,volumen):
    #la funcion interna ya no recive parametros
    #utilizan el estado de la funcion padre o externa
    def minusculas():
        return texto.lower()
    def mayusculas():
        return texto.upper()
    if volumen > 0.5:
        #no usamos la referencia si no la funcion
        return mayusculas()
    else:
        return minusculas()

print(hablar('Hablo fuerte mother fucker!!',0.8))
print(hablar('Hablo suave mother fucker!!',0.2))

#ejemplo 2
#capturar y guardar el estado de una funcion mas externa
#podemos preconfigurar una funcion, depende como se configure mostrará un titulo
def mostrar(titulo):
    #definimos la funcion anidada o interna
    def saludar(mensaje):
        return titulo + '. ' + mensaje
    return saludar
mostrar_ing = mostrar('Ingeniero')
mostrar_lic = mostrar('Licenciado')

#podemos seguir usando el estado de la funcion previamente configurada
#aunque el valor de titulo ya esta fuera del alcance scope
print(mostrar_ing('Giovanni Sosa '))
print(mostrar_lic('Angelica Aneliz'))




print('')

#In Python, callable() is a built-in function used to check if an object can be called like a function.
#If an object is "callable," it means you can use () to call it and potentially pass arguments to it.
print('Funcion callable'.center(60,'-'))
#La funcion callable permite saber si un objeto se puede llamar o no
#todas las funciones en python son objetos
#pero no todos en python son funciones
print(f'Se puede llamar el objeto mostrar como funcion?: {callable(mostrar)}')
print(f'SE puede llamar el objeto hablar como funcion?: {callable(hablar)}')
print(f'SE puede llamar el objeto mostrar_ing como funcion?: {callable(mostrar_ing)}')
print(f'Se puede llamar el objeto cualquier cadena como funcion?: {callable("Cualquier texto")}')



#podemos crear clases que definan objetos y se puedan llama como funciones, debemos de usar
#dumder call __call__
class Mostrar():
    def __init__(self, titulo):
        self.titulo = titulo

    def __call__(self, mensaje):
        return self.titulo + '. ' + mensaje

doctor = Mostrar('Doctor')
print(doctor('Luis David Sosa'))
print(f'Se puede llamar el objeto doctor como una funcion?: {callable(doctor)}')

