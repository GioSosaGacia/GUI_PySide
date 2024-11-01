'''
Como definir clases de exepcion personalizada
Crear una clase para definir una clase de exepcion personalizada

'''
#Validar que un nombre no pueda tener menos de 3 caracteres
#Este tipo de validacion no indica cual es el problema en especifico
def validar(nombre_completo):
    if len(nombre_completo) < 3:
        raise ValueError
    else:
        print('Validacion Correcta')

#nombre = 'Jn'
#validar(nombre)

#cREANDO CLASES DE EXEPCION PERSONALIZADAS
#Validacion personalizada, indica cual es el problema
'''class NombreDemasiadoCorto(ValueError):
    pass

def validar_mejorado(nombre_completo):
    if len(nombre_completo) < 3:
        #arrojamos la exepcion de la clase y pasamos el nombre que causo el error
        raise NombreDemasiadoCorto(nombre_completo)
    else:
        print('Validacion correcta')

nombre = 'Ka'
validar_mejorado(nombre)
'''

#mejorado
#es buena idea crear una clase base y de ahi extender las demas clases de exepcion personalizada
class ClaseExepcionBase(TypeError):
    pass

class NombreDemasiadoCorto(ClaseExepcionBase):
    pass

def validar_mejorado(nombre_completo):
    if len(nombre_completo) < 3:
        #arrojamos la exepcion de la clase y pasamos el nombre que causo el error
        raise NombreDemasiadoCorto(nombre_completo)
    else:
        print('Validacion correcta...')

nombre = 'Ka'
try:
    validar_mejorado(nombre)
except Exception as e:
    #con el __traceback__ podemos obtener el numero de la linea y en que archivo se mostro el error
    print(f'{type(e).__name__}, linea: {e.__traceback__.tb_lineno}en {__file__}: {e}')
