#Copia de atributos de objetos
import copy


#Definimos una clase de tipo Punto 2d
class Punto:
    def __init__(self,x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Punto: ({self.x!r}, {self.y!r})'

#Definimos manualmente la comprobacion de los atributos de nuestra clase y retorne True, sin comparar la referencia y solo
    #compare los atributos, esto se usa para saber si dos objetos tienen el mismo contemido
    def __eq__(self, other):
        return isinstance(other,Punto) and self.x == other.x and self.y == other.y

punto_a = Punto(2,3)
punto_b = copy.copy(punto_a)

#Copia poco profunda (shallow), crea un nuevo objeto con el mismo contnido
print(f'Copia poco profunda (shallow)')
#da falso porque al usar== tambien compara la referencia en memoria y obvio es otra para que de true debemos de usar
#__eq__ de equal
print(f'Punto a: {punto_a}')
print(f'Punto b: {punto_b}')
print(f'Son objetos con el mismo contenido:? {punto_a == punto_b}')
print(f'Son los mismos objetos(misma referencia):? {punto_a is punto_b}')

#Clase rectangulo utiliza dos puntos como referencia -> superior izquierdo e inferior derecho, para crear un rectangulo
class Rectangulo:
    def __init__(self,sup_izq, inf_der):
        self.sup_izq = sup_izq
        self.inf_der = inf_der

        #retorna la inf en formato de tipo constructor
    def __repr__(self):
        return f'Rectangulo: ({self.sup_izq!r}, {self.inf_der!r})'

rectangulo1 = Rectangulo(Punto(0,1), Punto(3,4))
#Copia Superficial
print(f'Copia superficial de rectangulos')
rectangulo2 = copy.copy(rectangulo1)
print(f'Rectangulo 1: {rectangulo1}')
print(f'Rectangulo 2: {rectangulo2}')
#debido a que la copia fue superficial un cambio en un punto afecta a otro rectangulo
rectangulo1.inf_der.y = 6
print(f'Cambio en un punto afect al otro rectangulo(shallow copy')
print(f'Rectangulo 1: {rectangulo1}')
print(f'Rectangulo 2: {rectangulo2}')

print(f'Creacion de copia profunda o deepcopy'.center(80,'-'))
rectangulo3 = copy.deepcopy(rectangulo1)
#Modificamos un valor en un punto, no afecta al otro rectangulo(copia profunda)
rectangulo3.sup_izq.x = 2
rectangulo1.sup_izq.y = 2
print(f'Cambio en un punrto No afecta al otro rectangulo (deepCopy')
print(f'Rectangulo 1: {rectangulo1}')
print(f'Rectangulo 3: {rectangulo3}')
