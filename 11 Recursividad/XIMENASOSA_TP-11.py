# /// Ejercicio 1 / Factorial de todos los números hasta el que indique el usuario ///

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Pide un número al usuario
limite = int(input("Ingresá un número para calcular factoriales: "))

# Muestra los factoriales desde 1 hasta el número indicado
for i in range(1, limite + 1):
    print(f"Factorial de {i}: {factorial(i)}")


# /// Ejercicio 2 / Serie de Fibonacci hasta la posición indicada por el usuario ///

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

posicion = int(input("\nIngresá hasta qué posición querés mostrar la serie de Fibonacci: "))

for i in range(posicion + 1):
    print(fibonacci(i), end=" ")


# /// Ejercicio 3 / Potencia usando recursividad ///

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

base = int(input("\n\nIngresá la base: "))
exponente = int(input("Ingresá el exponente: "))
print(f"{base} elevado a la {exponente} es: {potencia(base, exponente)}")


# /// Ejercicio 4 / Convertir número decimal a binario con recursividad ///

def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("\nIngresá un número para convertir a binario: "))
if numero == 0:
    print("0")
else:
    print("Binario:", decimal_a_binario(numero))


# /// Ejercicio 5 / Ver si una palabra es palíndromo con recursividad ///

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

texto = input("\nIngresá una palabra: ")
print("¿Es palíndromo?", es_palindromo(texto))


# /// Ejercicio 6 / Sumar los dígitos de un número con recursividad ///

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

numero = int(input("\nIngresá un número para sumar sus dígitos: "))
print("Suma de los dígitos:", suma_digitos(numero))


# /// Ejercicio 7 / Contar bloques necesarios para una pirámide ///

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

niveles = int(input("\n¿Cuántos bloques tiene el nivel más bajo?: "))
print("Total de bloques necesarios:", contar_bloques(niveles))


# /// Ejercicio 8 / Contar cuántas veces aparece un dígito ///

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

numero = int(input("\nIngresá un número: "))
digito = int(input("Ingresá un dígito a buscar: "))
print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces.")
