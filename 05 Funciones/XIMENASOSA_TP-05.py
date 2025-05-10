# /// Ejercicio 1 / Crear una lista con múltiplos de 4 del 1 al 100 ///

#Lista usando range con inicio en 4, fin en 101 y salto de 4
lista_multiplos_4 = list(range(4, 101, 4))

#Muestra la lista resultante
print(lista_multiplos_4)

# /// Ejercicio 2 / Crear una lista con cinco elementos y mostrar el penúltimo ///

#Lista con cinco elementos
cosas_que_me_gustan = ["pizza", "juegos", "playa", "perros", "fútbol"]

#Muestra el penúltimo elemento usando índice negativo
print(cosas_que_me_gustan[-2])

# /// Ejercicio 3 / Crear una lista vacía, agregar tres palabras con append e imprimirla ///

#Lista vacía
lista_vacia = []

#Agrego tres palabras con append
lista_vacia.append("sol")
lista_vacia.append("escritorio")
lista_vacia.append("impresora")

#Imprime la lista resultante
print(lista_vacia)

# /// Ejercicio 4 / Reemplazar el segundo y último valor de la lista “animales” ///

#Lista original
animales = ["perro", "gato", "conejo", "pez"]

#Reemplaza el segundo valor por "loro"
animales[1] = "loro"

#Reemplaza el último valor por "oso"
animales[-1] = "oso"

#Muestra la lista resultante
print(animales)

# /// Ejercicio 5 / Explicación: este código elimina el número más grande de la lista "numeros" y luego imprime la lista actualizada ///

#Define una lista de números
numeros = [8, 15, 3, 22, 7]

#Elimina el valor máximo de la lista
numeros.remove(max(numeros))

#Muestra la lista resultante sin el número mayor
print(numeros)

# /// Ejercicio 6 / Crear lista con números del 10 al 30 con saltos de 5 y mostrar los dos primeros ///

#Lista con números del 10 al 30 inclusive, saltando de 5 en 5
numeros = list(range(10, 31, 5))

#Imprime los dos primeros elementos de la lista
print(numeros[0])
print(numeros[1])

# /// Ejercicio 7 / Reemplazar los valores centrales de la lista autos ///

#La lista original con cuatro elementos
autos = ["sedan", "polo", "suran", "gol"]

#Reemplaza los valores en los índices 1 y 2
autos[1] = "cruze"
autos[2] = "yaris"

#Imprime la lista actualizada
print(autos)

# /// Ejercicio 8 / Crear una lista con los dobles de 5, 10 y 15 usando append ///

#Lista vacía
dobles = []

#Agrega los dobles directamente con append
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

#Imprime la lista resultante
print(dobles)

# /// Ejercicio 9 / Listas con productos de compras ///

#Lista de compras por cliente
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

#Agrega "jugo" a la lista del tercer cliente
compras[2].append("jugo")

#Reemplaza "fideos" por "tallarines" en la lista del segundo cliente
compras[1][1] = "tallarines"

#Elimina "pan" de la lista del primer cliente
compras[0].remove("pan")

#Imprime la lista resultante
print(compras)

# /// Ejercicio 10 / Crear una lista anidada con distintos elementos ///

#Lista anidada con los elementos especificados
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

#Imprime la lista resultante
print(lista_anidada)
