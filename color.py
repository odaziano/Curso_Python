""" Módulo color:
## 7.3. Evitando que un módulo se ejecute al importarlo
Cuando importamos un módulo, Python ejecuta todo el código que se encuentra en el módulo.
Si queremos evitar que se ejecute el código al importar el módulo, debemos colocar el código dentro de un bloque `if` de la siguiente forma:
if __name__ == '__main__':
    # Hacer algo
    pass
De lo contrario, como es el caso del presente módulo, se ejecutará directamente """

negro =     '\033[30m'
rojo =      '\033[91m'
verde =     '\033[92m'
amarillo =  '\033[93m'
azul =      '\033[94m'
magenta =   '\033[95m'
cyan =      '\033[96m'
blanco =    '\033[97m'
naranja =   '\033[38;5;208m'

negrita =   '\033[1m'
italica =   '\033[3m'

famarillo = '\033[48;5;226m'    # Fondo amarillo
fnegro =    '\033[40m'          # Fondo negro

back =      '\033[0m'           # Color y formato x defecto



"""
En Python, :.2f es una especificación de formato que se utiliza al formatear números en una cadena (string). Esta especificación
controla la cantidad de dígitos que se mostrarán después del punto decimal cuando se formatea un número en punto flotante.
:: Marca el comienzo de la especificación de formato.
.2: Indica que se deben mostrar dos dígitos después del punto decimal.
f: Indica que el número es un número de punto flotante.

Colores
'\033[91m': Rojo
'\033[92m': Verde
'\033[93m': Amarillo
'\033[94m': Azul
'\033[95m': Magenta
'\033[96m': Cyan
'\033[97m': Blanco
'\033[30m': Negro
'\033[0m' : Retorna al color anterior

Formatos
Negrita
'\033[1m' activa el modo de texto en negrita, y '\033[0m' lo desactiva
Itálica
'\033[3m' activa el modo de texto en itálica, y '\033[0m' lo desactiva
Fondo
# Ejemplo de fondo amarillo (puedes cambiar el número según el color que desees)
print('\033[48;5;226m' + 'Este es un párrafo con fondo amarillo.' + '\033[0m')
print('\033[40m' + 'Este es un fondo negro.' + '\033[0m')

En este ejemplo, 48 indica que estás cambiando el color de fondo, 5 indica que estás utilizando un color definido por el sistema, y 226 es el número de color específico para el amarillo. La secuencia '\033[0m' se utiliza nuevamente para restablecer la configuración predeterminada del fondo.
 """