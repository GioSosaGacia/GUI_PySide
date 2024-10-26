'''
Aserciones:
Las aserciones ayudan a depurar los programas de errores de los cuales no nos podemos recuperar
El uso del afirmar en Python nos permite verificar que una determinada condición sea True, y de no serlo, se lanzará una excepción.

 Son herramientas que ayudan a garantizar que el programa se esté comportando como se espera en puntos
 específicos.
 assert condición, "Mensaje opcional de error"

'''

#Ejemplo 1, revisamos si la dicicion es entre cero 0 assert

def divicion(a,b):
    assert b != 0, 'Divicion entre 0'
    print(f'Resultado divicion: {a/b}')


#Ejemplo 2 Realizamos el calculo del promedio de una lista de calificaciones
def obtener_promedio(calificacione):
    #si la lista esta vacia no deberi de continuar el programa
    assert len(calificacione) != 0, 'Lista de calificaciones vacia'
    print(f'El promedio final de calificaciones es: {sum(calificacione)/len(calificacione)}')

#Ejemplo tres realizamos un descuento al producto seleccionado
def aplicar_descuento(productos, descuento):
    precio_con_descuento = productos['precio'] * (1.0 - descuento)
    print(f'Precio sin descuento = { productos["precio"]}')
    print(f'Nuevo precio del producto: {precio_con_descuento:0.2f}')
    #si el precio con descuento es mayor o igual a 0 o menor o igual al precio del producto
    assert  0 <= precio_con_descuento <= productos ['precio'], f'DEscuento invalido: {precio_con_descuento:0.2f}'
    print('Descuento Valido')



if __name__ == '__main__':
    #Ejemplo 1 divicion(2,0)
    divicion(10,5)
    #Ejemplo 2
    calificaciones =[7,8,9,10,8,9]
    #calificaciones = []
    obtener_promedio(calificaciones)

    #ejemplo 3
    productos ={'nombre':'playera', 'precio':1500}
    aplicar_descuento(productos,0.10)
