'''
comparacion del uso del operador == o el operador is en POO
'''

#El operador == comapra el contenido de 2 objetos(contenido igual)
#no necesariamente son el mismo objeto(pueden apuntar a objetos distintos

#El operador is revisa si dos objetos son iguales(objetos son identicos
#Ambos deben de estar apuntando a la misma direccion de memoria para ser iguales


lista = [1,2,3]
lista_b = lista

#En este caso tanto la lista a y b tienen el mismo contenido (==True)
#y tambien apunta a la misma refencia is regresa True
print(f'La lista a y b tienen el mismo contenid? -> {lista == lista_b}')
print(f'Lista a y b apuntan al mismo objeto? -> {lista is lista_b}')

#Sin embargo si creamos un nuevo objeto
#el constructor de list apunta a un objeto nuevo
lista_c = list(lista)
#En este caso la lista a tiene el mismo contenido que c(== es True
#pero... lista c apunta a un objeto distinto en memoria (is es Falso
print(f'Lista a y c? -> {lista == lista_c}')
print(f'Lista a y c apunta al mismo objeto en memoria? -> {lista is lista_c}')
