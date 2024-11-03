'''
Diccionarios en python -> dict
Puden implementarse en multiples formas
Se les conoce como maps, hashmaps, lookup tables, etc, se implementan con key:value


defaultdict es una subclase de dict en Python que proporciona un valor por defecto para las claves que no existen en el diccionario.
'''

#diccionario -> directorio llave nombre, valor:telefono
diccionario = {
    'Juan': 3326036684,
    'Aneliz': 3344556677,
    'Luis': 9988776655,
}

print(diccionario)
#recuperar un elemento
print(diccionario['Juan'])

#Arroja un error de tipo keyerror al no encontrar una llave
#print(diccionario['Gio'])


#Podemos usar una expresion para crear un diccionario
#x-> llave, x+x-> valor
valores_al_cuadrado = {x: x*x  for x in range(5)}
print(valores_al_cuadrado)

#no se puede crear un diccionario a partir de una [] lista ya que es mutable, marcara error
#lista = [1,2,3]
#diccionario_erroneo = {lista : 'A'}
#print(diccionario_erroneo)

#diccionario a partir de una tupla
tuple = (1,2,3,4,5)
diccionario_correcto = {tuple: 'a'}
print(diccionario_correcto)


#Diccionarios ordenados
print(f'Diccionarios ordenados'.center(60,'-'))
#si queremos garantizar un orden de irsercion debemos de utilizar "OrderedDict
from collections import OrderedDict, defaultdict

diccionario_ordenado = OrderedDict(uno=1,dos=2,tres=3)#no usamos ''
print(diccionario_ordenado)
#agregamos un nuevo elemento
diccionario_ordenado['cuatro'] = 4
print(diccionario_ordenado)

#obtener las llaves
print(diccionario_ordenado.keys())
print(diccionario_ordenado.values())

#si cambiamos algun valor de una llave, las llaves son inmutables, solo se puede camiar el valor y mantiene el orden
diccionario_ordenado['uno'] = -1
print(diccionario_ordenado)

#eliminamos una llave
diccionario_ordenado.pop('tres')
print(diccionario_ordenado)

#insertar el elemento eliminado, sigue respetando el orden como se fueron agregando
diccionario_ordenado['tres'] = 3
print(diccionario_ordenado)


print(f'Diccionario de tipo defaul dict'.center(60,'-'))
#defauldict es una subclase de la clase dict
diccionario_default = defaultdict(lambda : 'Valor Erroneo')
diccionario_default['a'] = 1
diccionario_default['b'] = 2
print(diccionario_default.items())

#Imprimir un elemento que no existe
print(diccionario_default['c'])

#Podemos crear valores por defaul como una lista
diccionario_default_lista = defaultdict(list)
#si accedemos a una llave no existente la crea y los valores se asignan como una lista
diccionario_default_lista['nombres'].append('Juan')
diccionario_default_lista['nombres'].append('Karla')
diccionario_default_lista['nombres'].append('Laura')
print(diccionario_default_lista)
print(diccionario_default_lista.items())
print(diccionario_default_lista.keys())
print(diccionario_default_lista.values())




#Mezclando diccionarios y diccionarios de solo lectura
#buscar en multiples diccionarios como si fuera un diccionario unico
from collections import ChainMap
print(f'Mezclando diccionarios y diccionarios de solo lectura'.center(80,'-'))
diccionario1 = {'uni':1, 'dos':2,'tres':3, 'cinco':'a'}
diccionario2 = {'cuatro':4, 'cinco':5}

#Combinacion de diccionarios
combinacion_diccionarios = ChainMap(diccionario1,diccionario2)
print(combinacion_diccionarios)

#Buscamos en todos los diccionarios de izq a der como si fuera uno solo, la primera clave que encuentre es la que arrojara
print(combinacion_diccionarios['cinco'])

#Una llave no existente, arrojara un keyerror
#print(combinacion_diccionarios['seis'])


print('dICCIONARIO DE SOLO LECTUTA'.center(50,'-'))
#obtencion de diccionarios de solo lectura
from types import MappingProxyType
diccionario_modificable = {'uno':1,'dos':2,'tres':3}
diccionario_solo_lectura = MappingProxyType(diccionario_modificable)

#leemos el valor del diccionario
print(diccionario_solo_lectura)
print(diccionario_solo_lectura['uno'])
#si queremos modificar el valor del diccionario arrojara error ya que es de solo lectura
#diccionario_solo_lectura['uno'] = -1
#print(diccionario_solo_lectura)

#Si modificamos al diccionario mutable afecta al de solo lectura
diccionario_modificable['dos'] = 22
print(diccionario_modificable) # se pueden hacer cambios en el original y afectara al solo lectura,
print(diccionario_solo_lectura)
