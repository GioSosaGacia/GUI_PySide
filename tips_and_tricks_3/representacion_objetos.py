# __str__ su objetvo es que la informacion sea legible para el usuario
#__repr__ su objetivo es que la informacion no se ambigua
#se utiliza para hacer debugging (tiene un formato tipo constructor)
#La implementacion por defaul del str es llamar al metodo repr(representacion de objeto)

class Auto:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    #por defaul solo se muestra el nombre de la clase y id del objeto(direccion)
#sin el metodo str o repr solo manda el nombre de la clase y la direccion del objeto
audi_a3 = Auto('Audi','a3','Rojo')
print(audi_a3)

class AutoStr:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def __str__(self):
        return f'str: Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}'

    #def __repr__(self):
     #   return f'repr: Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}'

#Metodo repr muestra la inf tipo contructor, con el nombre de la clase + los atributos
    #se usa parentesis porque contendra varias lineas
    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.marca!r},{self.modelo!r},{self.color!r})')

aidi_a1 = AutoStr('Audi', 'a1', 'Blanco')
#diferentes formas de imprimir el objeto, el metodo str se manda a llamar utilizando el metodo str
print(aidi_a1)
print(aidi_a1.__str__())
print(str(aidi_a1))
print('{}'.format(aidi_a1))
print(f'{aidi_a1}')

#Sin embargo es mas recomendable usar repr en lugar de str, str llama por defaulf a repr
#cualquier coleccion usa repr en lugar de str para mostrar la informacion
print([aidi_a1])
#Tambien podemos llamar al metodo repr-> usando !r podemos mandar a llamar al metodo repr
print(f'{aidi_a1!r}')


#TAMBIEN DE manera manual podemos elegir que metodo utilizar repr o str
print(str(aidi_a1))
print(f'{aidi_a1!r}')
