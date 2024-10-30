'''
Las funciones lambda permiten declarar funciones en una sola linea de manera anonima,
no es necesaruio
'''
def sumar(a,b):
    return a + b

print(sumar(5,5))

#funion lambda
#una funcion landa la podemos usar sin necesidad de ligarla a una variable ya que es una funcion anonima
#1.nombre, lambda, parametros, expresion/lo que vamos a retornar
sumar_labda = lambda a, b: a + b
print(sumar_labda(3,987))

#utilizando una sola linea
print((lambda a, b: a + b)(5,9))

#Como utilizar una funcion lambda, la podemos usar siempre que necesitemos una funcion muy concreta
#ordenar una lista de tuplas, por su segundo valor proporcionando una llave
lista_tuplas = [(1,'b'),(2,'f'),(5,'a'),(4,'c')]
#lista_tuplas_ordenada = sorted(lista_tuplas,key=lambda tupla: tupla[0], reverse=True)
lista_tuplas_ordenada = sorted(lista_tuplas,key=lambda tupla: tupla[1],reverse=True)
print(lista_tuplas_ordenada)



#Otro ejemplo de ordenamiento usando una expresión lambda
#funcion abs o valor absoluto no considera signos
print('')
print(list(range(-3,4) ))
#si queremos ordenar por el valor absoluto -> sin considerar signo
for valor in range(-3,4):
    print(valor, valor * valor)
#Ahora lo aplicamos a una funcion lambda
#En Python, el argumento key en funciones como sorted(), min(), y max() permite especificar una función que se
# aplicará a cada elemento antes de hacer la comparación. El nombre key es simplemente un nombre predefinido
# para este parámetro en estas funciones y describe cómo se realizará el criterio de ordenamiento o de selección.
listar_ordenada = sorted(range(-3,4), key=lambda valor: valor * valor)
print(listar_ordenada)



#las funciones landa tambien podemos aplicar el concepto de closure, donde desde una funcion interna podemos acceder al estado
#de la funcion más externa
print('')
def mostrar_titulo(titulo):
    return lambda mensaje: titulo + '. ' + mensaje
mostrar_ing = mostrar_titulo('Ingeniero')
mostrar_lic = mostrar_titulo('Licenciado')

print(mostrar_ing('Carlos Lara'))
print(mostrar_lic('Maria del Rosario'))


#Malos usos de funciones lambda: casos de funciones lambda que no son recomendados
class Prueba:
    mostrar = lambda self: print('Función mostrar')
    saludar = lambda self: print('Función saludar')
prueba = Prueba()
prueba.mostrar()
prueba.saludar()




print(' ')
#Otro ejemplo donde una funcion lambda agregaria complejidad innecesaria
'''
filter(lambda valor: valor % 2 == 0, range(10)):

filter() es una función que toma dos argumentos:
Una función que devuelve True o False para cada elemento.
Un iterable (en este caso, range(10)).
La función filter() pasa cada elemento de range(10) a la función lambda valor: valor % 2 == 0.
lambda valor: valor % 2 == 0 es una función anónima (lambda) que toma un valor y verifica si es par (valor % 2 == 0).
Si el resultado es True (es par), el valor se mantiene en el resultado de filter.
Si el resultado es False, se excluye.
'''
lista_pares = list(filter(lambda valor: valor % 2 == 0, range(10)))
print(lista_pares)

#con list comprehentios, sintaxis -> [ expresión for elemento in iterable if condición ]
#expresión: La operación o transformación que deseas aplicar a cada elemento.
#elemento: Cada elemento del iterable (lista, rango, etc.).
#condición (opcional): Una condición que filtra los elementos; si es True, el elemento se incluye en la lista final.

lista_pares_modificada = [ valor for valor in range(10) if valor % 2 == 0]
print(lista_pares_modificada)
cuadrados = [x**2 for x in range(10)]
print(cuadrados)
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
