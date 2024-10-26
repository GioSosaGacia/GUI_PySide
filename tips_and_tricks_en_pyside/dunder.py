'''
Dunder significa doble guion bajo or double underscore
'''
''''''
class Padre():
    def __init__(self):
        #al usar dunder al inicio y final de la variable no se aplica el concepto de name mangling
        self.__variable_privada = 10
        self.__variable_dunder__ = 15


#Uso de guion bajo como variable temporal o que no se va a utilizar en nuestro programa
#El guion bajo simple se utiliza por convencion y se usa para indicar
#que una variable es temporal o sin importancia, ademas se puede omitir su impresion
for _ in range(3):
     print(f'Hola... {_} ')

#Tambien lo podemos utilizar cuando trabajamos con tuplas:
valores = ('Juan', 'Perez', 31)
nombre, _, edad = valores
print(f'Nombre: {nombre}')
print(nombre)
print(edad)
print(_)

#Se puede usar como variable temporal de cualquier tipo
_ = list()
_.append(1)
_.append(2)
_.append(3)
print(f'Variable temporal que apunta a una lista: {_}')
print(' ')

if __name__ == '__main__':
    padre = Padre()
    print(dir(padre))
    print(f'Accediendo a la variable dunder: {padre._Padre__variable_privada}')
    print(f'Accediendo a la variable dunder: {padre.__variable_dunder__}')
