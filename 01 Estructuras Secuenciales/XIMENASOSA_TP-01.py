# Actividad 1
print("Hola Mundo!")

# Actividad 2
nombre = input("¿Cuál es tu nombre? ")
print(f"Hola {nombre}!")

# Actividad 3
nombre = input("Cuál es tu nombre? ")
apellido = input("Cuál es tu apellido? ")
edad = input("Cuál es tu edad? ")
residencia = input("Dónde vivís? ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Actividad 4
import math
radio = float(input("Ingresa el radio del circulo: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio
print(f"Área: {area:.2f}")
print(f"Perímetro: {perimetro:.2f}")

# Actividad 5
segundos = int(input("Ingresa la cantidad de segundos: "))
horas = segundos / 3600
print(f"Equivale a {horas:.2f} horas")

# Actividad 6
numero = int(input("Ingresa un número: "))
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# Actividad 7
num1 = int(input("Ingresa el primer número (distinto de 0): "))
num2 = int(input("Ingresa el segundo número (distinto de 0): "))
#
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
#
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division:.2f}")

# Actividad 8
peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))
bmi = peso / (altura ** 2)
print(f"Tu índice de masa corporal es: {bmi:.2f}")

# Actividad 9
celsius = float(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit = (9 / 5) * celsius + 32
print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

# Actividad 10
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los tres números es: {promedio:.2f}")
