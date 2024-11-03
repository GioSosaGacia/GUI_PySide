'''
Named tuple son una extencion del tipo tupla
Son una buena alternativa para escribir clases, donde sus atributos son tipo inmutables igual que las tuplas
#una ventaja es que podemos asignar un identificador a cada elemento de la tupla
'''

from collections import namedtuple

#definimos una clase con atributos inmutables usando named tuple
#1.Nombre de la clase
#2.Atributos
Persona1 = namedtuple('Persona1','nombre apellido edad')

#creamos una instancia de la clase(en automatico se agrega un constructor por default, con los atributos agregados)
persona1 = Persona1('Juan','Perez',28)

#En uatomatico se crea un metodo repr__ con los atributos proporcindos
print(persona1)

#Tambien podempos crear nuestra clase usando una lista
print(' ')
Persona2 = namedtuple('Persona2', ['nombre','apellido','edad'])
persona2 = Persona2('Karla','Gomez',30)
print(persona2)

#Podemos acceder a los atributos de manera individual por nombre o por indice
print(f'Nombre: {persona2.nombre}, Apellido: {persona2.apellido}, Edad: {persona2.edad}')
#accedemos a los atributos por indice, si nos accedemos o equivocamos de indice marcara error
print(f'Nombre: {persona2[0]}, Apellido: {persona2[1]}, Edad: {persona2[2]}')

#Podemos convertir los valores a una tupla, pero se perderan los nombres de los atributos
print(tuple(persona2))

#Tambien podemos hacer Unpacking de los elementos de la tupla
nomebre, apellido, edad = persona2
print(f'Valores de la tupla persona: {nomebre},{apellido},{edad}')

#Podemos hacer unpacking pasando como argumentos, mediante el uso de *
print(*persona2)
#Las tuplas son inmutables al igual que namedtuple
#persona2.edad = 30


#Subclase de namedTuple
print(f'Creando subclase namedtuple'.center(60,'-'))
class Persona3(Persona2):
    #Agregamos un nuevo metodo a la clase hija
    def covertir_matusculas(self):
        return f'Nombre completo: {self.nombre.upper()} {self.apellido.upper()}'


persona3 = Persona3('Angelica', 'Aneliz',39)
print(persona3)
print(persona3.covertir_matusculas())


#Otra forma de crear una clase hija sin usar namedtuple, extendemos de Persona2 y con .fields a sus atributos, para agregar unos mas solo concatenamos
Persona4 = namedtuple('Persona4', Persona2._fields + ('email',))
#creamos un objeto de persona4 con el nuevo atributo email
persona4 = Persona4('Luis David','Sosa',23,'luis@gmail.com')
print(persona4)

#Metodos de ayuda de tipo built-in
print(f'Metodos de ayuda de tipo built-in'.center(60,'-'))
print(persona4._fields)
#convertir los elementos a un diccionario
diccionario_persona4 = persona4._asdict()
print(diccionario_persona4)
