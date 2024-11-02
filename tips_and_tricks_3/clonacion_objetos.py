#La clonacion o copia de informacion de objetos depende de la cantidad de niveles de inf que tengamos en cierto objeto
#Existeb 2 tipos

import copy

#1. Copia superficial o shallow deep  o copia poco profunda
lista_a = [[1,2],[3,4],[5,6]]

#copia superficial shallow
lista_b = list(lista_a)

#las listas son dos objetos distintos, apuntan a diferente pposicion de memoria,pero los niveles
#mas internos, solo se copio la referencia, no se crearon nuevos objetos
print(f'Lista a: {lista_a}')
print(f'Lista b: {lista_b}')

#comprobación de que los objetos son distintos a nivel superior
#Un cabio en el nivel superior, no afecta a la otra lista
lista_a.append([7,8])
print(f'Son distintos objetos a nivel superior')
print(f'Lista a: {lista_a}')
print(f'Lista b: {lista_b}')
#Comprobación de que los objetos internos tienen la misma referencia es decir que se realizo una copia suoerficial
#Si hacemos un cambio en un elemento de una sublista, afecta a la otra sublista de la otra referencia/lista
lista_a[0][1] = 'A'
print(f'La copia fue superficial, los elementos internos solo se copio la referencia')
print(f'Lista a: {lista_a}')
print(f'Lista b: {lista_b}')

#crear copias profundas importando copy
lista_c = [[1,2],[3,4],[5,6]]
lista_d = copy.deepcopy(lista_c)
#Comprobación de que son objetos distintos:
lista_c.append([7,8])
print(f'Son distintos objetos a nivel superior')
print(f'Lista c: {lista_c}')
print(f'Lista d: {lista_d}')
#Ahora si los elemento s internos o sublistas son nuevos objetos, no solo se copia la referencia
lista_c[0][1]= 'A'
print(f'Lista c: {lista_c}')
print(f'Lista d: {lista_d}')
#eLMETODO COPY SIRVE para realizar copias poco profundas(shallow)
