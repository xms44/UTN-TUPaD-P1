# /// Ejercicio 1 / Verificar si el usuario es mayor de edad /// 

#Se solicita la edad
edad = int(input("Ingrese su edad: "))

#Condición para saber si es mayor
if edad >= 18:
    print("Es mayor de edad")

# /// Ejercicio 2 / Verificar si el usuario aprueba o no /// 

#Se solicita la nota del usuario
nota = int(input("Ingrese su nota: "))

#Determina si está aprobado o desaprobado
if 0 <= nota <= 10:
    if nota >= 6:
        print("Aprobado")
    else:
        print("Desaprobado")
else:
    print("Nota inválida, debe ser entre 0 y 10")

# /// Ejercicio 3 / Verificar si el número ingresado es par /// 

#Se solicita un número al usuario
numero = int(input("Ingrese un número: "))

#Verifica si el número es par usando el operador módulo (%)
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# /// Ejercicio 4 / Clasificar edad según categoría /// 

#Se solicita la edad del usuario
edad = int(input("Ingrese su edad: "))

#Se evalúa a qué categoría pertenece
if edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# /// Ejercicio 5 / Verificar longitud de contraseña /// 

#Solicita la contraseña al usuario
contraseña = input("Ingrese su contraseña: ")

#Verifica si la longitud está entre 8 y 14 caracteres inclusive
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# /// Ejercicio 6 / Determinar tipo de sesgo en una lista de números /// 

import random
from statistics import mode, median, mean

#Se genera una lista de 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

#Cálculo de estadísticos
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

#Imprime la lista y los valores estadísticos
print("Lista generada:", numeros_aleatorios)
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

#Determina el tipo de sesgo
if media > mediana > moda:
    print("Sesgo positivo (a la derecha).")
elif media < mediana < moda:
    print("Sesgo negativo (a la izquierda).")
elif media == mediana == moda:
    print("Sin sesgo (distribución simétrica).")
else:
    print("No se puede determinar un sesgo claro.")

# /// Ejercicio 7 / Verificar si la frase termina con vocal /// 

#Solicita una frase al usuario
frase = input("Ingrese una frase o palabra: ")

#Verifica si termina con una vocal (mayúscula o minúscula)
if frase[-1].lower() in 'aeiou':
    frase += "!"  #Agrega signo de exclamación si termina en vocal

#Imprime el resultado
print(frase)

# /// Ejercicio 8 / Formatear nombre según opción elegida /// 

#Solicita nombre al usuario
nombre = input("Ingrese su nombre: ")

#Solicita una opción al usuario
print("Seleccione una opción:")
print("1. Mostrar en mayúsculas")
print("2. Mostrar en minúsculas")
print("3. Mostrar con la primera letra en mayúscula")
opcion = input("Ingrese 1, 2 o 3: ")

#Aplica la transformación correspondiente
if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción inválida. Por favor ingrese 1, 2 o 3.")

# /// Ejercicio 9 / Clasificar magnitud de un terremoto según la escala de Richter /// 

#Solicita al usuario la magnitud del terremoto
magnitud = float(input("Ingrese la magnitud del terremoto: "))

#Clasificación según la escala de Richter
if magnitud < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitud < 7:
    print("Muy fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

# /// Ejercicio 10 / Determinar la estación del año según fecha y hemisferio /// 

#Se solicita la ubicación del usuario
hemisferio = input("¿En qué hemisferio estás? (N/S): ").upper()

#Se solicita el mes y día
mes = int(input("Ingrese el número del mes (1 a 12): "))
dia = int(input("Ingrese el día del mes: "))

#Se determina la estación según la fecha
if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
else:
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"

#Mostrar el resultado según el hemisferio
if hemisferio == "N":
    print("Estás en", estacion_norte)
elif hemisferio == "S":
    print("Estás en", estacion_sur)
else:
    print("Hemisferio no válido. Ingrese N o S.")

