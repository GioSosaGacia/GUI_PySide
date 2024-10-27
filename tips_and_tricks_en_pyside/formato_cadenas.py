'''
Formas para dar formato a cadenas en python
%s = str
%i = entero
%x = hexadecimal
%f = float
'''

#1. Estilo antiguo %s nos permite concatenar s -> str con % + la variable es lo que agregara en el %s entre ' '
nombre = "Juan"
mi_cadena = 'Hola, %s' %nombre
print(mi_cadena)

#Tambien podemos hacer converciones de tipos, enteros a hexadecimales, etc.
error = 500
cade_hexadecimal = 'Error en hexadecimal: %x ' %error
print(cade_hexadecimal)

#si queremos pasar varios valores debemos de usar una tupla()
cadena = 'Hola %s hay un error: %x' % (nombre, error)
print(cadena)

#podemos referenciar por sustitucion de variables, usando un diccionario
#en este caso podemos reutilizar las variables
cadena = 'hola %(nombre)s hay un error: %(error)x, %(nombre)s ' % {'nombre': nombre, 'error':error} #nombre dentro de la cadena : nombre de la variable a utilizar
print(cadena)



'''
Formato cadenas nuevo 
'''
#2. Formato de cadenas actualizado conocido como: format, fstring
nombre = 'Giovanni'
mi_cadena = 'Hola, {}' .format(nombre)
print(mi_cadena)

#podemos convertir enteros a hexadecimales  .format(etiqueta=nombre de la variable), entro de la etiqueta podemos cambiar el tipo de dato
#en este caso lo comvertimos a hexadecimal
error = 500
cadena_hexadecimal = 'Error en hexadecimal: {error:x}' .format(error=error)
print(cadena_hexadecimal)

#De entero a flotante
entero = 50
cadena_flotante = 'Numero flotante: {entero:0.2f}'.format(entero=entero)
print(cadena_flotante)

'''
Usando f-string o interpolation 
'''
#3.
mi_cadena = f'Hola: {nombre}'
print(mi_cadena)
#mandar a imprimir diectamente sin declrara una variable
print(f'Hola, {nombre}')
#Este es el mismo ejemplo del valor de hexadecimal con string interpolation
print(f'Error en hexadecimal: {error:x}')
#mismo ejemplo deimpresion de entero a flotante
print(f'Numero flotante: {entero:0.2f}')
#string literal puede incluir expresiones o llamadas a funciones
a = 10
b = 3
print(f'Dividimos y damos formato: {a/b:.2f}')


'''
Zen de python, basicamente son la reglas de python para escribir un codigo legible 
Son los tips 
'''
import  this

