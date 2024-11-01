'''
Desempaquetado de argumnetos cuando estamos trabajando con funciones en python
Vamos a trabajar con un vector x,y,z
'''

def imprimir_vector(x,y,z):
    print(f'<{x}, {y}, {z}>')

imprimir_vector(10,3,9)

#Desempaquetar un iterable -> tupla, lista, set, etc.
tupla_vector = (8,2,15)
#si no usamos el * la tupla solo se pasa a la variable x aunque estemos pasando una tupla con 3 elementos
#Para que se pasen los elementos de la tupla debemos de aplicar el desempaquetado y usar el *
imprimir_vector(*tupla_vector)
#imprimir_vector(tupla_vector ) marca error por no agregar el * para desempaquetar


#lista
lista_vector = [3,4,5]
imprimir_vector(*lista_vector)

#Desempaquetar un generador
expresion_generador = (x * x for x in range(3))
imprimir_vector(*expresion_generador)

#Desempaquetar un diccionario
diccionario_vector = {'x':10, 'y':3, 'z':4}
imprimir_vector(**diccionario_vector)
#pasar las llaves y no los valores, solo utilizamos un * en vez de  **
imprimir_vector(*diccionario_vector)


print('Valores None'.center(60,'-'))
#Valores retornado None
#Una funcion en python simpre va ha retornar un valor y si no regresa ningun valor sera NOne
#De manera explicita retorna none
def funcion1(valor):
    if valor:
        return valor
    else:
        return None

print(funcion1(0))


#De manera implicita retorna none
def funcion2(valor):
    if valor:
        return valor
print(funcion2(0))


def funcion3(valor):
    print(valor)

funcion3(10)
#print(funcion3(10)) marca con porque manda a imprimir dos veces la funcion y solo ahi un recurso

