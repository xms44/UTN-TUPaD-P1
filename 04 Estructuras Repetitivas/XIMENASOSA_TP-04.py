# /// Ejercicio 1: Mostrar números del 0 al 100 en orden creciente /// 

for numero in range(0, 101):
    print(numero)


# /// Ejercicio 2 / Contar la cantidad de dígitos de un número ///

#Se solicita al usuario un número entero
numero = int(input("Ingrese un número entero: "))

#Se inicializa un contador de dígitos
contador = 0

#Se usa el valor absoluto para evitar errores con números negativos
n = abs(numero)

#Si el número es 0, se cuenta como un dígito
if n == 0:
    contador = 1
else:
    while n > 0:
        n = n // 10  #División entera para eliminar el último dígito
        contador += 1

#Se muestra el resultado
print(f"El número tiene {contador} dígito(s).")

# /// Ejercicio 3 / Sumar los enteros entre dos valores dados, excluyéndolos ///

#Se solicitan los dos valores al usuario
inicio = int(input("Ingrese el primer número: "))
fin = int(input("Ingrese el segundo número: "))

#Se asegura el orden correcto de los valores
if inicio > fin:
    inicio, fin = fin, inicio

#Se inicializa la suma
suma = 0

#Se suman los valores entre los extremos (excluyéndolos)
for numero in range(inicio + 1, fin):
    suma += numero

#Se muestra el resultado
print(f"La suma de los enteros entre {inicio} y {fin} (excluyéndolos) es: {suma}")

# /// Ejercicio 4 / Sumar números ingresados hasta que el usuario ingrese 0 ///

#Se inicializa la variable acumuladora
total = 0

#Se solicita números al usuario hasta que ingrese 0
while True:
    numero = int(input("Ingrese un número (0 para finalizar): "))
    if numero == 0:
        break
    total += numero

#Se muestra el resultado final
print(f"La suma total es: {total}")

# /// Ejercicio 5 / Adivinar un número aleatorio entre 0 y 9 ///

#Se importa el módulo random para generar un número aleatorio
import random

#Se genera un número aleatorio entre 0 y 9
numero_secreto = random.randint(0, 9)

#Se inicializa el contador de intentos
intentos = 0

#Se inicia el bucle de adivinanza
while True:
    adivinanza = int(input("Adiviná el número (entre 0 y 9): "))
    intentos += 1
    if adivinanza == numero_secreto:
        break

#Se muestra el resultado final
print(f"¡Correcto! Adivinaste el número en {intentos} intento(s).")

# /// Ejercicio 6 / Mostrar los números pares entre 0 y 100 en orden decreciente ///

#Se recorre desde 100 hasta 0, bajando de 2 en 2
for numero in range(100, -1, -2):
    print(numero)

# /// Ejercicio 7 / Sumar todos los números desde 0 hasta un número ingresado ///

#Se solicita al usuario un número entero positivo
limite = int(input("Ingrese un número entero positivo: "))

#Se inicializa la variable suma
suma = 0

#Se recorre desde 0 hasta el número ingresado, incluyendo ese número
for numero in range(0, limite + 1):
    suma += numero

#Se muestra el resultado
print(f"La suma de los números desde 0 hasta {limite} es: {suma}")

# /// Ejercicio 8 / Contar pares, impares, positivos y negativos entre 100 números ingresados ///

#Se define cuántos números se van a ingresar
cantidad = 100  #Cambiar este valor si querés probar con menos

#Se inicializan los contadores
pares = 0
impares = 0
positivos = 0
negativos = 0

#Se inicia el bucle de ingreso de números
for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i + 1}: "))

    #Se clasifica como positivo o negativo
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

    #Se clasifica como par o impar
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

#Se muestran los resultados
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")

# /// Ejercicio 9 / Calcular la media de 100 números ingresados por el usuario ///

#Se define cuántos números se van a ingresar
cantidad = 100  #Cambiar este valor si querés probar con menos

#Se inicializa el acumulador
suma_total = 0

#Se ingresan los números y se acumulan
for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    suma_total += numero

#Se calcula la media
media = suma_total / cantidad

#Se muestra el resultado
print(f"La media de los {cantidad} números ingresados es: {media}")

# /// Ejercicio 10 / Invertir los dígitos de un número ingresado ///

#Se solicita al usuario un número entero
numero = int(input("Ingrese un número entero: "))

#Se convierte el número a positivo si es negativo, para no incluir el signo en la inversión
positivo = abs(numero)

#Se invierten los dígitos usando slicing sobre la conversión a string
invertido = int(str(positivo)[::-1])

#Se muestra el resultado (conservando el signo si era negativo)
if numero < 0:
    invertido = -invertido

print(f"El número invertido es: {invertido}")