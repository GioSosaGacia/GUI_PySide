'''
Permite extender y modificar el comportamiento de una Funcion, basicamente es una funcion
que recibe una funcion distinta y  a su vez retorna otra distinta
'''

#Ejemplo login, seguridad, caching
#Un decorador es codigo reutilizable
#1. ejemplo de un decorador

def decorador_envolvente(funcion_a_decorar):
    #recibir la funcion y regresarla
    print('Estamos dentro de la funcion decoradora')
    return  funcion_a_decorar

#Ahora utilicemos este decorador
def saludar():
    return 'Saludos desde mi funcion... '

#Llamamos manualmente el decorador: no es lo comun en python
funcion_retornada = decorador_envolvente(saludar)
print(funcion_retornada)

#sintaxis para el uso de decoradores
@decorador_envolvente
#al momento de usar el decorador esta funcion se pasa como parametro a decorador envolvente
#a funcion a decorar
def saludar_funcion_a_decorar():
    #y retorna la funcion a decorar del return de decorador_envolvente  sustituyendolo por la linea de abajo ' '
    return 'Saludos desde funcion a decorar'
print(saludar_funcion_a_decorar())



print(' ')
#2. Ejemplo Decorador que convierte un texto a mayusculas
def mayusculas(funcion_a_decorar):
    def envolvente():
        print('Antes de la llamada a la funcion a decorar')
        #mandamos a llamar la funcion original (closure) -> la cual recibe parametros de funciones externas
        resultado_original = funcion_a_decorar()
        print('Despues de la llamada a la funcion a decorar')
        resultado_modificado = resultado_original.upper()
        return  resultado_modificado
    return envolvente

@mayusculas
def saludar_minusculas():
    return 'hola...'
print(saludar_minusculas())






print('Decoradores multiples: '.center(70,'-'))
#Decoradores multiples: los decoradores se ejecutan from botton to top(desde abajo, hacia arriba)
def negritas(funcion):
    def funcion_envolvete():
        return '<strong>' + funcion() + '</strong>'
    return  funcion_envolvete

def enfatizar(funcion):
    def funcion_envolvente():
        return '<em>' + funcion() + '</em>'
    return funcion_envolvente

@negritas
@enfatizar
def saludar_HTML():
    return 'Hola desde HTML'

print(saludar_HTML())





print('Decoradores con argumentos...'.center(70,'-'))
#Decoradores con argumentos *arg=tupla and **kwargs=diccionario
def decorador_con_argumentos(funcion):
    def funcion_envolvente(*args, **kwargs):
        print('Se esta ejecutando decorador')
        #si vamos a trabajar con los parametros no usamos * o ** y si vamos hacer el desempaquetado(extraer elementos de una estructura de datos como listas, etc) si.
        print('Args: ',args)
        print(f'kwargs: {kwargs}')
        #modificar los argumentos antes de enviarlo:
        lista_arg = []
        for indice, valor_tupla in enumerate(args): #enumerate recorre un iterable y al mismo tiempo obtener el indice y el valor
            lista_arg.append(args[indice].upper())
        #Agregamos mas elememntos a la lista
        lista_arg.append('Nuevo argumento 1')
        lista_arg.append('Nuevo argumento 2')
        #agregamos inf al diccionario
        kwargs['valor 1'] = 'Nuevo valor 1'
        #propagamos los parameros a la funcion original
        #return funcion(*args, **kwargs)
        #Propagar los valores modificados
        return funcion(*lista_arg, **kwargs)#agregamos * para que se desempaquete
    return funcion_envolvente


@decorador_con_argumentos
def funcion_saludar(titulo,nombre, *args, **kwargs):
    #imprimir titulo con el nombre
    print(f'{titulo}. {nombre}')
    #imprimimos los argumentos variables
    print('args: ',args)
    print('kwargs: ', kwargs)

funcion_saludar('Ingeniero', 'Luis Sosa')
