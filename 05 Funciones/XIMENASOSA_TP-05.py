# /// Ejercicio 1 / Crear una lista con múltiplos de 4 del 1 al 100 ///

# Lista de múltiplos de 4 usando range
lista_multiplos_4 = list(range(4, 101, 4))

# Imprime la lista
print(lista_multiplos_4)

# /// Ejercicio 2 / Crear una lista con cinco elementos y mostrar el penúltimo ///

# Lista con cosas que me gustan
cosas_que_me_gustan = ["pizza", "juegos", "playa", "perros", "fútbol"]

# Muestra el penúltimo elemento
print(cosas_que_me_gustan[-2])

# /// Ejercicio 3 / Crear una lista vacía, agregar tres palabras con append e imprimirla ///

# Lista vacía
lista_vacia = []

# Agrega tres palabras
lista_vacia.append("sol")
lista_vacia.append("escritorio")
lista_vacia.append("impresora")

# Muestra la lista
print(lista_vacia)

# /// Ejercicio 4 / Reemplazar el segundo y último valor de la lista “animales” ///

# Lista de animales
animales = ["perro", "gato", "conejo", "pez"]

# Cambia el segundo por "loro"
animales[1] = "loro"

# Cambia el último por "oso"
animales[-1] = "oso"

# Imprime la lista
print(animales)

# /// Ejercicio 5 / Eliminar el número más grande de la lista ///

# Lista de números
numeros = [8, 15, 3, 22, 7]

# Elimina el máximo
numeros.remove(max(numeros))

# Imprime la lista sin el mayor
print(numeros)

# /// Ejercicio 6 / Crear lista con números del 10 al 30 con saltos de 5 y mostrar los dos primeros ///

# Lista del 10 al 30 saltando de 5
numeros = list(range(10, 31, 5))

# Imprime los dos primeros
print(numeros[0])
print(numeros[1])

# /// Ejercicio 7 / Reemplazar los valores centrales de la lista autos ///

# Lista de autos
autos = ["sedan", "polo", "suran", "gol"]

# Cambia el segundo y el tercero
autos[1] = "cruze"
autos[2] = "yaris"

# Muestra la lista actualizada
print(autos)

# /// Ejercicio 8 / Crear una lista con los dobles de 5, 10 y 15 usando append ///

# Lista vacía
dobles = []

# Agrega los dobles
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

# Muestra la lista
print(dobles)

# /// Ejercicio 9 / Listas con productos de compras ///

# Lista de compras por cliente
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# Agrega "jugo" al tercer cliente
compras[2].append("jugo")

# Cambia "fideos" por "tallarines" en el segundo cliente
compras[1][1] = "tallarines"

# Elimina "pan" del primer cliente
compras[0].remove("pan")

# Muestra la lista
print(compras)

# /// Ejercicio 10 / Crear una lista anidada con distintos elementos ///

# Lista anidada
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

# Muestra la lista
print(lista_anidada)
