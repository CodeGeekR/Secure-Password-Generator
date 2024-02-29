import string
import random
from zxcvbn import zxcvbn
import pyperclip


def generar_contrasena(longitud):
    """
    Esta función genera una contraseña segura de una longitud dada.

    Parámetros:
    longitud (int): la longitud de la contraseña a generar.

    Devuelve:
    str: la contraseña generada.
    """

    # Todos los caracteres posibles que la contraseña puede tener
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Generar la contraseña
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))

    return contrasena

def verificar_fortaleza(contrasena):
    resultado = zxcvbn(contrasena)
    return resultado['score']

# Solicitar al usuario la longitud de la contraseña
longitud = int(input("Ingrese la longitud de la contraseña que desea generar: "))

while longitud < 8:
    print("La longitud de la contraseña debe ser al menos 8")
    longitud = int(input("Ingrese la longitud de la contraseña que desea generar: "))

# Generar la contraseña
contrasena = generar_contrasena(longitud)

# Imprimir la contraseña generada
print("La contraseña generada es: ", contrasena)
# Copiar la contraseña al portapapeles
pyperclip.copy(contrasena)
print("La contraseña se copió al portapapeles")

score = verificar_fortaleza(contrasena)
print(f"La fortaleza de la contraseña es: {score} (0 = muy débil, 4 = muy fuerte)")
