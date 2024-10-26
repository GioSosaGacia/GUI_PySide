'''
Context manager
In Python, a context manager is a construct that allows you to set up and tear down resources precisely
and automatically using the with statement. It's commonly used to manage resources like file handling,
 network connections, database connections, and more, ensuring that they are cleaned up after use (even if errors occur).
'''
from contextlib import contextmanager

with open('prueba.txt','w') as archivo:
    archivo.write('Hola desde python')

#equivalente al uso de with
#archivo = open('prueba.txt','w')
#try:
 #   archivo.write('Hola desde python...')
#finally:
 #   archivo.close()


#Esto no es equivalente:
archivo = open('prueba.txt','w')
archivo.write('Hola sin with ')
#esto no aseguro el cierre de recurso en caso de error
archivo.close()


#manejo de context manager en clases, ahi dos opciones
#1. Implementando el protocolo con las funciones (__enter__) y (__exit__)


#1er opcion
class ManejoArchivos:
    def __init__(self, nombre):
        self.nombre = nombre

    def __enter__(self):
        self.archivo = open(self.nombre, 'w')
        return self.archivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.archivo:
            self.archivo.close()

#context manager con lalibreria de contextlib, requiere del uso de generadores y decoradores
#este metodo es un generador, en primer lugar adquiere el recurso
#posteriormente suspende temporalment la ejecucion al utilizar yield
#cuando de ser utilizado este metodo, regresa la eecucion y cierra el recurso
@contextmanager
def manejador_archivos(nombre):
    try:
        archivo = open(nombre,'w')
        #abre y suspende el archivo para agregar inf
        yield archivo
    finally:
        archivo.close()
        print('Informacion agregada a prueba.txt')

#Ejersicion de la clase para agregar in identador
class Identador():
    def __init__(self):
        self.nivel = 0

    def __enter__(self):
        self.nivel += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.nivel -= 1

    def imprimir(self, texto):
        print(' '*self.nivel + texto)

#identador con contextlib
class Identador2():
    def __init__(self):
        self.nivel = 0

    @contextmanager
    def identador(self):
        try:
            self.nivel += 1
            yield self
        finally:
            self.nivel -= 1
    def imprimir(self,texto):
        print(' ' * self.nivel + texto)

if __name__ == '__main__':
    with ManejoArchivos('prueba.txt') as archivo:
        archivo.write('Prueba desde ManejoArchivos')
    #prueba con la libreria de contextlib
    with manejador_archivos('prueba.txt') as archivo:
        archivo.write('Prueba desde el decorador')
        archivo.write('\nadios')
    #prueba de iterador
    with Identador() as identador:
        identador.imprimir('Primer nivel')
        with identador:
            identador.imprimir('Segundo nivel')
            identador.imprimir('Coninua segundi nivel...')
            with identador:
                identador.imprimir('Tercer nivel: ')
                identador.imprimir('Continua tercer nivel...')
        identador.imprimir('fin del primer nivel')

    #identador2 con contextlib
    print(' ')
    objecto = Identador2()
    with objecto.identador():
        objecto.imprimir('primer nivel')
        objecto.imprimir('continua el primer nivel')
        with objecto.identador():
            objecto.imprimir('segundo nivel')
            with objecto.identador():
                objecto.imprimir('tercer nivel')
                with objecto.identador():
                    objecto.imprimir('cuarto nivel')
        objecto.imprimir('Fin del primer nivel')
