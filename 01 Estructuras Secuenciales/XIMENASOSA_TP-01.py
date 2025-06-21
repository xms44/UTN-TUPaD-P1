# /// Ejercicio 1 ///
# Imprime "Hola Mundo!" en pantalla

print("Hola Mundo!")

# /// Ejercicio 2 ///
# Pide el nombre y saluda

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# /// Ejercicio 3 ///
# Pide nombre, apellido, edad y lugar, y lo muestra en una frase

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("¿Dónde vivís?: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# /// Ejercicio 4 ///
# Pide radio y muestra área y perímetro de un círculo

radio = float(input("Ingrese el radio del círculo: "))
area = 3.14 * radio ** 2
perimetro = 2 * 3.14 * radio
print(f"Área: {area}")
print(f"Perímetro: {perimetro}")

# /// Ejercicio 5 ///
# Pide segundos y muestra cuántas horas representa

segundos = int(input("Ingrese cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas} horas")

# /// Ejercicio 6 ///
# Pide un número y muestra su tabla de multiplicar del 1 al 10

numero = int(input("Ingrese un número: "))
print("Tabla del", numero)
print(numero * 1)
print(numero * 2)
print(numero * 3)
print(numero * 4)
print(numero * 5)
print(numero * 6)
print(numero * 7)
print(numero * 8)
print(numero * 9)
print(numero * 10)

# /// Ejercicio 7 ///
# Pide dos enteros distintos de 0 y muestra suma, resta, multiplicación y división

num1 = int(input("Ingrese un número entero (distinto de 0): "))
num2 = int(input("Ingrese otro número entero (distinto de 0): "))
print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicación: {num1 * num2}")
print(f"División: {num1 / num2}")

# /// Ejercicio 8 ///
# Pide altura y peso, y muestra el índice de masa corporal (IMC)

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / altura ** 2
print(f"Su IMC es {imc}")

# /// Ejercicio 9 ///
# Pide temperatura en Celsius y la muestra en Fahrenheit

celsius = float(input("Ingrese temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32
print(f"{celsius}°C equivale a {fahrenheit}°F")

# /// Ejercicio 10 ///
# Pide tres números y muestra el promedio

n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))
promedio = (n1 + n2 + n3) / 3
print(f"El promedio es {promedio}")
